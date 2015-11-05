import braille_alphabet, braille_punctuation, braille_digits, braille_contractions, braille_complex


currentlyQuoting = False
currentlyNumbers = False
uppercaseAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def translateDocument(documentContents): 
	brailleContent = ""
	contentList = documentContents.split()
	for word in contentList:
		brailleWord = translate(word) + " "
		brailleContent += brailleWord
	return brailleContent
#if it begins with starting point of contraction, look at the next two or three. 
#if they match a contraction, replace the first with the shorthand, then delete the next letter.

def translate(englishWord):
	newWord = ""
	if englishWord in braille_contractions.acb_contractions:
		newWord = chr(braille_contractions.acb_contractions[englishWord])
		return newWord
	if englishWord in braille_complex.comp_cont_1:
		return lookupComplexContraction(englishWord)
	else:
		for a in englishWord:
		#if a = 'g' OR a='s' OR a='a' OR a='b' OR a='c' OR a='o' OR a='e' OR a='i':
		#	new_word = new_word + check_lv2(word, a)
		#	new_a = frag_length()
		#	a = a+new_a
		#else:
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

