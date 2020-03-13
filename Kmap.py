import itertools
import copy

def minFunc(numVar, stringIn):
	
	minterms , dont_care = inputProcess(stringIn)
	for i in range(0, len(minterms)):
		minterms[i] = binary(minterms[i], numVar)  # converting decimal values of minterms to binary
	# print(dont_care)
	if dont_care != '-':
		for i in range(0, len(dont_care)):
			dont_care[i] = binary(dont_care[i], numVar)  # converting decimal values of don't care terms to binary
	else:
		dont_care = []

	if len(dont_care) == 16:
		stringOut = '1'
	elif dont_care == [] and minterms == ['']:
		stringOut = '0'
	else:
		# print(dont_care)
		srcList = minterms + dont_care
		# print('srcList', srcList)


		inputList = srcList
		implicants = []
		for n in range(0,numVar + 1):
			resultList = []
			notImplicants = []
			for j in range(0,len(inputList)-1):
				s1 = inputList[j]
				for k in range(j+1,len(inputList)):
					s2 = inputList[k]
					commonResult = common(s1,s2)
					# print('commonResult', commonResult)
					if commonResult != 0:
						resultList.append(commonResult)
						notImplicants.append(s1)
						notImplicants.append(s2)

			resultList = list(set(resultList)) # removing duplicates
			notImplicants = list(set(notImplicants)) # removing duplicates
			implicants = implicants + [item for item in inputList if item not in notImplicants]
			implicants = list(set(implicants))
			inputList = resultList
		# print('implicants', implicants)
		
		dictRoot = {}
		for element in implicants:
			dashCount = element.count('-')
			dictRoot[element] = rootList(element, dashCount)

		essentialImplicants = essential(dictRoot, minterms)
		# print('essentialImplicants', essentialImplicants)
		remainingMinterms, remainingImplicants = remainder(essentialImplicants, minterms, dictRoot)
		# print('remainingImplicants', remainingImplicants)
		posList = pos(remainingMinterms, remainingImplicants, dictRoot)
		# print('posList', posList)
		result = minimumTerm(posList)
		minimum = minimumTerm(posList)
		# print('minimum', minimum)
		
		booleanExpression = []
		for i in range(0, len(essentialImplicants)):
			booleanExpression.append(expression(essentialImplicants[i]))

		minExpression = ''
		for i in range(0, len(minimum)):
			minExpression = minExpression + expression(minimum[i])
		minExpression = removeDuplicates(minExpression)
		stringOut = ''
		if minExpression != '':
			booleanExpression.append(minExpression)
		booleanExpression.sort()
		for i in range(0, len(booleanExpression)):
			if stringOut:
				stringOut = stringOut + '+' + booleanExpression[i]
			else:
				stringOut = booleanExpression[i]
	
	return stringOut

def inputProcess(stringIn):
	"""
	Processes the input
	Separates minterms and maxterms in two lists
	"""
	x = stringIn.find('d')
	minterms = stringIn[:x]
	minterms = minterms.replace('(', '')
	minterms = minterms.replace(')', '')
	minterms = minterms.strip()
	minterms = minterms.split(',')

	dont_care = stringIn[x+1:]
	dont_care = dont_care.strip()
	if dont_care != '-':
		dont_care = dont_care.replace('(', '')
		dont_care = dont_care.replace(')', '')
		dont_care = dont_care.split(',')
	return minterms, dont_care


def binary(num, numVar):
	"""
	Converts the numbers to binary
	Inputs are string containing decimal number and the number of variables
	Returns binary value as a string
	"""
	if num == '0':
		num = '0000'
	elif num == '1':
		num = '0001'
	elif num == '2':
		num = '0010'
	elif num == '3':
		num = '0011'
	elif num == '4':
		num = '0100'
	elif num == '5':
		num = '0101'
	elif num == '6':
		num = '0110'
	elif num == '7':
		num = '0111'
	elif num == '8':
		num = '1000'
	elif num == '9':
		num = '1001'
	elif num == '10':
		num = '1010'
	elif num == '11':
		num = '1011'
	elif num == '12':
		num = '1100'
	elif num == '13':
		num = '1101'
	elif num == '14':
		num = '1110'
	elif num == '15':
		num = '1111'
	if numVar == 4:
		return num
	elif numVar == 3:
		return num[1:]
	elif numVar == 2:
		return num[2:]
	elif numVar == 1:
		return num[3]

