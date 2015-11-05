import os, translator

EnglishFile = open("test.txt", "r+")
str = EnglishFile.read()
print "Read String is : ", str

# Check current position
position = EnglishFile.tell()
print "Current file position : ", position

# Reposition pointer at the beginning once again
position = EnglishFile.seek(0, 0)
str = EnglishFile.read()
print "Again read String is : ", str
EnglishFile.close()

files = os.listdir(os.curdir)
for file in files:
    if '.txt' in file:
    	f = open(file, 'r')
    	fileName = os.path.splitext(f.name)[0]
    	contents = f.read()
    	f.close()

    	fileName += ".txt.tmp"
    	brailleContents = translator.translateDocument(contents)
    	newFile = open(fileName, 'w')
    	newFile.write(brailleContents)
    	newFile.close()

files = os.listdir(os.curdir) #does this need to happen twice??
for file in files:
	if '.txt.tmp' in file:
        	brailleFile = file.replace('.txt.tmp','.brf')
        	os.rename(file, brailleFile)
