def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    print('Calculating...')
    lsub = ''
    sub = ''
    if len(s) <2: lsub = s
    else:
        for x in s:
            if x in sub:
                if len(lsub)<len(sub): lsub = sub
                sub = sub[sub.find(x)+1:]
            sub +=x
    if len(sub)>len(lsub): 
        print('Substring: ', sub)
        return(len(sub))
    else:
        print('Substring: ', lsub)
        return len(lsub)
		
inp = input('Please enter a string to be assessed: ')
print('Longest substring = ', lengthOfLongestSubstring(inp))