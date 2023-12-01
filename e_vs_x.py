import numpy as np
import matplotlib.pyplot as plt
#from sympy import latexify
from scipy import constants as cp

class Plt():
    def __init__(self, c:dict=None):

        plt.title(r'$\mathrm{%s}$' % "𝐸𝑛𝑒𝑟𝑔𝑦", fontsize=14)
        plt.grid(True, linestyle='solid', alpha=0.4, linewidth=0.5, color='black', which='major')
        plt.grid(True, linestyle='solid', alpha=0.2, linewidth=0.5, color='black', which='minor')
        plt.minorticks_on()
        plt.axhline(0, color="black", alpha=0.7, linewidth=1)
        plt.axvline(0, color="black", alpha=0.7, linewidth=1)
        axis_val = 36
        plt.axis(xmin=-10, ymin=0, xmax=10, ymax=axis_val)
        plt.xticks(color='w', )
        plt.yticks(color='w')
        plt.grid(True)

        plt.text(-0.2,-0.2,r'$\mathrm{%s}$' % "(0,0)",fontsize=8,horizontalalignment="center",verticalalignment="top")
        plt.text(8,0,r'$\mathrm{%s}$' % "𝑥ₒ",fontsize=12,horizontalalignment="center",verticalalignment="top")
        plt.text(-8,0,r'$\mathrm{%s}$' % "-𝑥ₒ",fontsize=12,horizontalalignment="center",verticalalignment="top")

        plt.text(10.2,0, r'$\mathrm{%s}$' % "𝑥", fontsize=14,horizontalalignment="left",verticalalignment="center")
        plt.text(0,36.2, "▴", fontsize=10,horizontalalignment="center",verticalalignment="top")
        plt.text(10,0, "▸", fontsize=10,horizontalalignment="right",verticalalignment="center")

        plt.text(4,32.2,r'$\mathrm{%s}$' % "𝑇𝑜𝑡𝑎𝑙 𝐸𝑛𝑒𝑟𝑔𝑦",fontsize=10,horizontalalignment="center",verticalalignment="bottom")
        plt.text(3.5,27.5,r'$\mathrm{%s}$' % "𝐾𝑖𝑛𝑒𝑡𝑖𝑐 𝐸𝑛𝑒𝑟𝑔𝑦",fontsize=10,horizontalalignment="left",verticalalignment="top", rotation=-60)
        plt.text(3.5,4,r'$\mathrm{%s}$' % "𝑃𝑜𝑡𝑒𝑛𝑡𝑖𝑎𝑙 𝐸𝑛𝑒𝑟𝑔𝑦",fontsize=10,horizontalalignment="left",verticalalignment="bottom", rotation=60)
       

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
        
        self.plot_function("(1/2)*(8**2-x**2)", "red", -8, 8)
        self.plot_function("-(1/2)*(8**2-x**2)+32", "red", -8, 8)
        self.plot_function("32*x**0", "red", -8, 8)
        
        #plt.show()
        plt.savefig('e_vs_x.png', dpi=600)

    def plot_function(self, fx, color, frm, to):
        fx = str(fx)
        x_val = np.linspace(frm, to, 1000000)
        self.function_list.update({"x":x_val})
        f = lambda x: eval(fx, {"__builtins__": None} , self.function_list)
        y_val = f(x_val)
        plt.plot(x_val, y_val, color=color, linewidth=1.1)
        

Plt()