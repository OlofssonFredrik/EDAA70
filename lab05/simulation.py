import random
import matplotlib.pyplot as plt

def roll_dice_sum(nr):
    sum = 0
    for n in range(nr):
        val = random.randint(1,6)
        sum += val
    return sum

def simulate_dice_sum(nr, tries):
    sums = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    for tri in range(tries):
        sum = 0
        for n in range(nr):
            val = random.randint(1,6)
 
            sum += val
        
        
        sums[sum] += 1
        
    
    for n,val in enumerate(sums):
        sums[n] = val/tries
  
    return sums
        


#print(roll_dice_sum(5))
sums = simulate_dice_sum(2,10000)

#plt.hist(sums, bins=range(1, max(sums)+2), density=True)
#plt.show()

x = [ i for i in range(len(sums)) ]
plt.bar(x, sums, tick_label=x)
plt.show()

