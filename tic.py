import numpy as np
w=0

def sigmoid(x,deriv=False):
	if(deriv == True):
		return x*(1-x)
	return 1/(1+np.exp(-x))

m = np.array([' ',' ',' ',' ',' ',' ',' ',' ',' '])
x=np.array([[2,1,0,0,1,0,0,0,0],[0,0,0,0,1,0,0,0,0],[1,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,0,0],[0,0,0,0,0,0,1,0,0],[2,0,1,0,1,0,0,0,0],[2,0,1,1,1,0,2,0,0],[1,0,0,1,2,0,0,0,0],[1,0,0,0,0,0,0,0,0],[1,0,1,0,2,0,0,0,0],[1,0,1,0,2,0,2,1,0],[2,2,0,0,1,0,0,0,1],[2,2,0,0,1,0,0,1,1]])
y=np.array([[7],[0],[4],[4],[4],[6],[5],[6],[4],[1],[1],[2],[2]])

x=x/2
y=y/8

np.random.seed(1)
b=np.random.randn(1)
syn0=np.random.random((9,9))-b
syn1=np.random.random((9,1))-b

#training loop
for i in range(1,5000):
	l0=x
	l1=sigmoid(np.dot(l0,syn0))
	l2=sigmoid(np.dot(l1,syn1))
	l2err=y-l2

	 #correcting error
	db=sigmoid(b,deriv=True)
	dl2=l2err*sigmoid(l2,deriv=True)
	l1err=dl2.dot(syn1.T)
	dl1=l1err*sigmoid(l1,deriv=True)
	syn0+=l0.T.dot(dl1)	
	
	syn1+=l1.T.dot(dl2)
	
	b+=b*db

print(l2)




def mark(x,b):
	if m[x]!=' ' :
		return 1
	m[x]=b
def think(m):

	k=np.array([0,0,0,0,0,0,0,0,0])
	for i in range (9):
		if(m[i]=='X'):
			k[i]=1
		if(m[i]=='O'):
			k[i]=2
	o=np.max(k)
	print(k)
	k=k/2
	layer1=sigmoid(np.dot(k,syn0))-b
	layer2=sigmoid(np.dot(layer1,syn1))-b
	
	return (np.round(layer2*10)-1)



 

def main():
	global w
	global m
	for i in range(9):
		print("\n  1  2  3\n")
		for k in range(3):

			print(k+1,(""+m[k+(k*2)]+" |" + m[(k+1)+(k*2)] + " |" +m[(k+2)+(k*2)] ))
			if(k<2):

			   print("  --------")

		if i%2 == 0:
			print("\n")
			print("Player 1 ")
			l =list(map(int,input().split()))
			c=(l[0]-1)*3+(l[1]-1)
			
			while mark(c,'X'):
				print("cant mark here")
				l =list(map(int,input().split()))
				c=(l[0]-1)*3+(l[1]-1)
			mark(c,'X')

			if win('X'):
				w=1
				break
		else:
			c=abs((int(think(m))))
			print(c)
			while mark(c,'O'):
				c=c+1


			mark(c,'O')
			

			if win('O'):
				w=2
				break

def win(u):
	counter1=0
	counter2=0
	counter3=0
	counter4=0
	for i in range(3):
		
		
		for j in range(3):
			if (m[j+(3*i)]==u):
				counter1 = counter1 +1
				if counter1==3 :
					return 1
				
			if (m[(j*3)+i]==u):
				counter2=counter2+1
				if counter2==3 :
					return 1
			
		counter1=0
		counter2=0


		if (m[i*4]==u):
		    	counter3=counter3 + 1
		    	if counter3==3:
		    		return 1

		if (m[(i+1)*2]==u):
		    	counter4 =counter4+1
		    	if counter4 == 3:
		    		return 1	


		counter3=0
		counter4=0
		    	

main()
print("\n")
for k in range(3):
			print("  "+m[k+(k*2)]+" |" + m[(k+1)+(k*2)] + " |" +m[(k+2)+(k*2)] )
			print(" ----------")
print("\n")
if w==1:
	print("Player 1 is the winner")
if w==2:
	print("You lost sucker!")
if w==0:
	print("Draw!")

