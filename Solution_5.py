#Grandest stair case of them all, how many possible stair cases
def answer5(n):
    func=[[1,0]]
    for x in range(1,n):
        func=mult(func,[[1,0],[1,x]],n)
    return func[-1][0]
    
def mult(og,new,n):
    d={}
    for x in og:
        for y in new:
            if x[1]+y[1] <=n:
            	#Multiply in new term
                term = [x[0]*y[0],x[1]+y[1]]
                if term[1] not in d:
               		d[term[1]] =0
               	d[term[1]]+=term[0]
    final =[]
    for term in d:
    	final.append((d[term],term))
    return final