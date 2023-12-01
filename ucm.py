import numpy as np
import matplotlib.pyplot as plt
from scipy import constants as cp

class Plt():
    def __init__(self, c:dict=None):

        fig, ax = plt.subplots()

        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

        # Remove ticks on the right and top sides of the plot
        ax.yaxis.tick_left()
        ax.xaxis.tick_bottom()


        plt.gca().set_aspect('equal')

        plt.title(r'$\mathrm{%s}$' % "𝑦", fontsize=14)
        plt.grid(True, linestyle='solid', alpha=0.4, linewidth=0.5, color='black', which='major')
        plt.grid(True, linestyle='solid', alpha=0.2, linewidth=0.5, color='black', which='minor')
        plt.minorticks_on()
        plt.axhline(0, color="black", alpha=0.7, linewidth=1)
        plt.axvline(0, color="black", alpha=0.7, linewidth=1)
        axis_val = 10
        plt.axis(xmin=-axis_val, ymin=-axis_val, xmax=axis_val, ymax=axis_val)
        plt.xticks(color='w', )
        plt.yticks(color='w')
        plt.grid(True)

        plt.text(-0.2,-0.2,r'$\mathrm{%s}$' % "0,0",fontsize=8,horizontalalignment="right",verticalalignment="top")
        plt.text(8,0,r'$\mathrm{%s}$' % "𝑥ₒ",fontsize=12,horizontalalignment="center",verticalalignment="top")
        plt.text(-8,0,r'$\mathrm{%s}$' % "-𝑥ₒ",fontsize=12,horizontalalignment="center",verticalalignment="top")

        plt.text(10.2,0, r'$\mathrm{%s}$' % "𝑥", fontsize=14,horizontalalignment="left",verticalalignment="center")
        
        plt.text(0,10.2, "▴", fontsize=10,horizontalalignment="center",verticalalignment="top")
        plt.text(10,0, "▸", fontsize=10,horizontalalignment="right",verticalalignment="center")
        
        plt.text(0.1,-0.3, "◂", fontsize=8,horizontalalignment="left",verticalalignment="center")
        plt.text(8*np.cos(np.pi/6),-0.3, "▸", fontsize=8,horizontalalignment="right",verticalalignment="center")
        
        plt.text(8*np.cos(np.pi/6),0.2, "▾", fontsize=8,horizontalalignment="center",verticalalignment="center")
        plt.text(8*np.cos(np.pi/6),8*np.sin(np.pi/6)-0.2, "▴", fontsize=8,horizontalalignment="center",verticalalignment="center")
        
        plt.text(8*np.cos(np.pi/6)*(1/2),-0.3 , r'$\mathrm{%s}$' % "𝑥ₒ𝑐𝑜𝑠(𝜔𝑡+𝜀)", fontsize=10,horizontalalignment="center",verticalalignment="top")
        plt.text(8*np.cos(np.pi/6) , 8*np.sin(np.pi/6)*(1/2), r'$\mathrm{%s}$' % "𝑥ₒ𝑠𝑖𝑛(𝜔𝑡+𝜀)", fontsize=10, horizontalalignment="left",verticalalignment="center")
        
        plt.text((8*np.cos(np.pi/6))*(1/3) , 0.3, r'$\mathrm{%s}$' % "𝜀", fontsize=7, horizontalalignment="left",verticalalignment="center")
        plt.text((8*np.cos(np.pi/6))*(1/3.5) , 0.85, r'$\mathrm{%s}$' % "𝜔𝑡", fontsize=7, horizontalalignment="left",verticalalignment="center")

        self.function_list = {
                              "sin": np.sin, "cos": np.cos, "tan": np.tan,
                              "log": np.log, "log10": np.log10, "e": np.e,
                              "abs" : np.absolute, "arcsin" : np.arcsin,
                              "arccos" : np.arccos, "arctan" : np.arctan,
                              "sinh" : np.sinh,  "cosh" : np.cosh,"tanh" : np.tanh,
                              "sqrt" : np.sqrt, "pi" : np.pi, "exp" : np.exp,
                              "h":cp.h, "c":cp.c, "k":cp.k
                              }
        if c:
            self.function_list.update(c)
        
        self.plot_function("(8**2-x**2)**(1/2)", "red", -8, 8) # top half of circle
        self.plot_function("-(8**2-x**2)**(1/2)", "red", -8, 8) #bottom half of circle
        
        lw =0.8
        
        plt.plot([8*np.cos(np.pi/6),8*np.cos(np.pi/6)],[0,8*np.sin(np.pi/6)],color='black',linestyle='--',alpha=1, linewidth=lw) # line from the origin to the point
        plt.plot([0 , 8*np.cos(np.pi/6)],[0 , 8*np.sin(np.pi/6)],color='black',linestyle='--',alpha=1, linewidth=lw) # vertical line to the point
        plt.plot([0.2 , 8*np.cos(np.pi/6)-0.2],[-0.3 , -0.3],color='black',linestyle='--',alpha=1, linewidth=lw) # horizontal line with the arrows connecting
        
        plt.plot([8*np.cos(np.pi/16),8*np.cos(np.pi/16)],[0,8*np.sin(np.pi/16)],color='black',linestyle='--',alpha=0.6, linewidth=lw/2) # line from the origin to the point at t=0
        plt.plot([0 , 8*np.cos(np.pi/16)],[0 , 8*np.sin(np.pi/16)],color='black',linestyle='--',alpha=0.6, linewidth=lw/2) # vertical line to the point at t=0

        self.plot_function("(3**2-x**2)**(1/2)", "black", 3*np.cos(np.pi/6), 3, lw/2, 0.6)

        plt.savefig('ucm.png', dpi=600)

    def plot_function(self, fx, color, frm, to, line_width:float=1.1, a:float=1):
        fx = str(fx)
        x_val = np.linspace(frm, to, 1000000)
        self.function_list.update({"x":x_val})
        f = lambda x: eval(fx, {"__builtins__": None} , self.function_list)
        y_val = f(x_val)
        plt.plot(x_val, y_val, color=color, linewidth = line_width, alpha=a)
        

Plt()