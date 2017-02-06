#Largest number divisible by 3 problem 
import itertools
def answer3(l):
	maxVal =  0
	for i in range(len(l),0,-1):
		# Check Divisibility rules:
		for s in itertools.combinations(l,i):
			divisCount = (s.count(1)+s.count(4)+s.count(7))-(s.count(2)+s.count(5)+s.count(8))
			if sum(s)%3 == 0 or divisCount%3 ==0:
				#If it has a solution check all permuations
				combos = set(itertools.permutations(s))
				for combo in combos:
					num = int(''.join(map(str,combo)))
					if num > maxVal and num%3 == 0:
						maxVal = num
		return maxVal
	return maxVal