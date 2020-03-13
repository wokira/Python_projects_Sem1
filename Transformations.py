from matplotlib import pyplot 
from math import *
pyplot.ion() #Interactive mode on for python

def matrix_mul(X,Y):
	#Matrix Multipication - for mutliplying any two matrices.
	fin = []
	for i in range(len(X)):
		temp = list(Y[0])
		for j in range(len(Y)):
			for k in range(len(Y[0])):
				if j ==0 :
					temp[k] = X[i][j]*Y[j][k]
				else:
					temp[k] += X[i][j]*Y[j][k]
		fin.append(temp)
	return fin 

dec = input("Enter disc or polygon: " ) 
if(dec == 'disc'):
	a,b,r = map(int,input().split())
	#print((a,b,r))
	theta = 0
	pointx = [] 
	pointy = []
#Making a polygon of 2000 points using parametric equation of a circle.		
	while theta <=360: 
		#theta = (theta/180)*(3.14)
		xd = a + r*cos(theta)
		yd = b + r*sin(theta)
		pointx.append(xd)
		pointy.append(yd)
		theta += 0.036

	#print(pointx)

	pyplot.figure()
	pyplot.plot(pointx,pointy)
	pyplot.show()
	i = 0 
	zd = []	
	for i in range (len(pointx)):
		zd.append(1)
	M = []
	M.append(pointx)
	M.append(pointy)
	M.append(zd)
	cmd = ""
	while cmd  != "quit":
		comm = list(input().split())
		cmd = comm[0]
		if cmd == "s":
			#scaling the disc 
			sx= int(comm[1])
			sy =int(comm[2])
			S= [[sx,0,0] , [0,sy,0] , [0,0,1]]
			Dd =matrix_mul(S,M)
			pyplot.figure()
			pyplot.plot(Dd[0],Dd[1])
			pyplot.show()
		elif( cmd == "r"):
			#rotating the polygon 
			t = float(comm[1])
			t = (t/180)*(pi)
			R= [[cos(t), -sin(t), 0], [sin(t), cos(t),0], [0,0,1]]
			Bd = matrix_mul(R,M)
			pyplot.figure()
			pyplot.plot(Bd[0],Bd[1])
			pyplot.show()
		elif( cmd == 't'):
			#translating the polygon. 
			dx = int(comm[1])
			dy = int(comm[2])
			T= [[1,0,dx], [0,1,dy], [0,0,1]]
			Cd = matrix_mul(T,M)
			pyplot.figure()
			pyplot.plot(Cd[0], Cd[1])
			pyplot.show()	
			a = a + dx
			b = b + dy 
			print (a)
			print (b)

	
	

elif(dec == 'polygon'):
	#We are making a polyon here of as many sides as user desires.
	x = input("Enter x coordinates seperated by space:" )
	y = input("Enter y coordinates seperated by space:" )
	x=x.split()
	x=list(map(int,x))
	x.append(x[0])
	y=y.split()
	y=list(map(int,y))
	y.append(y[0])
	pyplot.figure()
	pyplot.plot(x,y) 
	pyplot.show() #Now we can see the polygon
	#we are making a 3*n matrix that includes x,y and z coordinates.
	#This is done to make matrix multiplication easier.
	#i = 0 
	z = []	
	for i in range (len(x)):
		z.append(1)
	A = []
	A.append(x)
	A.append(y)
	A.append(z)
	cmd = ""
	while cmd  != "quit":
		comm = input().split()
		cmd = str(comm[0])
		if cmd == "s":
			#scaling the polygon 
			sx= int(comm[1])
			sy = int(comm[2])
			S= [[sx,0,0] , [0,sy,0] , [0,0,1]]
			D =matrix_mul(S,A)
			pyplot.figure()
			pyplot.plot(D[0],D[1])
			pyplot.show()
		elif( cmd == "r"):
			#rotating the polygon 
			t = float(comm[1])
			t = (t/180)*(pi)
			R= [[cos(t), -sin(t), 0], [sin(t), cos(t),0], [0,0,1]]
			B = matrix_mul(R,A)
			pyplot.figure()
			pyplot.plot(B[0],B[1])
			pyplot.show()
		elif( cmd == 't'):
			#translating the polygon. 
			dx = int(comm[1])
			dy = int(comm[2])
			T= [[1,0,dx], [0,1,dy], [0,0,1]]
			C = matrix_mul(T,A)
			pyplot.figure()
			pyplot.plot(C[0], C[1])
			pyplot.show()
	
	





