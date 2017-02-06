#M and F Bomb problem (Greatest Common Denominator Recusion)
def answer4(M, F):
    M = int(M)
    F = int(F)
    gens = helper(M,F,0)
    return str(gens)
    
def helper(M,F,gen):
	print (M,F)
	if (M == 0 or M ==1) and (F ==0 or F == 1):
		return gen-1
		#Cant be multiples
	if M > 1 and F > 1 and (M%F == 0 or F%M ==0):
		return "impossible"
	if M > F:
		mult = M/F
		return helper(M-(mult*F),F,gen+mult)
	if F > M:
		mult = F/M
		return helper(M,F-(mult*M),gen+mult)