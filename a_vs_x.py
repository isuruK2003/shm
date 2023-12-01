import numpy as np
import matplotlib.pyplot as plt
import sympy as smp
from scipy import constants as cp

class Plt():
    def __init__(self, fx:str, c:dict, xlabel:str, ylabel:str):
        self.fx = fx
        
        fig, ax = plt.subplots()
        
        #ax.set_ylabel(r'$\mathrm{%s}$' % ylabel, fontsize=10)
        #ax.set_xlabel(r'$\mathrm{%s}$' % xlabel, fontsize=10)
        
        plt.title(r'$\mathrm{%s}$' % ylabel, fontsize=14)

        plt.grid(True, linestyle='solid', alpha=0.4, linewidth=0.5, color='black', which='major')
        plt.grid(True, linestyle='solid', alpha=0.2, linewidth=0.5, color='black', which='minor')
        
        plt.minorticks_on()
        
        plt.axhline(0, color="black", alpha=0.7, linewidth=1)
        plt.axvline(0, color="black", alpha=0.7, linewidth=1)
        axis_val = 12
        plt.axis(xmin=-axis_val, ymin=-axis_val, xmax=axis_val, ymax=axis_val)
        
        plt.text(-0.2,-0.2,r'$\mathrm{%s}$' % "0,0",fontsize=8,horizontalalignment="right",verticalalignment="top")
        
        plt.text(10,0,r'$\mathrm{%s}$' % "𝑥ₒ",fontsize=12,horizontalalignment="center",verticalalignment="bottom")
        plt.text(-10,0,r'$\mathrm{%s}$' % "𝑥ₒ",fontsize=12,horizontalalignment="center",verticalalignment="top")
        
        plt.text(0,10,r'$\mathrm{%s}$' % "𝑎ₘₐₓ",fontsize=12,horizontalalignment="left",verticalalignment="bottom")
        plt.text(0,-10,r'$\mathrm{%s}$' % "𝑎ₘₐₓ",fontsize=12,horizontalalignment="right",verticalalignment="center")
        
        plt.text(13,0, r'$\mathrm{%s}$' % xlabel, fontsize=12,horizontalalignment="right",verticalalignment="center")
        
        plt.text(0,12.2, "▴", fontsize=10,horizontalalignment="center",verticalalignment="top")
        plt.text(12,0, "▸", fontsize=10,horizontalalignment="right",verticalalignment="center")
                
        # xticks color white
        plt.xticks(color='w')
 
        # yticks color white
        plt.yticks(color='w')
        plt.grid(True)

        self.function_list = {
                              "sin": np.sin, "cos": np.cos, "tan": np.tan,
                              "log": np.log, "log10": np.log10, "e": np.e,
                              "abs" : np.absolute, "arcsin" : np.arcsin,
                              "arccos" : np.arccos, "arctan" : np.arctan,
                              "sinh" : np.sinh,  "cosh" : np.cosh,"tanh" : np.tanh,
                              "sqrt" : np.sqrt, "pi" : np.pi, "exp" : np.exp,
                              "h":cp.h, "c":cp.c, "k":cp.k
                              }
        self.function_list.update(c)
        
    def plot_function(self):
        fx = str(self.fx)
        x_val = np.linspace(-10, 10, 1000000)
        self.function_list.update({"x":x_val})
        f = lambda x: eval(fx, {"__builtins__": None} , self.function_list)
        y_val = f(x_val)
        plt.plot(x_val, y_val, color="red", linewidth=1.1)
        
        plt.plot([-10,-10], [0,10], color="black", linewidth=1.5, linestyle="dotted", alpha=0.5)
        plt.plot([10,10], [0,-10], color="black", linewidth=1.5, linestyle="dotted", alpha=0.5)
        
        plt.plot([0,-10], [10,10], color="black", linewidth=1.5, linestyle="dotted", alpha=0.5)
        plt.plot([0,10], [-10,-10], color="black", linewidth=1.5, linestyle="dotted", alpha=0.5)
        
        
        #plt.show()
        plt.savefig('a_vs_x.png', dpi=600)

Plt(fx="-ω**2*x", c={"ω":1}, xlabel="𝑥", ylabel="𝑎=-𝜔^2𝑥").plot_function()