import numpy as np
import matplotlib.pyplot as plt
def sigmoid(x,deriv = False):


	if (deriv ==True):


		return x*(1-x)
	return 1/(1+np.exp(-x))

x =np.array([[0,0,1],[0,1,1],[1,0,1],[1,1,1]])
y= np.array([[0],[1],[1],[0]])

#seed 
np.random.seed(1)

#synapses
syn0 = 2*np.random.random((3,4))-1.
syn1 = 2*np.random.random((4,1))-1

error=[]

#training loop 
for j in range (1,60000):
	#layers
	l0=x
	l1=sigmoid(np.dot(l0,syn0))
	l2=sigmoid(np.dot(l1,syn1))
	#back propogation
	l2err = y -l2
	
	dl2=l2err*sigmoid(l2,deriv=True)
	l1err = dl2.dot(syn1.T)
	dl1=l1err*sigmoid(l1,deriv=True)
	syn1+=l1.T.dot(dl2)
	syn0+=l0.T.dot(dl1)
	error.append(np.mean(abs(l2err)))


plt.plot(error)
plt.show()
print ('output after training' ,l2)
unknown=np.array([[1,0,1]])
layer1=sigmoid(np.dot(unknown,syn0))
layer2=sigmoid(np.dot(layer1,syn1))
print("Unknown=",layer2)



