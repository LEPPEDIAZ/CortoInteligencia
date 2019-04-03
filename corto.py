import numpy as np

from scipy.misc import derivative

from matplotlib import pyplot as plt


def function_f(x1,x2,x3): 

    return x3*(1+x1**2/x2**2)**(-1.0/2)

def Copiar_puntos(func, index, puntos):

    puntos_copy = puntos[:]

    def as_func_of(x):     

        puntos_copy[index] = x 

        return func(*puntos_copy) 

    return derivative(as_func_of, puntos[index], dx = 1e-6) 



x1_list = np.linspace(-2,2,100)

x1_value = x1_list[74] 

x2_constant = 0.05

x3_constant = 0.75 





delx1_value = Copiar_puntos(function_f, 0, [x1_value, x2_constant, x3_constant])

delx1_list = Copiar_puntos(function_f, 0, [x1_list, x2_constant, x3_constant])

delx2 = Copiar_puntos(function_f, 1, [x1_list, x2_constant, x3_constant])




plt.plot(x1_list, delx1_list)

plt.plot(x1_list, delx2)

plt.show()

