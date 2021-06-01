import matplotlib.pyplot as plt
import numpy as np

nums = np.array([0.5, 0.7, 1.0, 1.2, 1.3, 2.1])
bins = [0, 1, 2, 3]
plt.hist(nums, bins)
plt.title('Histogram of nums against bins')
plt.xlabel('Nums')
plt.ylabel('Bins')
plt.show()
