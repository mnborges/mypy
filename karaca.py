print("The Karaca's Encryption Algorithm")
def karaka(txt):
    v = {'a':'0','e':'1','i':'2','o':'2','u':'3'}
    #split entry into separate words
    words = txt.lower().split()
    result = ''
    for pieces in words:
        revpiece= ''
        count =len(pieces)-1
        #step 1 - reverse the input
        while count >= 0:
            revpiece += pieces[count]
            count-=1
        #step 2 - replace vowels
        for x in pieces:
            if v.get(x,9) != 9: revpiece = revpiece.replace(x, v[x])
        #step 3 - add 'aca' to the end of each word
        result += revpiece+'aca '
    result.rstrip()
    #if not txt.islower(): result = result.upper()
    return (result)

msg = input('Enter a message to encrypt: ')
print(karaka(msg))