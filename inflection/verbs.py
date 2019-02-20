"""Verb inflection"""

from enum import Enum, auto
from typing import List

from cltk.phonology.old_norse.transcription import measure_old_norse_syllable, DIPHTHONGS_IPA, DIPHTHONGS_IPA_class, \
    IPA_class, old_norse_rules

from cltk.phonology.syllabify import Syllabifier, Syllable
from cltk.corpus.old_norse.syllabifier import invalid_onsets, VOWELS, CONSONANTS, LONG_VOWELS, BACK_TO_FRONT_VOWELS
from cltk.inflection.utils import Number
from cltk.phonology.utils import Length, Transcriber

from inflection.phonemic_rules import apply_i_umlaut, apply_u_umlaut

__author__ = ["Clément Besnier <clemsciences@aol.com>", ]

s = Syllabifier(language="old_norse", break_geminants=True)
s.set_invalid_onsets(invalid_onsets)

s_ipa = Syllabifier(language="old_norse_ipa", break_geminants=True)
s_ipa.set_invalid_onsets(invalid_onsets)

transcriber = Transcriber(DIPHTHONGS_IPA, DIPHTHONGS_IPA_class, IPA_class, old_norse_rules)


class Person(Enum):
    first = auto()
    second = auto()
    third = auto()


class Mood(Enum):
    infinitive = auto()
    imperative = auto()
    indicative = auto()
    subjunctive = auto()
    supine = auto()
    present_participle = auto()
    past_participle = auto()


class Voice(Enum):
    active = auto()
    middle = auto()


class Tense(Enum):
    present = auto()
    past = auto()


class VerbCategory(Enum):
    strong = auto()
    weak = auto()
    preteritopresent = auto()


class OldNorseVerb:

    def __init__(self):
        self.name = ""
        self.category = None
        self.forms = {}

    def set_canonic_forms(self, canonic_forms: List[str]):
        """

        :param canonic_forms: 3-tuple or 5-tuple
        :return:
        """
        pass

    def get_form(self, *args: List[str]):
        """

        :param args:
        :return:
        """
        for i in args:
            if isinstance(i, Person):
                pass
            elif isinstance(i, Tense):
                pass

            elif isinstance(i, Number):
                pass

            elif isinstance(i, Mood):
                pass

            elif isinstance(i, Voice):
                pass

        return self.forms

    def _present_active_weak(self):
        print()
        l = []

        pass

    def _past_active_weak(self):
        pass

    def _present_active_strong(self):
        pass

    def _past_active_strong(self):
        pass

    def _present_mediopassive_weak(self):
        pass

    def _past_mediopassive_weak(self):
        pass

    def _present_mediopassive_strong(self):
        pass

    def _past_mediopassive_strong(self):
        pass

    def _present_active_weak_subjunctive(self):
        pass

    def _past_active_weak_subjunctive(self):
        pass

    def _present_active_strong_subjunctive(self):
        pass

    def _past_active_strong_subjunctive(self):
        pass

    def _present_mediopassive_weak_subjunctive(self):
        pass

    def _past_mediopassive_weak_subjunctive(self):
        pass

    def _present_mediopassive_strong_subjunctive(self):
        pass

    def _past_mediopassive_strong_subjunctive(self):
        pass


