import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

r = 90  * (np.pi/180)
t = 50000

fig = plt.figure()
ax = fig.subplots(subplot_kw={'projection': 'polar'})
fig.canvas.manager.set_window_title('FractalPlot')
ax.plot(r, t, color ='b', marker = 'o', markersize = '3')
ax.set_theta_zero_location('N')
ax.set_theta_direction(-1)
ax.set_ylim(0,1.02*t)

line1, = ax.plot([0, 0],[0,t], color = 'b', linewidth = 1)

def update(angle):
    line1.set_data([angle, angle],[0,t])
    return line1,

frames = np.linspace(0,2*np.pi,120)

fig.canvas.draw()
ani = FuncAnimation(fig, update, frames=frames, blit=True, interval=10)

plt.show()