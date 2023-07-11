import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-45,45,30)
y=3*(x**2)+ (5*x) + 10

plt.plot(x,y)
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.title ('Plotting function ')
plt.show
