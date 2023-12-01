import numpy as np
import matplotlib.pyplot as plt
from scipy import constants as cp

class Plt():
    def __init__(self, fx:str, xlabel:str, ylabel:str, c:dict=None):
        self.fx = fx
        
        fig, ax = plt.subplots()
                
        plt.title(r'$\mathrm{%s}$' % ylabel, fontsize=14)

        plt.grid(True, linestyle='solid', alpha=0.4, linewidth=0.5, color='black', which='major')
        plt.grid(True, linestyle='solid', alpha=0.2, linewidth=0.5, color='black', which='minor')

        plt.minorticks_on()
        
        plt.axhline(0, color="black", alpha=0.7, linewidth=1)
        plt.axvline(0, color="black", alpha=0.7, linewidth=1)
        
        plt.axis(xmin=-12, ymin=-12, xmax=12, ymax=12)
        
        plt.text(0.2,-0.2,r'$\mathrm{%s}$' % "0,0",fontsize=8,horizontalalignment="left",verticalalignment="top")
        
        plt.text(8,0,r'$\mathrm{%s}$' % "𝑥ₒ",fontsize=12,horizontalalignment="center",verticalalignment="top")
        plt.text(-8,0,r'$\mathrm{%s}$' % "-𝑥ₒ",fontsize=12,horizontalalignment="center",verticalalignment="top")
        plt.text(0,8,r'$\mathrm{%s}$' % "𝑣ₘₐₓ",fontsize=12,horizontalalignment="left",verticalalignment="bottom")
        plt.text(0,-8,r'$\mathrm{%s}$' % "𝑣ₘₐₓ",fontsize=12,horizontalalignment="left",verticalalignment="top")
        plt.text(12.2,0, r'$\mathrm{%s}$' % xlabel, fontsize=14,horizontalalignment="left",verticalalignment="center")      
        plt.text(0,12.2, "▴", fontsize=10,horizontalalignment="center",verticalalignment="top")
        plt.text(12,0, "▸", fontsize=10,horizontalalignment="right",verticalalignment="center")

        plt.xticks(color='w', )
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
        if c:
            self.function_list.update(c)

        self.plot_function(func=fx)
        self.plot_function(func=f"-{fx}")
        
    def plot_function(self, func):
        fx = str(self.fx)
        x_val = np.linspace(-11.83, 11.83, 1000000)
        self.function_list.update({"x":x_val})
        f = lambda x: eval(func, {"__builtins__": None} , self.function_list)
        y_val = f(x_val)
        plt.plot(x_val, y_val, color="red", linewidth=1.1)
        plt.savefig('v_vs_x.png', dpi=600)

Plt(fx="sqrt(8**2-x**2)", xlabel="𝑥", ylabel=r'𝑣=𝜔\sqrt{𝑥ₒ^2 - 𝑥^2}')