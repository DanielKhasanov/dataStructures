class tokenizedEdgeNGram:
    def __init__(self):
        self.substringsDict = {}

    def edgeNGramTokenizer(self, word):
        # Create all sub words
        return [word[0:idx] for idx in range(1, len(word) + 1)]

    def add(self, word):
        for token in self.edgeNGramTokenizer(word):
            # Either initialize new entry
            self.substringsDict[token] = self.substringsDict.get(token, 0) + 1

    def find(self, word):
        return self.substringsDict.get(word, 0)

    def __str__(self):
        entries = []
        for k,v in self.substringsDict.items():
            entries.append(" : ".join([k,str(v)]) + " \n" )
        return " ".join(entries)


eGram = tokenizedEdgeNGram()
testList = "Johnny: You’re lying, I never hit you. You are tearing me apart, Lisa!".split(" ")
for word in testList:
    eGram.add(word)

print(eGram)

