import Config

def morse_encode(input_string):
	logMorse = ""
	for x in range(0, len(input_string)):
		c = input_string[x].upper()
		logMorse = logMorse + Config.morseNumericalKeyVal[c]
		print(Config.morseNumericalKeyVal[c])
	return logMorse
