import braille_alphabet, braille_punctuation, braille_digits, braille_contractions, braille_complex


currentlyQuoting = False
currentlyNumbers = False
uppercaseAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def translateDocument(documentContents): 
	brailleContent = ""
	contentList = documentContents.split()
	for word in contentList:
		brailleWord = translate(word) 
		brailleWord = shorthandTranslate(brailleWord) + " "
		brailleContent += brailleWord
	return brailleContent

#Full world translation not quite working--if there is or punctuation attached it does 
#not register as a word in the contraction dictionary.
def translate(englishWord):
	newWord = ""
	if englishWord.lower() in braille_contractions.acb_contractions:
		if englishWord == englishWord.lower():
			newWord = chr(braille_contractions.acb_contractions[englishWord.lower()])
		else: 
			newWord = chr(braille_punctuation.composition['capitalization']) + chr(braille_contractions.acb_contractions[englishWord.lower()])
		return newWord
	elif englishWord in braille_complex.comp_cont_1:
		newWord = lookupComplexContraction(englishWord)
		return newWord
	else:
		for a in englishWord:
			nextLetter = lookupCharacter(a)
			newWord = newWord + nextLetter
		newWord = newWord + chr(braille_alphabet.alphabet[' '])
		return newWord

def lookupCharacter(a):
	character = ""
	global currentlyNumbers
	global currentlyQuoting
	if a in braille_alphabet.alphabet or a in uppercaseAlphabet:
		if a in braille_alphabet.alphabet and currentlyNumbers:
			character = chr (braille_punctuation.composition['letter sign']) + chr(braille_punctuation.composition['capitalization']) + chr(braille_alphabet.alphabet[a])
			currentlyNumbers = False
		elif a in uppercaseAlphabet and currentlyNumbers:
			character = chr (braille_punctuation.composition['letter sign']) + chr(braille_punctuation.composition['capitalization']) + chr(braille_alphabet.alphabet[a.lower()])
			currentlyNumbers = False
		elif a in uppercaseAlphabet and not currentlyNumbers:
			character = chr(braille_punctuation.composition['capitalization']) + chr(braille_alphabet.alphabet[a.lower()])
		else:
			character = chr(braille_alphabet.alphabet[a])
	elif a in braille_digits.digits:
		if currentlyNumbers: 
			character = chr(braille_digits.digits[a])
		else:	
			character = chr(braille_punctuation.composition["number sign"]) + chr(braille_digits.digits[a])
			currentlyNumbers = True
	elif a == '"':
		if currentlyQuoting:
			character = chr(braille_punctuation.punctuation['starting "'])
			currentlyQuoting = True
		else:
			character = chr(braille_punctuation.punctuation['ending "'])
			currentlyQuoting = False
	elif a in braille_punctuation.punctuation:
		character = chr(braille_punctuation.punctuation[a])
	return character

def lookupComplexContraction(word):
	shorthand = ""
	if word in braille_complex.comp_cont_1:
		shorthand += chr(braille_complex.comp_cont_1[word])
	if word in braille_complex.comp_cont_2:
		shorthand += chr(braille_complex.comp_cont_2[word])
	if word in braille_complex.comp_cont_3:
		shorthand += chr(braille_complex.comp_cont_3[word])
	if word in braille_complex.comp_cont_4:
		shorthand += chr(braille_complex.comp_cont_4[word])
	if word in braille_complex.comp_cont_5:
		shorthand += chr(braille_complex.comp_cont_5[word])
	if word in braille_complex.comp_cont_6:
		shorthand += chr(braille_complex.comp_cont_6[word])
	return shorthand
def shorthandTranslate(word):
	if word.find('TH') or word.find:
		new = word.replace('TH','?')
	if word.find('CH'):
		new = word.replace('CH', '*')
	if word.find('GH'):
		new = word.replace('GH', '<')
	if word.find('WH'):
		new= word.replace('WH', ':')
	if word.find('SH'):
		new = word.replace('SH', '%')
	if word.find('ED'):
		new = word.replace('ED', '$')
	if word.find('ER'):
		new = word.replace('ER', "]")
	if word.find('OU'):
		backslash = chr(92)
		new = word.replace('OU', backslash)
	if word.find('OW'):
		new = word.replace('OW', "[")
	if word.find('BB'):
		new = word.replace('BB', ';')
	if word.find('CC'):
		new = word.replace('CC', '3')
	if word.find('DD'):
		new = word.replace('DD', '4')
	if word.find('EN'):
		new = word.replace('EN', '5')
	if word.find('GG'):
		new = word.replace('GG', '7')
	if word.find('ING'):
		new = word.replace('ING', '+')
	if word != "IN" and word.find('IN'):
		new = word.replace('IN', '9')
	if word.find('ST'):
		new = word.replace('ST', '/')
	if word.find('AR'):
		new = word.replace('AR', '>')
	return new

	"""shorthand_translate() is inefficient because it cannot account for all possibilities; however, it is simple to 
	add more shorthand words through:
		while word.find(ASCII):
			new = word.replace(oldASCII, newASCII)
	A count can even be set"""