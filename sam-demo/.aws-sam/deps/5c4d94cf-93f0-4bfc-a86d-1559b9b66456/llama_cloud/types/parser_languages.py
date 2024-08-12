# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ParserLanguages(str, enum.Enum):
    """
    Enum for representing the languages supported by the parser
    """

    AF = "af"
    AZ = "az"
    BS = "bs"
    CS = "cs"
    CY = "cy"
    DA = "da"
    DE = "de"
    EN = "en"
    ES = "es"
    ET = "et"
    FR = "fr"
    GA = "ga"
    HR = "hr"
    HU = "hu"
    ID = "id"
    IS = "is"
    IT = "it"
    KU = "ku"
    LA = "la"
    LT = "lt"
    LV = "lv"
    MI = "mi"
    MS = "ms"
    MT = "mt"
    NL = "nl"
    NO = "no"
    OC = "oc"
    PI = "pi"
    PL = "pl"
    PT = "pt"
    RO = "ro"
    RS_LATIN = "rs_latin"
    SK = "sk"
    SL = "sl"
    SQ = "sq"
    SV = "sv"
    SW = "sw"
    TL = "tl"
    TR = "tr"
    UZ = "uz"
    VI = "vi"
    AR = "ar"
    FA = "fa"
    UG = "ug"
    UR = "ur"
    BN = "bn"
    AS = "as"
    MNI = "mni"
    RU = "ru"
    RS_CYRILLIC = "rs_cyrillic"
    BE = "be"
    BG = "bg"
    UK = "uk"
    MN = "mn"
    ABQ = "abq"
    ADY = "ady"
    KBD = "kbd"
    AVA = "ava"
    DAR = "dar"
    INH = "inh"
    CHE = "che"
    LBE = "lbe"
    LEZ = "lez"
    TAB = "tab"
    TJK = "tjk"
    HI = "hi"
    MR = "mr"
    NE = "ne"
    BH = "bh"
    MAI = "mai"
    ANG = "ang"
    BHO = "bho"
    MAH = "mah"
    SCK = "sck"
    NEW = "new"
    GOM = "gom"
    SA = "sa"
    BGC = "bgc"
    TH = "th"
    CH_SIM = "ch_sim"
    CH_TRA = "ch_tra"
    JA = "ja"
    KO = "ko"
    TA = "ta"
    TE = "te"
    KN = "kn"

    def visit(
        self,
        af: typing.Callable[[], T_Result],
        az: typing.Callable[[], T_Result],
        bs: typing.Callable[[], T_Result],
        cs: typing.Callable[[], T_Result],
        cy: typing.Callable[[], T_Result],
        da: typing.Callable[[], T_Result],
        de: typing.Callable[[], T_Result],
        en: typing.Callable[[], T_Result],
        es: typing.Callable[[], T_Result],
        et: typing.Callable[[], T_Result],
        fr: typing.Callable[[], T_Result],
        ga: typing.Callable[[], T_Result],
        hr: typing.Callable[[], T_Result],
        hu: typing.Callable[[], T_Result],
        id: typing.Callable[[], T_Result],
        is_: typing.Callable[[], T_Result],
        it: typing.Callable[[], T_Result],
        ku: typing.Callable[[], T_Result],
        la: typing.Callable[[], T_Result],
        lt: typing.Callable[[], T_Result],
        lv: typing.Callable[[], T_Result],
        mi: typing.Callable[[], T_Result],
        ms: typing.Callable[[], T_Result],
        mt: typing.Callable[[], T_Result],
        nl: typing.Callable[[], T_Result],
        no: typing.Callable[[], T_Result],
        oc: typing.Callable[[], T_Result],
        pi: typing.Callable[[], T_Result],
        pl: typing.Callable[[], T_Result],
        pt: typing.Callable[[], T_Result],
        ro: typing.Callable[[], T_Result],
        rs_latin: typing.Callable[[], T_Result],
        sk: typing.Callable[[], T_Result],
        sl: typing.Callable[[], T_Result],
        sq: typing.Callable[[], T_Result],
        sv: typing.Callable[[], T_Result],
        sw: typing.Callable[[], T_Result],
        tl: typing.Callable[[], T_Result],
        tr: typing.Callable[[], T_Result],
        uz: typing.Callable[[], T_Result],
        vi: typing.Callable[[], T_Result],
        ar: typing.Callable[[], T_Result],
        fa: typing.Callable[[], T_Result],
        ug: typing.Callable[[], T_Result],
        ur: typing.Callable[[], T_Result],
        bn: typing.Callable[[], T_Result],
        as_: typing.Callable[[], T_Result],
        mni: typing.Callable[[], T_Result],
        ru: typing.Callable[[], T_Result],
        rs_cyrillic: typing.Callable[[], T_Result],
        be: typing.Callable[[], T_Result],
        bg: typing.Callable[[], T_Result],
        uk: typing.Callable[[], T_Result],
        mn: typing.Callable[[], T_Result],
        abq: typing.Callable[[], T_Result],
        ady: typing.Callable[[], T_Result],
        kbd: typing.Callable[[], T_Result],
        ava: typing.Callable[[], T_Result],
        dar: typing.Callable[[], T_Result],
        inh: typing.Callable[[], T_Result],
        che: typing.Callable[[], T_Result],
        lbe: typing.Callable[[], T_Result],
        lez: typing.Callable[[], T_Result],
        tab: typing.Callable[[], T_Result],
        tjk: typing.Callable[[], T_Result],
        hi: typing.Callable[[], T_Result],
        mr: typing.Callable[[], T_Result],
        ne: typing.Callable[[], T_Result],
        bh: typing.Callable[[], T_Result],
        mai: typing.Callable[[], T_Result],
        ang: typing.Callable[[], T_Result],
        bho: typing.Callable[[], T_Result],
        mah: typing.Callable[[], T_Result],
        sck: typing.Callable[[], T_Result],
        new: typing.Callable[[], T_Result],
        gom: typing.Callable[[], T_Result],
        sa: typing.Callable[[], T_Result],
        bgc: typing.Callable[[], T_Result],
        th: typing.Callable[[], T_Result],
        ch_sim: typing.Callable[[], T_Result],
        ch_tra: typing.Callable[[], T_Result],
        ja: typing.Callable[[], T_Result],
        ko: typing.Callable[[], T_Result],
        ta: typing.Callable[[], T_Result],
        te: typing.Callable[[], T_Result],
        kn: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ParserLanguages.AF:
            return af()
        if self is ParserLanguages.AZ:
            return az()
        if self is ParserLanguages.BS:
            return bs()
        if self is ParserLanguages.CS:
            return cs()
        if self is ParserLanguages.CY:
            return cy()
        if self is ParserLanguages.DA:
            return da()
        if self is ParserLanguages.DE:
            return de()
        if self is ParserLanguages.EN:
            return en()
        if self is ParserLanguages.ES:
            return es()
        if self is ParserLanguages.ET:
            return et()
        if self is ParserLanguages.FR:
            return fr()
        if self is ParserLanguages.GA:
            return ga()
        if self is ParserLanguages.HR:
            return hr()
        if self is ParserLanguages.HU:
            return hu()
        if self is ParserLanguages.ID:
            return id()
        if self is ParserLanguages.IS:
            return is_()
        if self is ParserLanguages.IT:
            return it()
        if self is ParserLanguages.KU:
            return ku()
        if self is ParserLanguages.LA:
            return la()
        if self is ParserLanguages.LT:
            return lt()
        if self is ParserLanguages.LV:
            return lv()
        if self is ParserLanguages.MI:
            return mi()
        if self is ParserLanguages.MS:
            return ms()
        if self is ParserLanguages.MT:
            return mt()
        if self is ParserLanguages.NL:
            return nl()
        if self is ParserLanguages.NO:
            return no()
        if self is ParserLanguages.OC:
            return oc()
        if self is ParserLanguages.PI:
            return pi()
        if self is ParserLanguages.PL:
            return pl()
        if self is ParserLanguages.PT:
            return pt()
        if self is ParserLanguages.RO:
            return ro()
        if self is ParserLanguages.RS_LATIN:
            return rs_latin()
        if self is ParserLanguages.SK:
            return sk()
        if self is ParserLanguages.SL:
            return sl()
        if self is ParserLanguages.SQ:
            return sq()
        if self is ParserLanguages.SV:
            return sv()
        if self is ParserLanguages.SW:
            return sw()
        if self is ParserLanguages.TL:
            return tl()
        if self is ParserLanguages.TR:
            return tr()
        if self is ParserLanguages.UZ:
            return uz()
        if self is ParserLanguages.VI:
            return vi()
        if self is ParserLanguages.AR:
            return ar()
        if self is ParserLanguages.FA:
            return fa()
        if self is ParserLanguages.UG:
            return ug()
        if self is ParserLanguages.UR:
            return ur()
        if self is ParserLanguages.BN:
            return bn()
        if self is ParserLanguages.AS:
            return as_()
        if self is ParserLanguages.MNI:
            return mni()
        if self is ParserLanguages.RU:
            return ru()
        if self is ParserLanguages.RS_CYRILLIC:
            return rs_cyrillic()
        if self is ParserLanguages.BE:
            return be()
        if self is ParserLanguages.BG:
            return bg()
        if self is ParserLanguages.UK:
            return uk()
        if self is ParserLanguages.MN:
            return mn()
        if self is ParserLanguages.ABQ:
            return abq()
        if self is ParserLanguages.ADY:
            return ady()
        if self is ParserLanguages.KBD:
            return kbd()
        if self is ParserLanguages.AVA:
            return ava()
        if self is ParserLanguages.DAR:
            return dar()
        if self is ParserLanguages.INH:
            return inh()
        if self is ParserLanguages.CHE:
            return che()
        if self is ParserLanguages.LBE:
            return lbe()
        if self is ParserLanguages.LEZ:
            return lez()
        if self is ParserLanguages.TAB:
            return tab()
        if self is ParserLanguages.TJK:
            return tjk()
        if self is ParserLanguages.HI:
            return hi()
        if self is ParserLanguages.MR:
            return mr()
        if self is ParserLanguages.NE:
            return ne()
        if self is ParserLanguages.BH:
            return bh()
        if self is ParserLanguages.MAI:
            return mai()
        if self is ParserLanguages.ANG:
            return ang()
        if self is ParserLanguages.BHO:
            return bho()
        if self is ParserLanguages.MAH:
            return mah()
        if self is ParserLanguages.SCK:
            return sck()
        if self is ParserLanguages.NEW:
            return new()
        if self is ParserLanguages.GOM:
            return gom()
        if self is ParserLanguages.SA:
            return sa()
        if self is ParserLanguages.BGC:
            return bgc()
        if self is ParserLanguages.TH:
            return th()
        if self is ParserLanguages.CH_SIM:
            return ch_sim()
        if self is ParserLanguages.CH_TRA:
            return ch_tra()
        if self is ParserLanguages.JA:
            return ja()
        if self is ParserLanguages.KO:
            return ko()
        if self is ParserLanguages.TA:
            return ta()
        if self is ParserLanguages.TE:
            return te()
        if self is ParserLanguages.KN:
            return kn()