class StrongOldNorseVerb(OldNorseVerb):
    def __init__(self):
        super().__init__()

        self.sng = ""
        self.s_sng = None
        self.sp_sng = None

        self.sfg3et = ""
        self.s_sfg3et = None
        self.sp_sfg3et = None

        self.stgken = ""
        self.s_stgken = None
        self.sp_stgken = None

        self.subclass = 0
        self.syllabified = []

    def set_canonic_forms(self, canonic_forms: List[str]):
        """

        Strong verbs
        I
        >>> verb = OldNorseVerb()
        >>> verb.set_canonic_forms(["", "", "", "", ""])

        II
        >>> verb = OldNorseVerb()
        >>> verb.set_canonic_forms(["", "", "", "", ""])

        III
        >>> verb = OldNorseVerb()
        >>> verb.set_canonic_forms(["", "", "", "", ""])

        IV
        >>> verb = OldNorseVerb()
        >>> verb.set_canonic_forms(["", "", "", "", ""])

        V
        >>> verb = OldNorseVerb()
        >>> verb.set_canonic_forms(["", "", "", "", ""])

        VI
        >>> verb = OldNorseVerb()
        >>> verb.set_canonic_forms(["", "", "", "", ""])

        VII
        >>> verb = OldNorseVerb()
        >>> verb.set_canonic_forms(["", "", "", "", ""])

        :param canonic_forms:
        :return:
        """
        if len(canonic_forms) == 5:
            sng, sfg3en, sfg3et, sfg3ft, stgken = canonic_forms
            self.category = VerbCategory.strong
            self.name = sng
        else:
            raise ValueError("Not a correct argument")

    def _present_active_strong(self):
        pass

    def _past_active_strong(self):
        pass

    def _present_mediopassive_strong(self):
        pass

    def _past_mediopassive_strong(self):
        pass

    def _present_active_strong_subjunctive(self):
        if self.sng == "vera":
            print("sé")
            print("sér")
            print("sé")
            print("sém")
            print("séð")
            print("sé")
        elif self.sng == "sjá":
            print("sjá")
            print("sér")
            print("sé")
            print("sém")
            print("séð")
            print("sé")
        else:
            subjunctive_root = self.sng[:-1] if self.sng[-1] == "a" else self.sng

            print(subjunctive_root + "a")
            subjunctive_root = subjunctive_root[:-1] if subjunctive_root[-1] == "j" else subjunctive_root
            print(subjunctive_root + "ir")
            print(subjunctive_root + "i")
            print(subjunctive_root + "im")
            print(subjunctive_root + "ið")
            print(subjunctive_root + "i")

    def _past_active_strong_subjunctive(self):
        pass

    def _present_mediopassive_strong_subjunctive(self):
        pass

    def _past_mediopassive_strong_subjunctive(self):
        pass


