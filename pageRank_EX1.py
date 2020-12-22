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

matrice = numpy.array([0.3333, 0.5, 0, 0.3333, 0, 0.5, 0.3333, 0.5, 0.5],float)
M = matrice.reshape(3,3)
print ('Matrice', M)

# R0 
# 1/3
# 1/3
# 1/3

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

recursion (M, R0)


