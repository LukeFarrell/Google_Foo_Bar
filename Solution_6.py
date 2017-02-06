#Absorbing Markov Matrix Problem
from fractions import Fraction
def answer6(m):
    #Initialize Matrix
    Y = [[0 for x in range(len(m))] for x in range(len(m))]
    terminal = []
    nonTerminal = []
    #Keep track of absorbing states
    for i in range(len(m)):
        s = float(sum(m[i]))
        if s != 0:
            nonTerminal.append(i)
            for j in range(len(m)):
                #Put fractions in the matrix
                Y[i][j] = Fraction(m[i][j]/s).limit_denominator()
        else:
            if len(Y) <= 1:
                Y[i][i] = 1
            terminal.append(i)
    
    #Use the absorbing markov method
    if len(Y) > 1:
        I, R, Q = rearange(Y, terminal, nonTerminal)
        IQ = subtract(Q)
        F =  inverse(IQ)
        FR = multiply(F,R)
        return LCM(FR[0])
    #For small matrices use Brute Force
    else:
        a = helper(Y)
        final = LCM(a[0])
        return final[len(nonTerminal):]

def rearange(old,terminal,nonTerminal):
    #rearange the matrix
    t = terminal+nonTerminal
    new = [[0 for x in range(len(old))] for x in range(len(old))]
    for i in range(len(old)):
        for j in range(len(old)):
            new[i][j] = old[t[i]][t[j]]
    for i in range(len(terminal)):
        new[i][i] =1
    #Extreme Indexing to divide the matrix
    I = [[new[i][j] for j in range(len(terminal))] for i in range(len(terminal))]
    R = [[new[::-1][i][j] for j in range(len(terminal))] for i in range(len(nonTerminal))][::-1]
    Q = [[new[::-1][i][::-1][j] for j in range(len(nonTerminal))][::-1] for i in range(len(nonTerminal))][::-1]
    return I, R, Q

def subtract(Q):
    #Contruct the proper identity matrix
    I = [[0 for x in range(len(Q))] for x in range(len(Q))]
    for i in range(len(I)):
        I[i][i] = 1
    #Subtract I - Q
    new = [[0 for x in range(len(Q))] for x in range(len(Q))]
    for i in range(len(Q)):
        for j in range(len(Q)):
            new[i][j] = Fraction(I[i][j] - Q[i][j]).limit_denominator()
    return new

def LCM(l):
    #Calculate the LCM of the while list
    new = []
    temp = 1
    for i in range(0,len(l)):
        #Calculate and check the LCM
        a = lcm(temp, l[i].denominator)
        if a > temp:
            temp = a
    for i in l:
        mult = temp/i.denominator
        new.append(int(i.numerator*mult))
    new.append(int(temp))
    return new

def lcm(x,y):
    if x > y:
        greater = x
    else:
        greater = y
    while(True):
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm

#Use for brute force calculation of small matricies
def helper(a):
    b1 = multiply(a,a)
    b2 = []
    while b1 != b2:
        b2 = b1
        b1 = multiply(a,b1)
    return b1

def multiply(a,b):
    result = [[0 for x in range(len(b[0]))] for x in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(a[0])):
                result[i][j] += Fraction(a[i][k] * b[k][j]).limit_denominator()
    return result

def transpose(m):
    t = []
    for r in range(len(m)):
        tRow = []
        for c in range(len(m[r])):
            if c == r:
                tRow.append(m[r][c])
            else:
                tRow.append(m[c][r])
        t.append(tRow)
    return t

def getMatrixMinor(m,i,j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]

def getMatrixDeternminant(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]
    #Recursively call for determinant
    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant

def inverse(m):
    determinant = getMatrixDeternminant(m)
    #special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]

    #find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transpose(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors