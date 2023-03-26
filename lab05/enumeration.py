import matplotlib.pyplot as plt



def enumerate_two_dice_sum():
    
    sums = []
    for i in range(1,7):
        for j in range(1,7):
            sum = j+i
            sums.append(sum)

    return sums


sums = enumerate_two_dice_sum()

plt.hist(sums, bins=range(1, max(sums)+2), density=True)
plt.show()