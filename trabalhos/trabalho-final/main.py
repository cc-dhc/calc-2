import math

data = {
    0: (0, 128.67, 0.00),
    1: (1, 133.65, 0.00),
    2: (2, 124.40, 0.00),
    3: (3, 115.03, 0.00),
    4: (4, 109.22, 0.00),
    5: (5, 109.78, 0.00),
    6: (6, 117.20, 29.29),
    7: (7, 129.38, 90.34),
    8: (8, 142.73, 252.00),
    9: (9, 153.92, 292.27),
    10: (10, 161.33, 369.14),
    11:(11, 165.52, 189.42),
    12:(12, 168.37, 173.83),
    13:(13, 171.61, 323.57),
    14:(14, 175.59, 439.09),
    15:(15, 179.00, 344.66),
    16:(16, 179.76, 279.28),
    17:(17, 176.43, 270.96),
    18:(18, 169.26, 157.72),
    19:(19, 160.28, 57.73),
    20:(20, 152.23, 2.50),
    21:(21, 147.04, 0.00),
    22:(22, 144.69, 0.00),
    23:(23, 143.30, 0.00)
}

def func(x: float):
    return math.sin(x)

def meu_simpsons_i(li: float, ls: float, func):
    h = (ls - li) / 2.0

    return (1/3.0) * h * (func(li) + 4*func(h) + func(ls))

# Function for approximate integral 
def simpsons_(ll, ul, delta_x, func, round_h=False): 
  
    # Calculating the value of h 
    h = ( ul - ll )/delta_x

    if round_h: h = int(h)
  
    # List for storing value of x and f(x) 
    x = list() 
    fx = list() 
      
    # Calculating values of x and f(x) 
    i = 0
    while i<= delta_x: 
        x.append(ll + i * h) 
        fx.append(func(x[i])) 
        i += 1
  
    # Calculating result 
    res = 0
    i = 0
    while i<= delta_x: 
        if i == 0 or i == delta_x: 
            res+= fx[i] 
        elif i % 2 != 0: 
            res+= 4 * fx[i] 
        else: 
            res+= 2 * fx[i] 
        i+= 1
    res = res * (h / 3) 
    return res 

def func_load_1(t: int) -> float:
    return data[t][1]

def func_supply_1(t: int) -> float:
    return data[t][2]

def func_load_2(t: float) -> float:
    return (142.8 - 19.39*math.cos(2*math.pi*t/24) - 17.03*math.sin(2*math.pi*t/24) 
            + 4.56*math.cos(4*math.pi*t/24) - 3.80*math.sin(4*math.pi*t/24)
            + 5.15*math.cos(6*math.pi*t/24) - 0.93*math.sin(6*math.pi*t/24))

def func_supply_2(t: float) -> float:
    if t < 5 or t > 18: return 0
    else: return (151.7 - 212.8*math.cos(2*math.pi*t/24) + 31.45*math.sin(2*math.pi*t/24) 
                + 57.48*math.cos(4*math.pi*t/24) + 8.61*math.sin(4*math.pi*t/24)
                + 36.5*math.cos(6*math.pi*t/24) - 0.89*math.sin(6*math.pi*t/24))

if __name__ == "__main__":
    res_deltax_1 = simpsons_(0, 23, 23, func_supply_1, round_h=True) - simpsons_(0, 23, 23, func_load_1, round_h=True)
    res_deltax_2 = simpsons_(0, 23, 12, func_supply_1, round_h=True) - simpsons_(0, 23, 12, func_load_1, round_h=True)
    res_smoothed = simpsons_(0, 23, 100, func_supply_2) - simpsons_(0, 23, 100, func_load_2)

    print("Prejuízo (delta x = 1):\t\tA$ {:.2f}".format(res_deltax_1))
    print("Prejuízo (delta x = 2):\t\tA$ {:.2f}".format(res_deltax_2))
    print("Lucro (funções suavizadas):\tA$ {:.2f}".format(res_smoothed))