class WeakOldNorseVerb(OldNorseVerb):

    def __init__(self):
        super().__init__()

        self.sng = ""
        self.s_sng = None
        self.sp_sng = None

        self.sfg3et = ""
        self.s_sfg3et = None
        self.sp_sfg3et = None

        self.stgken = ""
        self.s_stgken = None
        self.sp_stgken = None

        self.subclass = 0
        self.syllabified = []

    def set_canonic_forms(self, canonic_forms: List[str]):
        """


        Weak verbs
        I
        >>> verb = WeakOldNorseVerb()
        >>> verb.set_canonic_forms(["kalla", "kallaði", "kallaðinn"])
        >>> verb.subclass
        1

        II
        >>> verb = WeakOldNorseVerb()
        >>> verb.set_canonic_forms(["mæla", "mælti", "mæltr"])
        >>> verb.subclass
        2

        III
        >>> verb = WeakOldNorseVerb()
        >>> verb.set_canonic_forms(["telja", "taldi", "talinn"])
        >>> verb.subclass
        3

        IV
        >>> verb = WeakOldNorseVerb()
        >>> verb.set_canonic_forms(["vaka", "vakta", "vakat"])
        >>> verb.subclass
        4

        :param canonic_forms: (infinitive, third person singular past indicative,
        past participle masculine singular nominative)
        :return:
        """
        if len(canonic_forms) == 3:
            self.sng, self.sfg3et, self.stgken = canonic_forms
            self.category = VerbCategory.weak
            self.name = self.sng

            self.s_sng = s.syllabify_ssp(self.sng)
            self.sp_sng = s_ipa.syllabify_phonemes(transcriber.text_to_phonemes(self.sng))

            self.s_sfg3et = s.syllabify_ssp(self.sfg3et)
            self.sp_sfg3et = s_ipa.syllabify_phonemes(transcriber.text_to_phonemes(self.sfg3et))

            self.s_stgken = s.syllabify_ssp(self.stgken)
            self.sp_stgken = s_ipa.syllabify_phonemes(transcriber.text_to_phonemes(self.stgken))
            self.classify()
        else:
            raise ValueError("Not a correct argument")

    def _present_active_weak(self):
        """
        Weak verbs
        I
        >>> verb = WeakOldNorseVerb()
        >>> verb.set_canonic_forms(["kalla", "kallaði", "kallaðinn"])
        >>> verb._present_active_weak()
        kalla
        kallar
        kallar
        köllum
        kallið
        kalla

        II
        >>> verb = WeakOldNorseVerb()
        >>> verb.set_canonic_forms(["mæla", "mælti", "mæltr"])
        >>> verb._present_active_weak()
        mæli
        mælir
        mælir
        mælum
        mælið
        mæla

        III
        >>> verb = WeakOldNorseVerb()
        >>> verb.set_canonic_forms(["telja", "taldi", "talinn"])
        >>> verb._present_active_weak()
        tel
        telr
        telr
        teljum
        telið
        telja

        IV
        >>> verb = WeakOldNorseVerb()
        >>> verb.set_canonic_forms(["vaka", "vakta", "vakat"])
        >>> verb._present_active_weak()
        vaki
        vakir
        vakir
        vökum
        vakið
        vaka

        :return:
        """
        stem_ending_by_j = self.sng[-1] == "a" and self.sng[-2] == "j"
        stem_ending_by_v = self.sng[-1] == "a" and self.sng[-2] == "v"
        stem = self.sng[:-1] if self.sng[-1] == "a" else self.sng
        if stem_ending_by_j or stem_ending_by_v:
            stem = stem[:-1]

        if self.subclass == 1:
            if stem_ending_by_v:
                print(stem+"va")
                print(stem + "r")
                print(stem + "r")
                print(apply_u_umlaut(stem) + "um")  # apply u umlaut
                print(stem + "við")
                print(stem+"va")
            elif stem_ending_by_j:
                print(stem+"ja")
                print(stem + "r")
                print(stem + "r")
                print(apply_u_umlaut(stem) + "jum")  # apply u umlaut
                print(stem + "ið")
                print(stem+"ja")
            else:
                print(stem+"a")
                print(stem + "ar")
                print(stem + "ar")
                print(apply_u_umlaut(stem) + "um")  # apply u umlaut
                print(stem + "ið")
                print(self.sng)

        elif self.subclass == 2:
            if stem_ending_by_v:
                print(stem + "vi")
                print(stem + "vir")
                print(stem + "vir")
                print(apply_u_umlaut(stem) + "um")  # apply u umlaut
                print(stem + "við")
                print(self.sng)

            elif stem_ending_by_j:
                print(stem + "i")
                print(stem + "ir")
                print(stem + "ir")
                print(apply_u_umlaut(stem) + "jum")  # apply u umlaut
                print(stem + "ið")
                print(self.sng)

            else:
                print(stem + "i")
                print(stem + "ir")
                print(stem + "ir")
                print(apply_u_umlaut(stem) + "um")  # apply u umlaut
                print(stem + "ið")
                print(self.sng)

        elif self.subclass == 3:
            if stem_ending_by_v:
                print(stem)
                print(stem + "r")
                print(stem + "r")
                print(apply_u_umlaut(stem) + "um")  # apply u umlaut
                print(stem + "við")
                print(self.sng)

            elif stem_ending_by_j:
                print(stem)
                print(stem + "r")
                print(stem + "r")
                print(apply_u_umlaut(stem) + "jum")  # apply u umlaut
                print(stem + "ið")
                print(self.sng)

            else:
                print(stem)
                print(stem + "r")
                print(stem + "r")
                print(apply_u_umlaut(stem) + "um")  # apply u umlaut
                print(stem + "ið")
                print(self.sng)

        elif self.subclass == 4:

            if stem_ending_by_v:
                print(stem + "vi")
                print(stem + "vir")
                print(stem + "vir")
                print(apply_u_umlaut(stem) + "um")  # apply u umlaut
                print(stem + "við")
                print(self.sng)

            elif stem_ending_by_j:
                print(stem + "i")
                print(stem + "ir")
                print(stem + "ir")
                print(apply_u_umlaut(stem) + "jum")  # apply u umlaut
                print(stem + "ið")
                print(self.sng)

            else:
                print(stem + "i")
                print(stem + "ir")
                print(stem + "ir")
                print(apply_u_umlaut(stem) + "um")  # apply u umlaut
                print(stem + "ið")
                print(self.sng)

    def _past_active_weak(self):
        pass

    def _present_mediopassive_weak(self):
        pass

    def _past_mediopassive_weak(self):
        pass

    def _present_active_weak_subjunctive(self):
        """
        Weak verbs
        I
        >>> verb = WeakOldNorseVerb()
        >>> verb.set_canonic_forms(["kalla", "kallaði", "kallaðinn"])
        >>> verb._present_active_weak_subjunctive()
        kalla
        kallir
        kalli
        kallim
        kallið
        kalli


        II
        >>> verb = WeakOldNorseVerb()
        >>> verb.set_canonic_forms(["mæla", "mælti", "mæltr"])
        >>> verb._present_active_weak_subjunctive()
        mæla
        mælir
        mæli
        mælim
        mælið
        mæli

        III
        >>> verb = WeakOldNorseVerb()
        >>> verb.set_canonic_forms(["telja", "taldi", "talinn"])
        >>> verb._present_active_weak_subjunctive()
        telja
        telir
        teli
        telim
        telið
        teli

        IV
        >>> verb = WeakOldNorseVerb()
        >>> verb.set_canonic_forms(["vaka", "vakta", "vakat"])
        >>> verb._present_active_weak_subjunctive()
        vaka
        vakir
        vaki
        vakim
        vakið
        vaki


        :return:
        """
        subjunctive_root = self.sng[:-1] if self.sng[-1] == "a" else self.sng

        print(subjunctive_root+"a")
        subjunctive_root = subjunctive_root[:-1] if subjunctive_root[-1] == "j" else subjunctive_root
        print(subjunctive_root+"ir")
        print(subjunctive_root+"i")
        print(subjunctive_root+"im")
        print(subjunctive_root+"ið")
        print(subjunctive_root+"i")

    def _past_active_weak_subjunctive(self):
        """
        Weak verbs
        I
        >>> verb = WeakOldNorseVerb()
        >>> verb.set_canonic_forms(["kalla", "kallaði", "kallaðinn"])
        >>> verb._past_active_weak_subjunctive()
        kallaða
        kallaðir
        kallaði
        kallaðim
        kallaðið
        kallaði

        II
        >>> verb = WeakOldNorseVerb()
        >>> verb.set_canonic_forms(["mæla", "mælti", "mæltr"])
        >>> verb._past_active_weak_subjunctive()
        mælta
        mæltir
        mælti
        mæltim
        mæltið
        mælti

        III
        >>> verb = WeakOldNorseVerb()
        >>> verb.set_canonic_forms(["telja", "taldi", "talinn"])
        >>> verb._past_active_weak_subjunctive()
        telda
        teldir
        teldi
        teldim
        teldið
        teldi


        IV
        >>> verb = WeakOldNorseVerb()
        >>> verb.set_canonic_forms(["vaka", "vakti", "vakat"])
        >>> verb._past_active_weak_subjunctive()
        vekta
        vektir
        vekti
        vektim
        vektið
        vekti


        :return:
        """
        subjunctive_root = self.sfg3et[:-1] if self.sng[-1] == "a" else self.sfg3et

        if self.subclass in [1, 2]:
            print(subjunctive_root + "a")
            subjunctive_root = subjunctive_root[:-1] if subjunctive_root[-1] == "j" else subjunctive_root
            print(subjunctive_root + "ir")
            print(subjunctive_root + "i")
            print(subjunctive_root + "im")
            print(subjunctive_root + "ið")
            print(subjunctive_root + "i")

        elif self.subclass in [3, 4]:
            subjunctive_root = apply_i_umlaut(subjunctive_root)
            print(subjunctive_root + "a")
            subjunctive_root = subjunctive_root[:-1] if subjunctive_root[-1] == "j" else subjunctive_root
            print(subjunctive_root + "ir")
            print(subjunctive_root + "i")
            print(subjunctive_root + "im")
            print(subjunctive_root + "ið")
            print(subjunctive_root + "i")

    def _present_mediopassive_weak_subjunctive(self):
        pass

    def _past_mediopassive_weak_subjunctive(self):
        pass

    def classify(self):
        if self.sng in ["segja", "þegja"]:
            self.subclass = 4
        elif self.sng in ["vilja", "gera"]:
            self.subclass = 3
        elif self.sng in ["spá"]:
            self.subclass = 2
        elif self.sng and self.sfg3et and self.stgken:
            if self.sfg3et.endswith("aði"):
                self.subclass = 1

            elif not "".join(Syllable(self.s_sng[0], VOWELS, CONSONANTS).nucleus) in BACK_TO_FRONT_VOWELS.values():
                self.subclass = 4
            else:
                stem_length = measure_old_norse_syllable(self.sp_sng[0])
                if stem_length == Length.long or stem_length == Length.overlong:
                    self.subclass = 2
                elif stem_length == Length.short:
                    self.subclass = 3
                else:
                    self.subclass = 5


