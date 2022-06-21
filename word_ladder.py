def strcomp (word1, word2):
    i = 0
    count =0
    for x in word1:
        if i < len (word2) and x == word2[i]: count+=1
        i+=1
    return (count)
def mostSimilar(list, word):
    count_list = []
    for elems in list:
        count_list.append(strcomp (elems, word))
    index = count_list.index(max(count_list))
    return list[index]
def ladderLength(beginWord, endWord, wordList):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
        'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'k', 'r', 's', 't', 'u', 'v', 'w',
        'x', 'y', 'z']
    if endWord not in wordList: return 0
    flag =0
    bw =[]
    found = []
    index = 0
    for x in beginWord: bw.append(x)
    while index<len(beginWord): 
        #print(wordList)
        flag =0
        for l in letters:
            x  = bw[index]
            if bw[index] != l: bw[index] = l
            else: continue
            s = ''.join(bw)
            #print(s)
            if s in wordList:
                #print('***************************')
                #print(bw)
                found.append(s)
                flag = 1
                #index=-1
                #break
            bw[index] = x
        if (found):
            print('found: ', found)
            #print('iahuu')
            s = mostSimilar(found, endWord)
            print('most similar: ', s)
            wordList.remove(s)
            bw.clear()
            for y in s: bw.append(y)
            print('new :', bw)
            index = -1
        found.clear()
        if ''.join(bw) == endWord: break
        index+=1
        print(bw)
    return 
    
print('Word Ladder')
ladderLength("hit", "cog", ["hot","dot", "dog","lot","log","cog"])
#print(mostSimilar(["hot","dot","dog","lot","log"], 'cog'))
