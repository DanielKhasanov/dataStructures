class TrieNode:
    def __init__(self):
        self.word = None
        self.children = {}
        
    def addWord(self, word, index=0):
        # Ending confirmation (equivalent of signifying a word or subword)
        if index == len(word):
            self.word = word
        # Traverse down letters
        elif word[index] in self.children:
            childNode = self.children[word[index]]
            childNode.addWord(word, index + 1)
        # Add new letter as children
        else:
            newNode = TrieNode()
            self.children[word[index]] = newNode
            newNode.addWord(word, index + 1)
    
    def isWord(self, word, index=0):
        if index == len(word):
            return self.word == word
        elif word[index] in self.children:
            childNode = self.children[word[index]]
            return childNode.isWord(word, index + 1)
        else:
            return False
    
    def getNode(self, prefix, index=0):
        if index == len(prefix):
            return self
        elif prefix[index] in self.children:
            childNode = self.children[prefix[index]]
            return childNode.getNode(prefix, index + 1)
        else:
            return None
        
    def getAllWords(self):
        words = []
        # Word is confirmed
        if self.word is not None:
            words.append(self.word)
        # Add more confirmed words in children and add to list
        for childNode in self.children.values():
            words.extend(childNode.getAllWords())
        return words
        
    def allWords(self, prefix, index=0):
        prefixNode = self.getNode(prefix,index=index)
        # Does not exist
        if prefixNode is None:
            return []
        # Find all related words starting at prefix
        else:
            return prefixNode.getAllWords()

        

trieRoot = TrieNode()
trieRoot.addWord("cat")
trieRoot.addWord("catheter")
trieRoot.addWord("catniss")
trieRoot.addWord("caturday")
trieRoot.addWord("caturday2")
trieRoot.allWords("catu")