def add_t_ending_to_syllable(last_syllable):
    """

    >>> add_t_ending_to_syllable("batt")
    'bazt'
    >>> add_t_ending_to_syllable("gat")
    'gazt'
    >>> add_t_ending_to_syllable("varð")
    'vart'
    >>> add_t_ending_to_syllable("hélt")
    'hélt'
    >>> add_t_ending_to_syllable("réð")
    'rétt'
    >>> add_t_ending_to_syllable("laust")
    'laust'
    >>> add_t_ending_to_syllable("sá")
    'sátt'

    :param last_syllable:
    :return:
    """
    if len(last_syllable) >= 2:
        if last_syllable[-1] == 't':
            if last_syllable[-2] in VOWELS:
                # Apocope of r
                return last_syllable[:-1]+"zt"
            elif last_syllable[-2] == 't':
                return last_syllable[:-2]+"zt"
            elif last_syllable[-2] in ['r', 'l', 's']:
                return last_syllable
            else:
                return last_syllable + "t"
        elif last_syllable[-1] == 'ð':
            if last_syllable[-2] in ['r', 'l', 's']:
                return last_syllable[:-1] + "t"
            else:
                return last_syllable[:-1]+"tt"

        elif last_syllable[-1] == 'd':
            return last_syllable[:-1]+"t"
        elif last_syllable[-1] in LONG_VOWELS:
            return last_syllable + "tt"
        else:
            return last_syllable + "t"
    else:
        return last_syllable + "t"


def add_t_ending(stem: str) -> str:
    """

    >>> add_t_ending("batt")
    'bazt'
    >>> add_t_ending("gat")
    'gazt'
    >>> add_t_ending("varð")
    'vart'
    >>> add_t_ending("hélt")
    'hélt'
    >>> add_t_ending("réð")
    'rétt'
    >>> add_t_ending("laust")
    'laust'
    >>> add_t_ending("sá")
    'sátt'

    :param stem:
    :return:
    """
    s_stem = s.syllabify_ssp(stem.lower())
    last_syllable = Syllable(s_stem[-1], VOWELS, CONSONANTS)
    return "".join(s_stem[:-1]) + add_t_ending_to_syllable(last_syllable.text)
