import sys

def main():
	
	if (len(sys.argv) == 2): # If only word is given
		printBig(sys.argv[1], '#')
	elif (len(sys.argv) == 3): # If both word and character given
		printBig(sys.argv[1], sys.argv[2][0])
	else: # Default
		printBig("HELLO", '#')

def printBig(word, c):
	letterList = [
		["     "+c+"   ", "    "+c+" "+c+"  ", "   "+c+"   "+c+" ", "  "+c+c+c+c+c+c+c, "  "+c+"     "+c], 			# A
		["  "+c+c+c+c+c+" ", "  "+c+"    "+c, "  "+c+c+c+c+c+" ", "  "+c+"    "+c, "  "+c+c+c+c+c+" "],  			# B
		["   "+c+c+c+c+c+c, "  "+c+"      ", "  "+c+"      ", "  "+c+"      ", "   "+c+c+c+c+c+c], 				# C
		["  "+c+c+c+c+c+"  ", "  "+c+"    "+c+" ", "  "+c+"    "+c+" ", "  "+c+"    "+c+" ", "  "+c+c+c+c+c+"  "], 		# D
		["  "+c+c+c+c+c+c+" ", "  "+c+"      ", "  "+c+c+c+c+c+c+" ", "  "+c+"      ", "  "+c+c+c+c+c+c+" "], 			# E
		["  "+c+c+c+c+c+c+" ", "  "+c+"      ", "  "+c+c+c+c+c+c+" ", "  "+c+"      ", "  "+c+"      "], 			# F
		["   "+c+c+c+c+c+c, "  "+c+"      ", "  "+c+"  "+c+c+c+c, "  "+c+"     "+c, "   "+c+c+c+c+c+" "], 			# G
		["   "+c+"    "+c, "   "+c+"    "+c, "   "+c+c+c+c+c+c, "   "+c+"    "+c, "   "+c+"    "+c], 				# H
		["  "+c+c+c+c+c, "    "+c+"  ", "    "+c+"  ", "    "+c+"  ", "  "+c+c+c+c+c], 						# I
		["   "+c+c+c+c, "      "+c, "      "+c, "  "+c+"   "+c, "   "+c+c+c+" "], 						# J
		["  "+c+"    "+c, "  "+c+"  "+c+c+" ", "  "+c+c+c+"   ", "  "+c+"  "+c+c+" ", "  "+c+"    "+c], 			# K
		["  "+c+"     ", "  "+c+"     ", "  "+c+"     ", "  "+c+"     ", "  "+c+c+c+c+c+c], 					# L 
		["  "+c+"     "+c , "  "+c+c+"   "+c+c, "  "+c+" "+c+" "+c+" "+c, "  "+c+"  "+c+"  "+c, "  "+c+"     "+c],  		# M
		["  "+c+c+"    "+c , "  "+c+" "+c+"   "+c, "  "+c+"  "+c+"  "+c, "  "+c+"   "+c+" "+c, "  "+c+"    "+c+c], 		# N
		["   "+c+c+c+c+" ", "  "+c+"    "+c, "  "+c+"    "+c, "  "+c+"    "+c, "   "+c+c+c+c+" "], 				# O
		["  "+c+c+c+c+c+" ", "  "+c+"    "+c, "  "+c+c+c+c+c+" ", "  "+c+"     ", "  "+c+"     "], 				# P
		["   "+c+c+c+c+"  ", "  "+c+"    "+c+" ", "  "+c+"  "+c+" "+c+" ", "  "+c+"   "+c+c+" ", "   "+c+c+c+c+" "+c],  	# Q
		["  "+c+c+c+c+c+" ", "  "+c+"    "+c, "  "+c+c+c+c+c+" ", "  "+c+"  "+c+c+" ", "  "+c+"    "+c], 			# R
		["   "+c+c+c+c+c, "  "+c+"     ","   "+c+c+c+c+" ", "       "+c, "  "+c+c+c+c+c+" "], 					# S
		["  "+c+c+c+c+c+c+c, "     "+c+"   ", "     "+c+"   ", "     "+c+"   ", "     "+c+"   "], 				# T
		["  "+c+"    "+c, "  "+c+"    "+c, "  "+c+"    "+c, "  "+c+"    "+c, "   "+c+c+c+c+" "], 				# U
		["  "+c+"    "+c, "  "+c+"    "+c, "  "+c+"    "+c, "   "+c+"  "+c+" ", "    "+c+c+"  "], 				# V
		["  "+c+"     "+c, "  "+c+"     "+c, "  "+c+"  "+c+"  "+c, "  "+c+"  "+c+"  "+c, "   "+c+c+" "+c+c+" "], 		# W
		["  "+c+"    "+c, "   "+c+"  "+c+" ", "    "+c+c+"  ", "   "+c+"  "+c+" ", "  "+c+"    "+c], 				# X
		["  "+c+"     "+c, "   "+c+"   "+c+" ", "    "+c+c+c+"  ", "     "+c+"   ", "    "+c+"    "], 				# Y
		["  "+c+c+c+c+c, "     "+c+" ", "     "+c+" ", "   "+c+"   ", "  "+c+c+c+c+c], 						# Z
		[" "+c, " "+c, " "+c, " "+c, " "+c],											# |
		["    ", "    ", "    ", "    ", "    "],										# SPACE
		["  "+c+c+" ", "  "+c+c+" ", "  "+c+c+" ", "     ", "  "+c+c+" "],							# !
		["     ", "     ", "     ", "     ", "  "+c+c+" "]

	]

	wordList = []
	for character in word.upper():
		if (character.isalpha()): wordList.append(letterList[ord(character)-ord('A')])
		elif (character == ' '): wordList.append(letterList[27])
		elif (character == '!'): wordList.append(letterList[28])
		elif (character == '.'): wordList.append(letterList[29])
		else: wordList.append(letterList[26])
	
	i = 0
	while (i < 5):
		line = ""
		for x in range(len(wordList)):
			line += wordList[x][i]
		print(line)
		i += 1



if __name__ == '__main__':
	main()
