import os, translator
from flask import Flask

app = Flask(_name_)
app.config["DEBUG"] = True 

@app.route("/")
def start():
    if _name_ == "_main_":
        app.run(host="127.0.0.1")

@app.errorHandler(404)
def page_not_found(error):
    return "Sorry, this page was not found" #404

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
