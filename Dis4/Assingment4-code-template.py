import numpy 
import matplotlib.pyplot as plt

# what each data point is called:
names = ["football","baseball","basketball","tennis","softball","canoeing","handball","rugby","hockey","ice hockey","swimming","track","boxing","volleyball","lacrosse","skiing","golf","polo","surfing","wrestling","gymnastics"]

 # load the csv provided on bcourses
similarities = numpy.loadtxt(open("similarities.csv", "rb"), delimiter=",", skiprows=1)


distances = ## *FILL IN* - How should we convert similarities to distances?


D = 2 # How many dimensions we are going to use
N = distances.shape[0] # the number of items
assert(distances.shape[1] == N and N==len(names)) # be sure we loaded as many items as we have names for

def dist(a,b):
    # Compute the Euclidean distance between two locations (numpy arrays) a and b
    # Thus, dist(pos[1], pos[2]) gives the distance between the locations for items 1 and 2
    
    ## *FILL IN*

    
def stress(p):
    # Take a matrix of positions (called here "p") and return the stress
	
	## *FILL IN*

def add_delta(p, i, d, delta):
    # This is a helper function that will make a new vector which is the same as p (a position matrix), except that
    # p[i,d] has been increased by delta (which may be positive or negative)
    v = numpy.array(p)
    v[i, d] += delta
    return v

def compute_gradient(p, i,d, delta = 0.001):
    # compute the gradient of the stress function with repect to the [i,d] entry of a position matrix p
    # (e.g. the derivative of stress with respect to the i'th coordinate of the x'th dimension)
    # Here, to compute numerically, you can use the fact that
    # f'(x) = (f(x+delta)-f(x-delta))/(2 delta) as delta -> 0
    
    ## *FILL IN*

    

def compute_full_gradient(p):
    # Numerically compute the full gradient of stress at a position p
    # This should return a matrix whose elements are the gradient of stress at p with respect to each [i,d] coordinate
  
	## *FILL IN*


# Pick a position for each point. Note this is an NxD matrix
# so that pos[11,1] is the y coordinate for the 11th item
# and pos[11] is a (row) vector for the position of the 11th item
pos = numpy.random.normal(0.0,1.0,size=(N,D))

# Now go through and adjust the position to minimize the stress
for steps in range(100):
    
    ## *FILL IN*


## *FILL IN* -- and plot
