def possibilities (list, word):
    poss = []
    for elems in list:
        i=0
        sim = 0
        for char in elems:
            if char == word[i]: sim+=1
            if i < len(word): i+=1
        if sim == len(word) -1: poss.append(elems)
    return (poss)

def ladderLength(beginWord, endWord, wordList):
    if endWord not in wordList: return 0
    poss = []
    count =0
    poss = possibilities (wordList, beginWord)
    if endWord in poss: return 1
    for x in poss: wordList.remove(x)
    for elems in poss:
        possibilities(
    while endWord not in poss:
        for elems in poss: 
            poss.append(possibilities(wordList, elems))
            #wordList.remove(possibilities(wordList, elems))
            if elems == poss[-1]: break
        count+=1
    print(poss)
    return count
print('another attempt')
ladderLength("hit", "cog", ["hot","dot", "dog","lot","log","cog"])
#print(possibilities(["hot","dot", "dog","lot","log","cog"], "pot"))