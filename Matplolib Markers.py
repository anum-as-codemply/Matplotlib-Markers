import matplotlib.pyplot as plt
import numpy as np

#you can give your own x and y points
xpoints= np.array([0,7,10,21,32])
ypoints= np.array([0,4,13,26,32])

#REMOVE THE COMMENT OF MARKER YOU WANT
#dont forget to comment down the marker you dont want
#otherwise both markers will be merged up
#Also add colors as per your choice
#default named colors file is attached too
#you can use them instead of HEX values

#plotting points with circle marker
plt.plot(xpoints, ypoints, marker= 'o',ms= 10, mec= "Red", mfc= "Yellow")
#plotting points with star marker
#plt.plot(xpoints, ypoints, marker= '*')
#plotting points with point marker
#plt.plot(xpoints, ypoints, marker= '.')
#plotting points with pixel marker
#plt.plot(xpoints, ypoints, marker= ',')
#plotting points with X marker
#plt.plot(xpoints, ypoints, marker= 'x')
#plotting points with filled X marker
#plt.plot(xpoints, ypoints, marker= 'X')
#plotting points with plus marker
#plt.plot(xpoints, ypoints, marker= '+')
#plotting points with filled plus marker
#plt.plot(xpoints, ypoints, marker= 'P')
#plotting points with square marker
#plt.plot(xpoints, ypoints, marker= 's')
#plotting points with diamond marker
#plt.plot(xpoints, ypoints, marker= 'D')
#plotting points with thin diamond marker
#plt.plot(xpoints, ypoints, marker= 'd')
#plotting points with pentagon marker
#plt.plot(xpoints, ypoints, marker= 'p')
#plotting points with hexagon marker
#plt.plot(xpoints, ypoints, marker= 'h')
#plotting points with triangle down marker
#plt.plot(xpoints, ypoints, marker= 'v')
#plotting points with triangle up marker
#plt.plot(xpoints, ypoints, marker= '^')
#plotting points with triangle left marker
#plt.plot(xpoints, ypoints, marker= '<')
#plotting points with triangle right marker
#plt.plot(xpoints, ypoints, marker= '>')
#plotting points with down arrow marker
#plt.plot(xpoints, ypoints, marker= '1')
#plotting points with up arrow marker
#plt.plot(xpoints, ypoints, marker= '2')
#plotting points with left arrow marker
#plt.plot(xpoints, ypoints, marker= '3')
#plotting points with right arrow marker
#plt.plot(xpoints, ypoints, marker= '4')
#plotting points with Vline marker
#plt.plot(xpoints, ypoints, marker= '|')
#plotting points with Hline marker
#plt.plot(xpoints, ypoints, marker= '_')

plt.show()
