import numpy as np
import matplotlib.pyplot as plt



#X as semi-continuous input range:
x = np.linspace(0, 10, 100)

#Values of y for first, second and third lines:
y_1 = (2 * x + 1)
y_2 = (2 * x + 2)
y_3 = (2 * x + 3)


#Initializing the plot object, and adding the title and captions:

plt.title('Three lines:')
plt.xlabel('X axis')
plt.ylabel('Y axis')

#Plottling the lines and adding colors and captions:
plt.plot(x,y_1, 'mediumpurple')
plt.plot(x,y_2, 'palegreen')
plt.plot(x,y_3, 'rosybrown')

plt.show()

