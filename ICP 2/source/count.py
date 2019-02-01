file1=open("test.txt", "r" )
words=0
letters=0
line=file1.readline()
while(line!=""):
    words=words+len(line.split())
    letters=letters+len(line)-1
    print("words and letters are",words,letters)
    words=0
    letters=0
    line=file1.readline()