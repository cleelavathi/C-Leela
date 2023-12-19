import matplotlib.pyplot as plt
plt.figure(figsize=(5,5))
institutes =[ "Nareshit","Satech","Gana Tech.","Pee Tech.","Dreams Solu."]
values =[3803,638,150,374,296]
explode = [0.05,0,0,0,0] #explode 1st i.e slice is separated by 0.05 distance
colors =["c","b","g","r","y"]
plt.pie(values, labels=institutes, explode=explode, colors=colors, autopct="%0.1f%%")
plt.show()
import numpy as np
import matplotlib.pyplot as plt
# Compute the x and y coordinates for points on sine and cosine curves
x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)
# Plot the points using matplotlib
plt.plot(x, y_sin)
plt.plot(x, y_cos)
plt.xlabel('x axis label')
plt.ylabel('y axis label')
plt.title('Sine and Cosine')
plt.legend(['Sine', 'Cosine'])
plt.show()