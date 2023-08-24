#!/usr/bin/env python
"""
This script import *csv file, which contains 'nogabals', 'kadastrs', 'kvart'.
And generate *kml file fro drone mission planning
__author__ = "Jēkabs Jaunslavietis"
"""
import os, sys
import logging
import getopt

import json
import csv
import owslib.wfs
import owslib.fes
from owslib.etree import etree

from ogc_filter.filter import OgcFilter

KADASTRS = 'kadastrs'
KVARTALS = 'kvart'
NOGABALS = 'nog'

column_names = [KADASTRS, KVARTALS, NOGABALS]

fields = []
rows = []


# Set up logging system
logger = logging.getLogger('main')
logging.basicConfig(format='%(name)s:%(levelname)s:%(message)s', stream=sys.stderr ,level = logging.INFO)



def main(argv):
    arg_input_file = 'input.csv'
    arg_help = f'Pass argument as -> {argv[0]} -i <input_filename.csv>'

    if(len(argv) != 1):
        try:
            opts, args = getopt.getopt(argv[1:], 'hi:', ['help', 'input='])
        except:
            print(arg_help)
            sys.exit(-1)
        
        if(len(opts) == 0):
            print(arg_help)
            sys.exit()

        for opt, arg in opts:
            if opt in ('-h', '--help'):
                print(arg_help)
                sys.exit()
            elif opt in ('-i', '--input'):
                arg_input_file = arg
            else:
                print(arg_help)
                sys.exit()
        logger.info(f'CSV data will be read from {arg_input_file}')
    else:
        logger.info(f'Using default filename: {arg_input_file}')

    # Parse CSV file
    process_csv(arg_input_file)

    # Connect to WFS service
    wfs = setup_wfs()
    logger.debug(wfs.get_schema('publicwfs:vmdpubliccompartments')['properties'])

    # Generate MKL and metadata info
    extract_data(wfs)

    
def setup_wfs():
    service_link = 'https://lvmgeoserver.lvm.lv/geoserver/publicwfs/ows?service=wfs&'\
    'version=2.0.0&request=GetCapabilities&layer=publicwfs:vmdpubliccompartments'

    try:
        wfs = owslib.wfs.WebFeatureService(service_link, timeout=10, version = '1.1.0')
    except:
        logger.fatal('owslib.wfs.WebFeatureService(): connection failed')
        sys.exit()

    keys = '\n' + '\n'.join(wfs.contents.keys())
    logger.debug(keys)
    return wfs

def process_csv(filename):
    # Check if file exists
    if(not os.path.exists(filename)):
        logger.fatal(f'Could not find file: "{filename}"!')
        sys.exit()

    with open(filename, 'r') as csvfile:

        csvreader = csv.reader(csvfile)

        # extraxct field name from 1st row
        try:
            fields = next(csvreader)
        except StopIteration:
            logger.fatal('CSV file is empty')
            sys.exit()
        
        if fields != column_names:
            logger.error(f'CSV column names are wrong. Correct names: {column_names} '\
                         f'But entered: {fields}')
            sys.exit()

        # Extract each data row
        for row in csvreader:
            logger.debug(f'Total number of rows: {csvreader.line_num}')

            if(len(row) != len(fields)):
                logger.error(f'In CSV file, line {csvreader.line_num}. has {len(row)} records, '\
                             f'but are only {len(fields)} allowed.')
                sys.exit()
            
            try:
                row_int = [int(i) for i in row]
            except:
                logger.error(f'In CSV file, line {csvreader.line_num}. has '\
                             f'invalid literal for int() with base 10.')
                sys.exit()
            rows.append(row_int)

        logger.debug(f'Total number of rows: {csvreader.line_num}')
        logger.debug(fields)
        logger.debug(rows[:5])


def extract_data(wfs):
    layer_name = 'publicwfs:vmdpubliccompartments'
    filter_gen = OgcFilter()
    
    for row in rows:
        filter = filter_gen.generate_filter(row[0], row[1], row[2])
        
        feature = wfs.getfeature(typename = [layer_name],
                                 maxfeatures = 10,
                                 #propertyname=['kadastrs', 'kvart'],
                                 filter = filter,
                                 outputFormat = 'application/json')

        res = json.loads(feature.read())
        if(not(res['numberMatched'] == 1 and res['numberReturned'] == 1)):
            logger.error(f'Could not find exactly 1 geometry for input data:'\
                         f'kadastrs: {row[0]}, kvartāls: {row[1]}, nogabals: {row[2]}.'\
                         f'Returned {res["numberMatched"]} instances.'\
                         f'Check input data to generate files. Skipping input for now...')
            continue

        doc_name = '_'.join(str(i) for i in row)

        # Generate folder for each disctrict
        current_path = os.getcwd()
        path = os.path.join(current_path, doc_name)
        try:
            os.mkdir(path)
        except OSError as error:
            logger.error(error)
        
        logger.debug(res)
        assert len(res['features']) == 1

        logger.debug(res['features'][0]['geometry'])

        with open(doc_name+'/'+doc_name+'.txt', 'w') as outfile:
            outfile.write(str(res['features'][0]['geometry']))
            


if __name__ == '__main__':
    main(sys.argv)