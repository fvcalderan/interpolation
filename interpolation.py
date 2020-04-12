__author__ =    'Felipe V. Calderan'
__copyright__ = 'Copyright (C) 2020 Felipe V. Calderan'
__license__ =   'BSD 3-Clause "New" or "Revised" License'
__version__=    '1.0'

import numpy as np
import matplotlib.pyplot as plt
import sys
from sympy import *


def check_args():
    """check correctnes of the arguments and get them"""
    if len(sys.argv) != 4:
        print('\nUsage: python3 interpolate.py data precision output_name\n')
        exit()
    return sys.argv[1], float(sys.argv[2]), sys.argv[3]


def gen_data(data):
    """get csv file and generate axis"""
    my_data = np.genfromtxt(data, delimiter=',')
    x_axis, y_axis = zip(*my_data)
    return x_axis, y_axis


def gen_expr_point(point, x_axis):
    """generate x part of lagrange interpolation"""
    nstr = ''
    dstr = ''
    for i, v in enumerate(x_axis):
        if i != point:
            nstr = nstr + '(x-'+str(v)+')'+'*'
            dstr = dstr + '('+str(x_axis[point])+'-'+str(v)+')*'

    return '('+nstr[:-1]+')/('+dstr[:-1]+')'


def gen_final_expr(x_axis, y_axis):
    """generate final lagrange interpolation"""
    expr=''
    for i, v in enumerate(y_axis):
        this_point = gen_expr_point(i, x_axis)
        expr = expr + str(v) + '*' + this_point + '+'

    return expr[:-1]


def gen_new_axis(x_axis, expr, precision):
    """evaluate lagrange interpolation"""
    new_x = np.arange(min(x_axis), max(x_axis), precision)
    f = lambdify('x', expr, "numpy")
    new_y = f(new_x)

    return new_x, new_y


def gen_out_file(expr, x_axis, y_axis, new_x, new_y, out_name):
    """output equation and plot to files"""
    # save equation
    tfile = open(out_name+'_LaTeX.txt', 'w')
    tfile.write(latex(expr))
    tfile.close()

    # save plot 
    plt.plot(x_axis, y_axis, 'o', new_x, new_y, '-')
    plt.savefig(out_name, dpi = 400)


def main():
    # check correctness of the arguments and get them
    csvfile, precision, out_name = check_args()

    # generate data
    x_axis, y_axis = gen_data(csvfile)

    # simplify and generate new interpolated data
    expr = sympify(gen_final_expr(x_axis, y_axis))
    expr = simplify(expr)
    new_x, new_y = gen_new_axis(x_axis, expr, precision)

    # print expression in the terminal
    pprint(expr)

    # generate output
    gen_out_file(expr, x_axis, y_axis, new_x, new_y, out_name)


if __name__ == '__main__':
    main()
