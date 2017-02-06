#Largest possible number composed of other numbers  in a list
def answer2(xs):
	answer =  1
	negL = []
	posL = []
	for x in xs:
		if x > 0:
			posL.append(x)
		if x < 0:
			negL.append(x)

	if len(posL) == 0:
		if len(negL) == 0 or len(negL) == 1:
			return 0

	for num in posL:
		answer*= num

	if len(negL)%2 == 0:
		for num in negL:
			answer*= num
	else:
		negL.sort()
		for num in negL[:-1]:
			answer*=num

	return answer