from enum import Enum

class Properties(Enum):
    ogc_fid     = ('OBJECTID',              False)
    kadastrs    = ('Kadastra apzīmējums',   False)
    kvart       = ('Kvartāls',              False)
    nog         = ('Nogabals',              False)
    anog        = ('Apakšnogabals',         False)
    nog_plat    = ('Nogabala platība ha',                               False)
    expl_mezs   = ('Meža platība nogabalā, ha',                         False)
    expl_celi   = ('Ceļu platība nogabalā, ha',                         False)
    expl_gravj  = ('Mel.kad. reģistrēto grāvju platība nogabalā ',      False)
    zkat        = ('Zemju kategorija',                                  True)
    mt          = ('Augšanas apstākļu tips',                            True)
    izc         = ('Mežaudzes izcelsme',                                True)
    p_darbg     = ('Pēdējās saimnieciskās darbības gads',               False)
    p_darbv     = ('Pēdējās saimnieciskās darbības veids',              True)
    p_cirg      = ('Pēdējās ciršanas gads',                             False)
    p_cirp      = ('Pēdējās ciršanas paņēmiens',                        True)
    atj_gads    = ('Atjaunošanas beigu termiņš',                        False)
    
    # Not implemented following features
    # TODO
    plant_audz  = ('Apakšnogabals',         False)
    s10         = ('Apakšnogabals',         False)
    a10         = ('Apakšnogabals',         False)
    h10         = ('Apakšnogabals',         False)
    d10         = ('Apakšnogabals',         False)
    g10         = ('Apakšnogabals',         False)
    n10         = ('Apakšnogabals',         False)
    bv10        = ('Apakšnogabals',         False)
    ba10        = ('Apakšnogabals',         False)
    s11         = ('Apakšnogabals',         False)
    a11         = ('Apakšnogabals',         False)
    h11         = ('Apakšnogabals',         False)
    d11         = ('Apakšnogabals',         False)
    g11         = ('Apakšnogabals',         False)
    n11         = ('Apakšnogabals',         False)
    bv11        = ('Apakšnogabals',         False)
    ba11        = ('Apakšnogabals',         False)
    s12         = ('Apakšnogabals',         False)
    a12         = ('Apakšnogabals',         False)
    h12         = ('Apakšnogabals',         False)
    d12         = ('Apakšnogabals',         False)
    g12         = ('Apakšnogabals',         False)
    n12         = ('Apakšnogabals',         False)
    bv12        = ('Apakšnogabals',         False)
    ba12        = ('Apakšnogabals',         False)
    s13         = ('Apakšnogabals',         False)
    a13         = ('Apakšnogabals',         False)
    h13         = ('Apakšnogabals',         False)
    d13         = ('Apakšnogabals',         False)
    g13         = ('Apakšnogabals',         False)
    n13         = ('Apakšnogabals',         False)
    bv13        = ('Apakšnogabals',         False)
    ba13        = ('Apakšnogabals',         False)
    s14         = ('Apakšnogabals',         False)
    a14         = ('Apakšnogabals',         False)
    h14         = ('Apakšnogabals',         False)
    d14         = ('Apakšnogabals',         False)
    g14         = ('Apakšnogabals',         False)
    n14         = ('Apakšnogabals',         False)
    bv14        = ('Apakšnogabals',         False)
    ba14        = ('Apakšnogabals',         False)
    gtf         = ('Apakšnogabals',         False)
    jaatjauno   = ('Apakšnogabals',         False)
    saimn_d_ie  = ('Apakšnogabals',         False)
    jakopj      = ('Apakšnogabals',         False)


    def __init__(self, long_name, coded_value):
        self.long_name = long_name
        self.coded_value = coded_value
        '''If coded value == True, use CodedValues class to decode
        Not yet implemented'''

class CodedValues(Enum):
    VALUE_30    = 'Meža lauce'
    VALUE_31    = 'Meža lauce'
    VALUE_32    = 'Dzīvnieku barošanās lauce'
    '''
    Not implemented yet
    '''

    def __init__(self, description):
        self.description = description


if __name__ == '__main__':
    pass
    # x = getattr(Properties, 'anog')
    # print(x.long_name)