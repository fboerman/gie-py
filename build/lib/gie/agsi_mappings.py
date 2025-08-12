import enum
from typing import Union


def lookup_company(s: Union['AGSICompany', str]) -> 'AGSICompany':
    if isinstance(s, AGSICompany):
        # If it already is an ASGICompany object, we're happy
        return s
    else:  # It is a string
        try:
            # do lookup
            return AGSICompany[s]
        except KeyError:
            # It is not, it may be a direct code
            try:
                return [obj for obj in AGSICompany if obj.value == s][0]
            except IndexError:
                raise ValueError('Invalid company string')


def lookup_storage(s: Union['AGSIStorage', str]) -> 'AGSIStorage':
    if isinstance(s, AGSIStorage):
        # If it already is an ASGIStorage object, we're happy
        return s
    else:  # It is a string
        try:
            # do lookup
            return AGSIStorage[s]
        except KeyError:
            # It is not, it may be a direct code
            try:
                return [obj for obj in AGSIStorage if obj.value == s][0]
            except IndexError:
                raise ValueError('Invalid storage string')


def lookup_country(s: Union['AGSICountry', str]) -> 'AGSICountry':
    if isinstance(s, AGSICountry):
        # If it already is an AGSICountry object, we're happy
        return s
    else:  # It is a string
        try:
            # do lookup
            return AGSICountry[s]
        except KeyError:
            # It is not, it may be a direct code
            try:
                return [obj for obj in AGSICountry if obj.value == s][0]
            except IndexError:
                raise ValueError('Invalid country string')


class AGSICountry(enum.Enum):
    """
    ENUM contains 2 things: code and full name

    """

    def __new__(cls, *args, **kwds):
        obj = object.__new__(cls)
        obj._value_ = args[0]
        return obj

    # ignore the first param since it's already set by __new__
    def __init__(self, _: str, full_name: str):
        self._full_name = full_name

    def __str__(self):
        return self.value

    @property
    def full_name(self):
        return self._full_name

    @property
    def code(self):
        return self.value

    def get_params(self):
        return {
            'country': self.code
        }

    AT = "AT", "Austria"
    BE = "BE", "Belgium"
    BG = "BG", "Bulgaria"
    HR = "HR", "Croatia"
    CZ = "CZ", "Czech Republic"
    DK = "DK", "Denmark"
    FR = "FR", "France"
    DE = "DE", "Germany"
    HU = "HU", "Hungary"
    IE = "IE", "Ireland"
    IT = "IT", "Italy"
    LV = "LV", "Latvia"
    NL = "NL", "Netherlands"
    PL = "PL", "Poland"
    PT = "PT", "Portugal"
    RO = "RO", "Romania"
    SK = "SK", "Slovakia"
    ES = "ES", "Spain"
    SE = "SE", "Sweden"
    GB_pre = "GB", "United Kingdom (Pre-Brexit)"
    RS = "RS", "Serbia"
    UA = "UA", "Ukraine"
    GB = "GB*", "United Kingdom (Post-Brexit)"


