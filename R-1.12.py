# importing the required library
import random
import seaborn as sns
import matplotlib.pyplot as plt

def myChoice(seq):
    i = random.randrange(0, len(seq))
    return seq[i]

val=[1,2,3,4,5]
myData=list()
random.seed(42)
for i in range(500):
    myData.append(myChoice(val))

yourData=list()
random.seed(42)
for i in range(500):
    yourData.append(random.choice(val))

plt.figure()
plt.title("Mine")
sns.countplot(myData)

plt.figure()
plt.title("Yours")
sns.countplot(yourData)

# Show the plot
plt.show()

