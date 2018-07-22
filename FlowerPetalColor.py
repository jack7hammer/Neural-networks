import numpy as np

#sigmoid and sigmoid prime
def sigmoid(x,deriv=False):
	if(deriv == True):
		return x*(1-x)
	return 1/(1+np.exp(-x))
x=np.array([[3,1.5],[2,1],[4,1.5],[3,1],[3.5,.5],[2,.5],[5.5,1],[1,1]])
y=np.array([[1],[0],[1],[0],[1],[0],[1],[0]])
print(x)
s=np.amax(x,axis=0)
x=x/s


#seed 
np.random.seed(2)

#bias and synapses
b=np.random.randn(1)
syn0=2*np.random.random((2,8))-b
syn1=2*np.random.random((8,1))-b

#training loop
for i in range (1,50000):
	#layer (input)
	l0=x
	#layer (invisible layer)
	l1=sigmoid(np.dot(l0,syn0))
	#layer (output)
	l2=sigmoid(np.dot(l1,syn1))

	#error
	l2err = y- l2

    #correcting error
	db=sigmoid(b,deriv=True)
	dl2=l2err*sigmoid(l2,deriv=True)
	l1err=dl2.dot(syn1.T)
	dl1=l1err*sigmoid(l1,deriv=True)
	syn0+=l0.T.dot(dl1)
	syn1+=l1.T.dot(dl2)
	b+=b*db

#finding the unkown value
print('Output:',l2)
unknown=np.array([[5 ,2]]	)
unknown=unknown/s
layer1=sigmoid(np.dot(unknown,syn0))-b
layer2=sigmoid(np.dot(layer1,syn1))-b
print("unknown",layer2)