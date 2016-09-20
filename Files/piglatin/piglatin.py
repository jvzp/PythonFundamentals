def to_piglatin(word):
	vowels = ['a','e','i','o','u']
	if word[0] in vowels:
		return "{}{}".format(word,"ay")
	else:
		if word[1] in vowels:
			return "{}{}{}".format(word[1:],word[0],"ay")
		else:
			if word[2] in vowels:
				return "{}{}{}".format(word[2:],word[0:2],"ay")
			else:
				if word[3] in vowels:
					return "{}{}{}".format(word[3:],word[0:3],"ay")
