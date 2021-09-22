import matplotlib.pyplot as plt

#data
ages = [5,8,45,8,12,36,44,12,26,27]

range = (0,50)
bins = 5

plt.hist(ages, bins, range, color='blue', histtype='bar', rwidth=0.5)

plt.xlabel('ages')
plt.ylabel('count')
plt.title('statics of ages')

plt.show()
