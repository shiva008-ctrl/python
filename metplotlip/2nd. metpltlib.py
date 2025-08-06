import matplotlib
import matplotlib.pyplot as plt
import numpy as np
# y1=np.array([7, 2, 3,8,2,-1,-3])
# y2=np.array([1, 2, 3,4,5,6,7])
# y3=np.array([2,4,5,6,7,8,99])
# plt.plot(y1,linestyle='--', color='red', linewidth=2, label='Line 1')
# plt.plot(y2,linestyle='-', color='blue', linewidth=2, label='Line 2')
# plt.plot(y3,linestyle=':', color='green', linewidth=2, label='Line 3')
# plt.legend()
# plt.show()

x1 = np.array([1, 4,8,12,16,20])
y1 = np.array([2, 3, 5, 7, 11, 13])
x2 = np.array([1, 2, 3, 4, 5, 6])
y2 = np.array([1, 4, 9, 16, 25, 36])
plt.plot(x1, y1, linestyle='-', color='red',  )
plt.plot(x2, y2, linestyle='-', color='blue', )
plt.title('Example plot')
plt.xlabel('sales')
plt.ylabel('number')
plt.show()