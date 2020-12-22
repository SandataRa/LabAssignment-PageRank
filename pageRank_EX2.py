import numpy 

# DONNEES 
# a { in : 2, out : 3 } 
# b { in : 2, out : 2 } 
# c { in : 3, out : 2 } 

# Ra? Rb? Rc?

# MATRICE : M 
#_| a  | b   | c
#a| 1/3| 1/2 | 0	
#b| 1/3| 0   | 1/2	
#c| 1/3| 1/2 | 1/2	

# B : 0.8, B-1 : 0.2

# MATRICE : 1/N 
#_| a  | b   | c
#a| 1/3| 1/3 | 1/3	
#b| 1/3| 1/3 | 1/3	
#c| 1/3| 1/3 | 1/3

matrice = numpy.array([0.3333, 0.5, 0, 0.3333, 0, 0.5, 0.3333, 0.5, 0.5],float)
M = matrice.reshape(3,3)
#print ('Matrice M', M)
betaM = numpy.dot(M,0.8)
print(betaM)

mat = numpy.array([0.3333, 0.3333, 0.3333, 0.3333, 0.3333, 0.3333, 0.3333, 0.3333, 0.3333],float)
N = mat.reshape(3,3)
#print ('Matrice N', N)
betaN = numpy.dot(N,0.2)
print(betaN)

A = betaM + betaN
print('Matrice A', A)

R0 = numpy.array([0.3333, 0.3333, 0.3333]) 
print ('Init', R0)

# M * R0 = R1 
# if R1 - R0 ~ 0 

def recursion (Matrice, r):
	rSuivant = numpy.dot(Matrice,r)
	print('R n+1', rSuivant)
	# Seuil
	check = numpy.linalg.norm(rSuivant - r) 
	if (abs(check) > 0.0001 ):
		recursion (Matrice, rSuivant)
	else:
		print('Solution', rSuivant)
		return 

recursion (A, R0)





