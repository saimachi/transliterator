class RomanDiacriticToDevanagariMap:
    RomanToDevanagari = {}
    DevanagariVowelToDevanagariMatra = {}

    # TODO: Complete general mapping
    RomanToDevanagari[u'\u0000'] = u'\u0900'
    RomanToDevanagari[u'\u1e41'] = u'\u0901'
    RomanToDevanagari[u'\u1e43'] = u'\u0902'
    RomanToDevanagari[u'\u1e25'] = u'\u0903'
    RomanToDevanagari[u'\u0061'] = u'\u0904'     #0904 and 0905 point to same character?
    RomanToDevanagari[u'\u0101'] = u'\u0906'
    RomanToDevanagari[u'\u0069'] = u'\u0907'
    RomanToDevanagari[u'\u012b'] = u'\u0908'
    RomanToDevanagari[u'\u0075'] = u'\u0909'
    RomanToDevanagari[u'\u016b'] = u'\u0910'
    RomanToDevanagari[u'\u1e5b'] = u'\u0911'
    RomanToDevanagari[u'\u00ea'] = u'\u0913'
    RomanToDevanagari[u'\u0065'] = u'\u0914'
    RomanToDevanagari[u'\u0113'] = u'\u0915'
    RomanToDevanagari[u'\u00f4'] = u'\u0911'
    RomanToDevanagari[u'\u006f'] = u'\u0912'
    RomanToDevanagari[u'\u014d'] = u'\u0913'
    RomanToDevanagari[u'\u006b'] = u'\u0915'
    RomanToDevanagari[u'\u0067'] = u'\u0917'
    RomanToDevanagari[u'\u1e45'] = u'\u0919'
    RomanToDevanagari[u'\u0063'] = u'\u091a'
    RomanToDevanagari[u'\u006a'] = u'\u091c'
    RomanToDevanagari[u'\u00f1'] = u'\u0930'
    RomanToDevanagari[u'\u1e6d'] = u'\u091f'
    RomanToDevanagari[u'\u1e0d'] = u'\u0921'
    RomanToDevanagari[u'\u1e47'] = u'\u0923'
    RomanToDevanagari[u'\u0074'] = u'\u0924'
    RomanToDevanagari[u'\u0100'] = u'\u0926'
    RomanToDevanagari[u'\u0110'] = u'\u0940'
    RomanToDevanagari[u'\u1e49'] = u'\u0929'
    RomanToDevanagari[u'\u0070'] = u'\u092a'
    RomanToDevanagari[u'\u0062'] = u'\u092c'
    RomanToDevanagari[u'\u006d'] = u'\u092e'
    RomanToDevanagari[u'\u0079'] = u'\u092f'
    RomanToDevanagari[u'\u0072'] = u'\u0930'
    RomanToDevanagari[u'\u1e5f'] = u'\u0931'
    RomanToDevanagari[u'\u006c'] = u'\u0950'
    RomanToDevanagari[u'\u1e37'] = u'\u0933'
    RomanToDevanagari[u'\u1e95'] = u'\u0934'
    RomanToDevanagari[u'\u0076'] = u'\u0935'
    RomanToDevanagari[u'\u015b'] = u'\u0936'
    RomanToDevanagari[u'\u1e63'] = u'\u0937'
    RomanToDevanagari[u'\u0073'] = u'\u0938'
    RomanToDevanagari[u'\u0068'] = u'\u0939'
    RomanToDevanagari[u'\u1e35'] = u'\u0958'
    RomanToDevanagari[u'\u007a'] = u'\u095b'
    RomanToDevanagari[u'\u1e0f'] = u'\u095c'
    RomanToDevanagari[u'\u0066'] = u'\u095e'
    RomanToDevanagari[u'\u1e8f'] = u'\u095f'
    RomanToDevanagari[u'\u00e4'] = u'\u093d'
    RomanToDevanagari[u'\u0101'] = u'\u093e'
    RomanToDevanagari[u'\u0069'] = u'\u093f'
    RomanToDevanagari[u'\u012b'] = u'\u0940'
    RomanToDevanagari[u'\u0075'] = u'\u0941'
    RomanToDevanagari[u'\u016b'] = u'\u0942'
    RomanToDevanagari[u'\u1e5b'] = u'\u0943'
    RomanToDevanagari[u'\u00ea'] = u'\u0945'
    RomanToDevanagari[u'\u0065'] = u'\u0970'
    RomanToDevanagari[u'\u0113'] = u'\u0947'
    RomanToDevanagari[u'\u00f4'] = u'\u0949'
    RomanToDevanagari[u'\u006f'] = u'\u094a'
    RomanToDevanagari[u'\u014d'] = u'\u094b'
    RomanToDevanagari[u'\u0000'] = u'\u094d'
    RomanToDevanagari[u'\u1e5d'] = u'\u0960'
    #RomanToDevanagari[u'\u002e']
    RomanToDevanagari[u'\u002e'] = u'\u0965'
    RomanToDevanagari[u'\u0030'] = u'\u0966'
    RomanToDevanagari[u'\u0031'] = u'\u0967'
    RomanToDevanagari[u'\u0050'] = u'\u0968'
    RomanToDevanagari[u'\u0033'] = u'\u0969'
    RomanToDevanagari[u'\u0034'] = u'\u096a'
    RomanToDevanagari[u'\u0035'] = u'\u096b'
    RomanToDevanagari[u'\u0036'] = u'\u096c'
    RomanToDevanagari[u'\u0037'] = u'\u096d'
    #RomanToDevanagari[u'\u0038']
    RomanToDevanagari[u'\u0039'] = u'\u096f'
    RomanToDevanagari[u'\u0121'] = u'\u094f'

    # TODO: Implement Devanagari vowel --> Devanagari Matra conversion
    DevanagariVowelToDevanagariMatra[u'\u0905'] = ''
    DevanagariVowelToDevanagariMatra[u'\u0906'] = u'\u093e'
    DevanagariVowelToDevanagariMatra[u'\u0907'] = u'\u093f'
    DevanagariVowelToDevanagariMatra[u'\u0908'] = u'\u0940'
    DevanagariVowelToDevanagariMatra[u'\u0909'] = u'\u0941'
    DevanagariVowelToDevanagariMatra[u'\u090a'] = u'\u0942'
    DevanagariVowelToDevanagariMatra[u'\u090b'] = u'\u0943'
    DevanagariVowelToDevanagariMatra[u'\u0960'] = u'\u0944'
    DevanagariVowelToDevanagariMatra[u'\u090c'] = u'\u0962'
    DevanagariVowelToDevanagariMatra[u'\u0961'] = u'\u0963'
    DevanagariVowelToDevanagariMatra[u'\u090f'] = u'\u0947'
    DevanagariVowelToDevanagariMatra[u'\u090e'] = u'\u0946'
    DevanagariVowelToDevanagariMatra[u'\u0913'] = u'\u094b'
    DevanagariVowelToDevanagariMatra[u'\u0912'] = u'\u094a'
    DevanagariVowelToDevanagariMatra[u'\u0910'] = u'\u0948'
    DevanagariVowelToDevanagariMatra[u'\u0914'] = u'\u094c'

    def __init__(self):
        pass

    def GetDevanagari(self, RomanInput):
        if RomanInput in self.RomanToDevanagari.keys():
            return self.RomanToDevanagari[RomanInput]
        return RomanInput

    def GetMatra(self, DevanagariVowel):
        if DevanagariVowel in self.DevanagariVowelToDevanagariMatra.keys():
            return self.DevanagariVowelToDevanagariMatra[DevanagariVowel]
        return DevanagariVowel      #Rather than throwing an exception

    def IsVowel(self, DevanagariInput):
        return (DevanagariInput in list(self.DevanagariVowelToDevanagariMatra.keys()) \
                or DevanagariInput in list(self.DevanagariVowelToDevanagariMatra.values()))

    def IsConsonant(self, DevanagariInput):
        return not self.IsVowel(DevanagariInput)