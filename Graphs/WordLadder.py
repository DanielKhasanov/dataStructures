

def findWordLadderDist(startWord, endWord, wordBank):
    distance, curr, visited, lookup  = 0, [startWord], set([startWord]), set(wordBank)

    while curr:
        next_queue = []
        for word in curr:
            print("Processing: ", word)
            if word == endWord:
                return distance + 1
            for i in range(len(word)):
                for letter in 'qwertyuiopasdfghjklzxcvbnm':
                    candidate = word[:i] + letter + word[i+1:]
                    if candidate not in visited and candidate in lookup:
                        print("New Candidate: ", candidate)
                        next_queue.append(candidate)
                        visited.add(candidate)
        distance += 1
        curr = next_queue
        print(curr)

    return 0


print (findWordLadderDist("hit", "cog", set(["hot", "dot", "dog", "lot", "log", "cog"])))