class AGSICompany(enum.Enum):
    """
    ENUM containing 2 things about an Area: code, country
    """

    def __new__(cls, *args, **kwds):
        obj = object.__new__(cls)
        obj._value_ = args[0]
        return obj

    # ignore the first param since it's already set by __new__
    def __init__(self, _: str, country: str):
        self._country = country

    def __str__(self):
        return self.value

    @property
    def country(self):
        return self._country

    @property
    def code(self):
        return self.value

    def get_params(self):
        return {
            'country': self.country,
            'company': self.code,
        }

    astora = '21X000000001160J', 'AT'
    gsa = '25X-GSALLC-----E', 'AT'
    omv_gas_storage = '25X-OMVGASSTORA5', 'AT'
    rag_energy_storage = '23X----100225-1C', 'AT'
    uniper_energy_storage_at = '21X000000001127H', 'AT'
    fluxys = '21X-BE-A-A0A0A-Y', 'BE'
    bulgartransgaz = '21X-BG-A-A0A0A-C', 'BG'
    psp = '31X-PSP-OSS-HR-D', 'HR'
    mnd_energy_storage = '27XG-MNDGS-CZ--R', 'CZ'
    moravia_gas_storage = '27X-MORAVIAGS--E', 'CZ'
    rwe_gas_storage_cz = '27XG-RWE-GAS-STI', 'CZ'
    spp_storage = '27X-SPPSTORAGE-R', 'CZ'
    gsd = '21X000000001104T', 'DK'
    storengy = '21X000000001083B', 'FR'
    terega = '21X-FR-B-A0A0A-J', 'FR'
    astora_germany = '21X000000001160J', 'DE'
    bayernugs = '37X0000000000151', 'DE'
    bes = '37X0000000000224', 'DE'
    edf_gas_deutschland = '37X000000000152S', 'DE'
    enbw_etzel_speicher = '11X0-0000-0667-8', 'DE'
    eneco_gasspeicher = '21X0000000010849', 'DE'
    enovos_storage = '**TOBEPROVIDED**', 'DE'
    equinor_storage_deutschland = '21X000000001368W', 'DE'
    erdgasspeicher_peissen = '21X000000001297T', 'DE'
    ekb = '21X000000001080H', 'DE'
    ewe_gasspeicher = '21X0000000011756', 'DE'
    hansewerk = '21X0000000013805', 'DE'
    kge = '21X000000001140P', 'DE'
    met_speicher = '37X000000000047P', 'DE'
    mnd_energy_storage_germany = '37X000000000042Z', 'DE'
    n_ergie = '11XNERGIE------1', 'DE'
    nafta_speicher_inzenham = '21X0000000011748', 'DE'
    nuon_epe_gasspeicher = '37X0000000000119', 'DE'
    omv_gas_storage_germany = '25X-OMVGASSTORA5', 'DE'
    rwe_gas_storage_west = '21X000000001262B', 'DE'
    stadtwerke_hannover = '11XSWHANNOVERAG3', 'DE'
    storengy_deutschland = '21X000000001072G', 'DE'
    swb_vertrieb_bremen = '11XSWB-BREMEN--I', 'DE'
    swkiel_speicher = '37X000000000051Y', 'DE'
    tep = '21X000000001307F', 'DE'
    #total_etzel_gaslager = '**TOBEPROVIDED**', 'DE'
    trianel_gasspeicher_epe = '21X000000001310Q', 'DE'
    uniper_energy_storage = '21X000000001127H', 'DE'
    vng_gasspeicher_gmbh = '21X000000001138C', 'DE'
    hexum = '21X0000000013643', 'HU'
    hgs = '21X0000000013635', 'HU'
    kinsale_energy = '47X0000000000584', 'IE'
    edison_stoccaggio = '21X0000000013651', 'IT'
    igs = '59X4-IGSTORAGE-T', 'IT'
    stogit = '21X000000001250I', 'IT'
    conexus_baltic_grid = '21X000000001379R', 'LV'
    energystock = '21X000000001057C', 'NL'
    ewe_gasspeicher_nl = '21X0000000011756', 'NL'
    nam = '21X000000001075A', 'NL'
    taqa_gas_storage = '21X000000001120V', 'NL'
    taqa_piek_gas = '21X0000000013732', 'NL'
    gsp = '53XPL000000OSMP5', 'PL'
    ren_armazenagem = '21X0000000013627', 'PT'
    depomures = '21X000000001300T', 'RO'
    depogaz_ploiesti = '21X-DEPOGAZ-AGSI', 'RO'
    nafta = '42X-NAFTA-SK---U', 'SK'
    pozagas = '42X-POZAGAS-SK-V', 'SK'
    enagas_gts = '21X0000000013368', 'ES'
    swedegas = '21X-SE-A-A0A0A-F', 'SE'
    centrica_storage = '21X000000001022V', 'GB'
    edf = '23X-EDFE-------W', 'GB'
    humbly_grove_energy = '55XHUMBLYGROVE1H', 'GB'
    scottish_power = '23XSCOTTISHPOWEF', 'GB'
    sse_gas_storage = '23X--140207-SSE9', 'GB'
    storengy_uk = '48XSTORENGYUK01P', 'GB'
    uniper_energy_storage_ltd = '21X0000000013716', 'GB'


