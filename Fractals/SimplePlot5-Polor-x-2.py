import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

r = 0  * (np.pi/180)
t = 1000

fig = plt.figure()
ax1 = fig.subplots(subplot_kw={'projection': 'polar'})
ax2 = fig.subplots(subplot_kw={'projection': 'polar'})
fig.canvas.manager.set_window_title('FractalPlot')
#fig.canvas.manager.full_screen_toggle()

# Base entries for first line plot

#ax1.plot(r, t, color ='b', marker = 'o', markersize = '3')
ax1.set_theta_zero_location('N')
ax1.set_theta_direction(-1)
ax1.set_ylim(0,1.02*t)
ax1.set_navigate(False)

line1, = ax1.plot([0, 0],[0,t], color = 'b', linewidth = 1)
dot1, = ax2.plot(r,t,color = 'b', marker = 'o', markersize = '2' )

# Base entries for second line plot
#ax2.plot(r,t)


def update(angle):
    #print("XData: {}\n".format(line1.get_xdata()[0]))
    line1.set_data([angle, angle],[0,t])
    dot1.set_data(line1.get_xdata()[0],t)
    return line1, dot1,

frames = np.linspace(0,2*np.pi,120)

fig.canvas.draw()
ani = FuncAnimation(fig, update, frames=frames, blit=False, interval=1)

plt.show()