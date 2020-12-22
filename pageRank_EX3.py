import numpy 

# MATRICE : M 
#_| a  | b   | c | d |e
#a| 0  | 1/4 |1/4|1/4|0
#b| 1/4| 0   |1/4|1/4|0
#c| 1/4|1/4  |  0|1/4|0
#d| 1/4|1/4  |1/4| 0 |0
#e| 1/4|1/4  |1/4|1/4|0

matrice = numpy.array([0, 0.25, 0.25, 0.25, 0, 0.25, 0, 0.25, 0.25, 0,0.25, 0.25, 0, 0.25, 0,0.25, 0.25, 0.25, 0, 0,0.25, 0.25, 0.25, 0.25, 0],float)
M = matrice.reshape(5,5)
print ('Matrice', M)

#R0
R0 = numpy.array([0.2,0.2,0.2,0.2,0.2])
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
