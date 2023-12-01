import numpy as np
import matplotlib.pyplot as plt

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
        axis_val = 12
        plt.axis(xmin=0, ymin=-axis_val, xmax=axis_val, ymax=axis_val)
        
        plt.text(-0.2,-0.2,r'$\mathrm{%s}$' % "(0,0)",fontsize=8,horizontalalignment="right",verticalalignment="center") 
        plt.text(-0.1,5,r'$\mathrm{%s}$' % "𝑥ₒ",fontsize=12,horizontalalignment="right",verticalalignment="center")
        plt.text(-0.1,-5,r'$\mathrm{%s}$' % "-𝑥ₒ",fontsize=12,horizontalalignment="right",verticalalignment="center")
        #plt.text(0,-5,r'$\mathrm{%s}$' % "-",fontsize=12,horizontalalignment="center",verticalalignment="center")
        #plt.text(0,-5,r'$\mathrm{%s}$' % "-",fontsize=12,horizontalalignment="center",verticalalignment="center")
        plt.text(12.2,0, r'$\mathrm{%s}$' % xlabel, fontsize=14,horizontalalignment="left",verticalalignment="center")
        plt.text(0,12.2, "▴", fontsize=10,horizontalalignment="center",verticalalignment="top")
        plt.text(12,0, "▸", fontsize=10,horizontalalignment="right",verticalalignment="center")
        plt.text(-0.1,5*np.sin(np.pi/6), r'$\mathrm{%s}$' % "𝑥ₒ𝑠𝑖𝑛(𝜀) " , fontsize=10,horizontalalignment="right",verticalalignment="center")
        plt.text(0,5*np.sin(np.pi/6), "--", fontsize=8,horizontalalignment="center",verticalalignment="center")
        #plt.text(np.pi/3,5, "◂", fontsize=10,horizontalalignment="left",verticalalignment="center")
        #plt.text(7*np.pi/3,5, "▸", fontsize=10,horizontalalignment="right",verticalalignment="center")
        #plt.text(8*np.pi/6,5.2,r'$\mathrm{%s}$' % "𝑃𝑒𝑟𝑖𝑜𝑑", fontsize=11,horizontalalignment="center",verticalalignment="bottom")
                
        # xticks color white
        plt.xticks(color='w', )
 
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
                              }
        if c:
            self.function_list.update(c)
        self.plot_function()
        plt.savefig('x_vs_t.png', dpi=600)
        
    def plot_function(self):
        fx = str(self.fx)
        x_val = np.linspace(-0.1, 11.83, 1000000)
        self.function_list.update({"x":x_val})
        f = lambda x: eval(self.fx, {"__builtins__": None} , self.function_list)
        y_val = f(x_val)
        plt.plot(x_val, y_val, color="red", linewidth=1.1)
        #plt.show()
        
Plt(fx="5*sin(x+(pi/6))", xlabel="𝑡", ylabel="𝑥=𝑥ₒ𝑠𝑖𝑛(𝜔𝑡+𝜀)")