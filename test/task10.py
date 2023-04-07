import operator

def deriv1(x1, x2, x3, x):
    return x1 * x**2 + x2 * x + x3


def deriv2(x1d, x2, x):
    return x1d * x + x2


def validate_precision(x1, x2, x3, x1d, x, itr): # Validate which minimum precision is applicable for the given equation
    
    p_list = dict()
    i = 0
    while i < itr:
        h = deriv1(x1, x2, x3, x) / deriv2(x1d, x2, x)
        x = x - h
        v = round(deriv1(x1, x2, x3, x), 4)
        p_list[x] = v
        i += 1
    x_p = min(p_list.items(), key=operator.itemgetter(1))
    return x_p


def cubic_equation_minimum(eqn, intv, eps, itr):

    # Parse the given equation to determine its derivatives
    equation_wo_spaces = eqn.replace(' ','')
    equation_wo_mult = equation_wo_spaces.replace('*','')
    eqn_list = list(equation_wo_mult)

    x1 = 3 * int(eqn_list[0])
    x2 = 2 * int(eqn_list[5])
    x3 = int(eqn_list[10])
    x1d = 2 * x1

    # Determine x: select a or b from the given interval
    x0 = int(intv[0])
    deriv3 = x1d
    if deriv1(x1, x2, x3, x0) * deriv3 > 0:
        x = int(intv[0])
    else:
        x = int(intv[1])

    # Validate precision
    x_p = validate_precision(x1, x2, x3, x1d, x, itr)
    p = x_p[1]
    xn_p = x_p[0]

    # Algorithm
    if eps < p:
        print(f"Given precision is not applicable for the derivative of the given equation, the minimum precision is {p}")
    else:
        if eps == p:
            x_res = xn_p
        
        elif eps > p:
            x_list = []
            while abs(deriv1(x1, x2, x3, x)) > eps:
                h = deriv1(x1, x2, x3, x) / deriv2(x1d, x2, x)
                x = x - h
                x_list.append(x)
                xn = x
            h = deriv1(x1, x2, x3, xn) / deriv2(x1d, x2, xn)
            x_res = x - h

        xf1 = int(eqn_list[0])
        xf2 = int(eqn_list[5])
        xf3 = int(eqn_list[10])
        xf4_1 = eqn_list[-2]
        xf4_2 = eqn_list[-1]
        xf4 = int(xf4_1 + xf4_2)
        
        equation_min = round(xf1 * x_res ** 3 + xf2 * x_res ** 2 + xf3 * x_res + xf4, 4)
        print(f"x = {x_res},\nmin: {equation_min}") # x value was printed to simplify result analysis
    

cubic_equation_minimum('3*X^3 + 4*X^2 +5*X + 21', [-3, 3], 4, 10)
# cubic_equation_minimum('3*X^3 + 4*X^2 +5*X + 21', [-3, 3], 3, 10)