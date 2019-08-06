from RomanToDevanagariMap import RomanDiacriticToDevanagariMap

class RomanDiacriticToDevanagariConverter:
    def __init__(self):
        self._mapping = RomanDiacriticToDevanagariMap()

    def DirectConversion(self, RomanInput):
        output = ''
        for character in RomanInput:
            output += self._mapping.GetDevanagari(character)
        return output

    def Refinement(self, DevanagariInput):
        output = ''
        DevanagariInput = DevanagariInput.split()
        DevanagariInput = [list(unit) for unit in DevanagariInput]
        for grouping in DevanagariInput:
            # Single character consonant needs Matra 
            if len(grouping) == 1:
                if self._mapping.IsConsonant(grouping):
                    output += str(grouping) + u'\u0902'
                else:
                    output += grouping
            elif len(grouping) == 2:
                if self._mapping.IsConsonant(grouping[0]) and \
                    self._mapping.IsVowel(grouping[1]):
                    output += grouping[0] + self._mapping.GetMatra(grouping[1])
            else:
                # Possibly recursive approach
                pass
        return output

    def Transliterate(self, RomanInput):
        return self.Refinement(self.DirectConversion(RomanInput))

if __name__ == "__main__":
    Converter = RomanDiacriticToDevanagariConverter()
    Converter.Transliterate('g')