class AGSIStorage(enum.Enum):
    """
    ENUM containing 3 things about an Area: code, country, code company
    """

    def __new__(cls, *args, **kwds):
        obj = object.__new__(cls)
        obj._value_ = args[0]
        return obj

    # ignore the first param since it's already set by __new__
    def __init__(self, _: str, country: str, company: str):
        self._country = country
        self._company = company

    def __str__(self):
        return self.value

    @property
    def company(self):
        return self._company

    @property
    def country(self):
        return self._country

    @property
    def code(self):
        return self.value

    def get_params(self):
        return {
            'country': self.country,
            'company': self.company,
            'facility': self.code
        }

    ugs_haidach_astora = '21W000000000078N', 'AT', '21X000000001160J'
    ugs_haidach_gsa = '25W-SPHAID-GAZ-M', 'AT', '25X-GSALLC-----E'
    vgs_omv_tallesbrunn = '21W000000000081Y', 'AT', '25X-OMVGASSTORA5'
    rag_puchkirchen_haag = '21W000000000079L', 'AT', '23X----100225-1C'
    ugs_7_fields_uniper = '21W000000000057V', 'AT', '21X000000001127H'
    ugs_loenhout = '21Z000000000102A', 'BE', '21X-BE-A-A0A0A-Y'
    ugs_chiren = '21W000000000031C', 'BG', '21X-BG-A-A0A0A-C'
    ugs_okoli = '21W000000000077P', 'HR', '31X-PSP-OSS-HR-D'
    ugs_uhrice = '21W000000000075T', 'CZ', '27XG-MNDGS-CZ--R'
    ugs_damborice = '21W000000000102F', 'CZ', '27X-MORAVIAGS--E'
    vgs_rwe_haje = '21W000000000076R', 'CZ', '27XG-RWE-GAS-STI'
    ugs_dolni_bojanovice = '21W000000000074V', 'CZ', '27X-SPPSTORAGE-R'
    vgs_gsd_lille_torup_stenlille = '45W000000000112V', 'DK', '21X000000001104T'
    vgs_saline_tersanne_etrez_manosque = '21W000000000084S', 'FR', '21X000000001083B'
    vgs_sediane_saintilliers = '21W0000000000710', 'FR', '21X000000001083B'
    vgs_sediane_b_gournay = '21W0000000000702', 'FR', '21X000000001083B'
    vgs_serene_atlantique_chemery = '63W197197128864M', 'FR', '21X000000001083B'
    vgs_serene_nord_trois_fontaines_labbaye = '21W000000000073X', 'FR', '21X000000001083B'
    vgs_lussagnet_terega = '21W000000000068Q', 'FR', '21X-FR-B-A0A0A-J'
    ugs_jemgum_h_astora = '21W0000000001148', 'DE', '21X000000001160J'
    ugs_rehden = '21Z000000000271O', 'DE', '21X000000001160J'
    vsp_nord_rehden_jemgum = '21W0000000001261', 'DE', '21X000000001160J'
    ugs_wolfersberg = '21W0000000000184', 'DE', '37X0000000000151'
    ugs_berlin = '21W0000000001083', 'DE', '37X0000000000224'
    vgs_ugs_etzel_edf = '37W000000000003M', 'DE', '37X000000000152S'
    vgs_ugs_etzel_enbw = '11W0-0000-0432-M', 'DE', '11X0-0000-0667-8'
    ugs_enschede_epe_eneco = '21W000000000012G', 'DE', '21X0000000010849'
    ugs_frankenthal = '37Z0000000034538', 'DE', '**TOBEPROVIDED**'
    ugs_etzel_egl_equinor_storage_deutschland = '21W000000000100J', 'DE', '21X000000001368W'
    ugs_katharina = '21W0000000000281', 'DE', '21X000000001297T'
    ugs_etzel_ekb = '21Z000000000291I', 'DE', '21X000000001080H'
    ewe_h = '37W000000000002O', 'DE', '21X0000000011756'
    ugs_ewe_l = '21W0000000001075', 'DE', '21X0000000011756'
    ugs_jemgum_h_ewe = '21W0000000000508', 'DE', '21X0000000011756'
    ugs_nuttermoor_h_2 = '21W000000000104B', 'DE', '21X0000000011756'
    ugs_nuttermoor_h_3 = '21W000000000103D', 'DE', '21X0000000011756'
    ugs_nuttermoor_l_gud = '21W0000000001067', 'DE', '21X0000000011756'
    ugs_rudersdorf_h = '21W000000000048W', 'DE', '21X0000000011756'
    ugs_kraak = '21W000000000020H', 'DE', '21X0000000013805'
    ugs_epe_kge = '21W000000000097J', 'DE', '21X000000001140P'
    ugs_etzel_ese_met = '21W000000000055Z', 'DE', '37X000000000047P'
    ugs_reckrod = '21W0000000000540', 'DE', '37X000000000047P'
    vgs_zone_mnd_esg_ugs_stockstadt = '37Y000000000386Q', 'DE', '37X000000000042Z'
    ugs_eschenfelden_nergie = '21Z000000000321Z', 'DE', '11XNERGIE------1'
    ugs_inzenham_west = '21W0000000000192', 'DE', '21X0000000011748'
    ugs_enschede_epe_nuon = '21W000000000005D', 'DE', '37X0000000000119'
    ugs_etzel_ese_omv = '21W000000000056X', 'DE', '25X-OMVGASSTORA5'
    innexpool_rwegsw = '21W000000000121B', 'DE', '21X000000001262B'
    ugs_epe_l_rwegsw = '21W0000000000532', 'DE', '21X000000001262B'
    ugs_epe_nl_rwegswest = '21W000000000003H', 'DE', '21X000000001262B'
    ugs_kalle_rwegswest = '21W000000000004F', 'DE', '21X000000001262B'
    ugs_stassfurt_rwegswest = '21W0000000000265', 'DE', '21X000000001262B'
    ugs_ronnenberg_empelde = '21Z0000000004002', 'DE', '11XSWHANNOVERAG3'
    ugs_fronhofen = '21W000000000091V', 'DE', '21X000000001072G'
    ugs_harsefeld = '21W000000000092T', 'DE', '21X000000001072G'
    ugs_lesum = '21W000000000090X', 'DE', '21X000000001072G'
    ugs_peckensen = '21W0000000000273', 'DE', '21X000000001072G'
    ugs_schmidhausen = '21W000000000089I', 'DE', '21X000000001072G'
    ugs_uelsen = '21W000000000093R', 'DE', '21X000000001072G'
    ugs_bremen_lesum_swb = '21W000000000090X', 'DE', '11XSWB-BREMEN--I'
    ugs_kiel_ronne = '21W0000000001164', 'DE', '37X000000000051Y'
    ugs_allmenhausen = '21W000000000030E', 'DE', '21X000000001307F'
    ugs_etzel_egl_total_etzel_gaslager = '**TOBEPROVIDED**', 'DE', '**TOBEPROVIDED**'
    ugs_epe_trianel = '21W000000000085Q', 'DE', '21X000000001310Q'
    ugs_bierwang = '21W0000000000613', 'DE', '21X000000001127H'
    ugs_breitbrunn = '21W0000000000605', 'DE', '21X000000001127H'
    ugs_epe_uniper_h= '21W000000000066U', 'DE', '21X000000001127H'
    ugs_epe_uniper_l = '21W000000000065W', 'DE', '21X000000001127H'
    ugs_eschenfelden_uniper = '21W000000000083U', 'DE', '21X000000001127H'
    ugs_etzel_erdgas_lager_egl = '21W000000000059R', 'DE', '21X000000001127H'
    ugs_etzel_ese_uniper_energy_storage = '21W0000000000168', 'DE', '21X000000001127H'
    ugs_krummhorn = '21W000000000067S', 'DE', '21X000000001127H'
    ugs_etzel_ese_vgs = '21W000000000120D', 'DE', '21X000000001138C'
    ugs_jemgum_h_vgs = '21W000000000128Y', 'DE', '21X000000001138C'
    vgs_storage_hub_bernburg = '21W0000000000427', 'DE', '21X000000001138C'
    vgs_vtp_storage_gpl = '21W0000000001091', 'DE', '21X000000001138C'
    ugs_szoreg_1 = '21W000000000086O', 'HU', '21X0000000013643'
    vgs_mfgt_pusztaederics = '21W000000000087M', 'HU', '21X0000000013635'
    ugs_kinsale_southwest = '47W000000000245J', 'IE', '47X0000000000584'
    vgs_edison_stoccaggio_collalto = '21W000000000095N', 'IT', '21X0000000013651'
    ugs_cornegliano = '59W-IGSTORAGE-0Q', 'IT', '59X4-IGSTORAGE-T'
    vgs_stogit_fiume_treste = '21Z000000000274I', 'IT', '21X000000001250I'
    ugs_incukalns = '21W000000000113A', 'LV', '21X000000001379R'
    ugs_energystock = '21W000000000006B', 'NL', '21X000000001057C'
    ugs_nuttermoor_h_1 = '21W0000000001059', 'NL', '21X0000000011756'
    ugs_grijpskerk = '21W000000000001L', 'NL', '21X000000001075A'
    ugs_norg_langelo = '21W000000000015A', 'NL', '21X000000001075A'
    ugs_bergermeer = '21W0000000000087', 'NL', '21X000000001120V'
    ugs_alkmaar = '21W000000000002J', 'NL', '21X0000000013732'
    gsp_historical_data_prior_to_4_feb_2014 = 'PRIOR_OSM_000001', 'PL', '53XPL000000OSMP5'
    ugs_wierzchowice = '21Z000000000381H', 'PL', '53XPL000000OSMP5'
    vgs_gim_kawerna_kosakowo = '21Z000000000383D', 'PL', '53XPL000000OSMP5'
    vgs_gim_sanok_brzeznica = '21Z000000000382F', 'PL', '53XPL000000OSMP5'
    ugs_carrico = '16ZAS01--------8', 'PT', '21X0000000013627'
    ugs_targu_mures = '21Z000000000309P', 'RO', '21X000000001300T'
    ugs_balaceanca = '21Z0000000003111', 'RO', '21X-DEPOGAZ-AGSI'
    ugs_bilciuresti = '21Z000000000313Y', 'RO', '21X-DEPOGAZ-AGSI'
    ugs_cetatea_de_balta = '21Z000000000316S', 'RO', '21X-DEPOGAZ-AGSI'
    ugs_ghercesti = '21Z000000000315U', 'RO', '21X-DEPOGAZ-AGSI'
    ugs_sarmasel = '21Z000000000314W', 'RO', '21X-DEPOGAZ-AGSI'
    ugs_urziceni = '21Z0000000003103', 'RO', '21X-DEPOGAZ-AGSI'
    ugs_lab_incl_gajary_baden = '21W000000000088K', 'SK', '42X-NAFTA-SK---U'
    ugs_lab_iv_pozagas = '21W000000000047Y', 'SK', '42X-POZAGAS-SK-V'
    vgs_enagas_serrablo = '21W000000000032A', 'ES', '21X0000000013368'
    ugs_skallen = '21W0000000000435', 'SE', '21X-SE-A-A0A0A-F'
    ugs_rough = '21W000000000094P', 'GB', '21X000000001022V'
    ugs_holehouse_farm_storage = '21Z000000000227R', 'GB', '23X-EDFE-------W'
    ugs_humbly_grove = '55WHUMBLY1GROVER', 'GB', '55XHUMBLYGROVE1H'
    ugs_hatfield_moors_storage = '21Z000000000229N', 'GB', '23XSCOTTISHPOWEF'
    ugs_aldbrough_i = '55WALDBOROUGH00H', 'GB', '23X--140207-SSE9'
    ugs_atwick = '55WATWICK-SSE00J', 'GB', '23X--140207-SSE9'
    ugs_stublach = '21W000000000101H', 'GB', '48XSTORENGYUK01P'
    ugs_holford = '21W000000000112C', 'GB', '21X0000000013716'
