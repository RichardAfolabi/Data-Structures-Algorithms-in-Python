
# coding: utf-8

## Enthought Python Worksheet

# In[7]:

get_ipython().magic(u'matplotlib inline')
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 30)
y = np.sin(x)
mu, sigma = 0, 1
z = y + np.random.normal(mu, sigma, 30) * 0.1

plt.clf()
plt.grid()
plt.plot(x, y, 'ro-')
plt.plot(x, z, 'b-')
plt.legend(('Sine wave', 'Noisy wave'), loc='best', fancybox=True, shadow=True)
plt.xlabel('X axis')
plt.ylabel('Y axis')





# In[1]:

elmt = dict(day="Friday", month=2, year= 3012)


print elmt.keys()
print elmt.items()
print elmt.values()

for i in elmt:
    print(elmt[i])


# In[ ]:



