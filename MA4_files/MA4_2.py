# #!/usr/bin/env python3

from person import Person
from time import perf_counter as pc
from numba import njit
import matplotlib.pyplot as plt



@njit
def fib_numba(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_numba(n-1) + fib_numba(n-2)
    

def fib_py(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_py(n-1) + fib_py(n-2)



def main():
    y_py = []
    y_num = []
    y_per = []
    x_vals = list(range(20,25))
    f = Person(10)
    for x in x_vals:
        start_py = 0
        stop_py = 0 
        
        start_num = 0
        stop_num = 0
        
        start_per = 0
        stop_per = 0
        
        start_py = pc()
        fib_py(x)
        stop_py = pc()
        
        y_py.append(stop_py-start_py)

        start_num = pc()
        fib_numba(x)
        stop_num = pc()
        
        y_num.append(stop_num-start_num)
        
        f.setAge(x)
        start_per = pc()
        f.fib()
        stop_per = pc()
		
        y_per.append(stop_per-start_per)



    plt.scatter(x_vals, y_num, label='Numba', color='blue', marker='.')
    plt.scatter(x_vals, y_py, label='Just python', color='red', marker='.')
    plt.scatter(x_vals,y_per, label = "C++", color = 'green', marker = '.')
    plt.xlabel('N')
    plt.ylabel('Time')
    plt.title('Time for fib')
    plt.legend()
    plt.savefig('myplot.png')

if __name__ == '__main__':
	main()


