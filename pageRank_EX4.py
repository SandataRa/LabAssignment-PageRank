import numpy 

# MATRICE : M 
#_| a| b| c| d
#a| 0| 0| 0| 1/4	
#b| 1| 0| 0| 1/4	
#c| 0| 1| 0| 1/4
#d| 0| 0| 1| 1/4

# Ra + Rb + Rc + Rd = 1 
# Rd = { 1/4 , 1/4, 1/4 , 1/4 } 
# Rb ? 

matrice = numpy.array([0,0,0,0.25,1,0,0,0.25,0,1,0,0.25,0,0,1,0.25],float)
M = matrice.reshape(4,4)
print ('Matrice', M)

#R0
R0 = numpy.array([0.25,0.25,0.25,0.25])
print ('Init', R0)


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
# B ~ 0.20 
