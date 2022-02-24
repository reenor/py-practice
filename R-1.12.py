# Python’s random module includes a function choice(data) that returns a random element
# from a non-empty sequence. The random module in- cludes a more basic function randrange, 
# with parameterization similar to the built-in range function, that return a random choice 
# from the given range. Using only the randrange function, implement your own version of 
# the choice function.
import random
import seaborn as sns
import matplotlib.pyplot as plt

def myChoice(seq):
    i = random.randrange(0, len(seq))
    return seq[i]

val = [1,2,3,4,5]
myData = list()
random.seed(42)
for i in range(500):
    myData.append(myChoice(val))

sysData = list()
random.seed(42)
for i in range(500):
    sysData.append(random.choice(val))

plt.figure()
plt.title("Mine")
sns.countplot(myData)

plt.figure()
plt.title("System")
sns.countplot(sysData)

# Show the plot
plt.show()