def group(list):
	"""
	Dividing the binary numbers into groups depending upon the number of 1s in them
	"""
	group0 = [] #0 one
	group1 = [] # 1 one
	group2 = [] # 2 one
	group3 = [] # 3 one
	group4 = [] # 4 one
	for num in list:
		count_1 = num.count('1')
		if count_1 == 0:
			group0.append(num)
		elif count_1 == 1:
			group1.append(num)
		elif count_1 == 2:
			group2.append(num)
		elif count_1 == 3:
			group3.append(num)
		elif count_1 == 4:
			group4.append(num)
	Group = [group0, group1, group2, group3, group4]
	return Group
	
def common(s1, s2):
	"""
	Finds if strings differ only by 1 bit.
	Returns 0 in case they differ by more than 1 bit else returns a string with _ in place of differing bit.
	"""
	count = 0
	# print('len s1', len(s1))
	# print('len s2', len(s2))
	if len(s1) != len(s2):
		return 0
	for i in range(0, len(s1)):
		if s1[i] == s2[i]:
			count += 1
		else:
			diff = i
	if count == len(s1) - 1:
		s1 = s1[:diff] + '-' + s1[diff+1:]
		return s1
	else:
		return 0

def rootList(s, dashCount):
	"""
	Finds the initial minterms and don't cares that the implicants are coming form.
	Returns a list
	"""
	lst = list(itertools.product([0, 1], repeat=dashCount))
	n = len(s)
	l = []
	for i in range (0, 2**dashCount):
		x = 0
		num = 0
		temp = copy.deepcopy(s)
		while x < n and x >= 0:
			dash = temp.find('-', x)
			if dash == -1:
				break
			else:
				temp = list(temp)
				temp[dash] = lst[i][num] # Changing dash to 1 or 0
				temp = ''.join(str(e) for e in temp) # list to string
				num += 1
				x = dash + 1
		l.append(temp)
	return l

def essential(dictRoot, minterms):
	"""
	Finds the essential prime implicants and returns it as a list
	"""
	essentialImplicants = []
	for element in minterms:
		count = 0
		matched_key = ''
		for key, value in dictRoot.items():
			if element in value:
				count += 1
				matched_key = key
		if count == 1:
			essentialImplicants.append(matched_key)
	essentialImplicants = list(set(essentialImplicants))
	return essentialImplicants

def remainder(essentialImplicants, minterms, dictRoot):
	"""
	Finding remaining implicants
	"""
	essentialList = []
	for element in essentialImplicants:
		essentialNum = dictRoot[element]
		essentialList += essentialNum
	essentialList = list(set(essentialList))
	remainingMinterms = [item for item in minterms if item not in essentialList]
	remainingImplicants = [item for item in dictRoot.keys() if item not in essentialImplicants]
	return remainingMinterms, remainingImplicants

def pos(remainingMinterms, remainingImplicants, dictRoot):
	"""
	Finding the product of sum expresseion
	"""
	posList = []
	for minterm in remainingMinterms:
		pos = []
		for primeImplicant in remainingImplicants:
			if minterm in dictRoot[primeImplicant]:
				pos.append(primeImplicant)
		posList.append(pos)
	return posList

def minimumTerm(posList):
	"""
	Finds the minimum length term out of all the resultant terms of the pos.
	"""
	result = list(itertools.product(*posList))
	result = list(set(result))
	for i in range(0,len(result)):
		result[i] = list(set(result[i]))
	result.sort()
	if result:
		minimum = result[0]

	minLength = len(result[0])
	for i in range(0,len(result)):
		if len(result[i]) < minLength:
			minLength = len(result[i])
			minimum = result[i]  
	return minimum

	
def expression(s):
	"""
	Finds the boolean expression corresponding the binary number
	"""
	if s == '----':
		s = '1'
	else:
		try:
			s,i = replace(s, 0, 'w')
		except IndexError:
			pass
		try:
			s,i = replace(s, i, 'x')
		except IndexError:
			pass
		try:
			s,i = replace(s, i, 'y')
		except IndexError:
			pass
		try:
			s,i = replace(s, i, 'z')
		except IndexError:
			pass
	return s

def replace(s, i, replacement):
	"""
	Replaces 1 with x, 0 with x' and removes dashes. 
	x is taken as an input variable
	Returns string and next index
	"""
	s = list(s)
	if s[i] == '1':
		s[i] = replacement
		i += 1
	elif s[i] == '0':
		s[i] = replacement + "'"
		i += 2 
	else:
		s[i] = ""
	s = ''.join(str(e) for e in s) 
	return s, i

def removeDuplicates(s):
	"""
	Removes duplicate characters from a string
	"""
	unique = ''
	for x in s:
	    if not(x in unique) or not(x in ['w','x','y','z']):
	        unique = unique + x
	return unique

