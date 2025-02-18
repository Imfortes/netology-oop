# Преобразование RGB в шестнадцатеричный формат
# 255, 255, 300 --> "FFFFFF"
def rgb(r, g, b):
    def clamp(n):
        return max(0, min(255, n))
    return ''.join(list(f'{clamp(value):02X}' for value in [r, g, b]))

def rgb(r, g, b):
    round = lambda x: min(255, max(x, 0))
    return ("{:02X}" * 3).format(round(r), round(g), round(b))

def rgb(r, g, b):
    clamp = lambda x: max(0, min(x, 255))
    return "%02X%02X%02X" % (clamp(r), clamp(g), clamp(b))

# print(rgb(155, 125, 5))

# 
# 
# def remainder(a,b):
#     if min(a, b) == 0:
#         if a == 0 and b == 0: 
#             return None
#         elif a == 0: 
#             return None
#         elif b == 0:  
#             return 0
    
#     larger = max(a, b)
#     smaller = min(a, b)
#     return larger % smaller
        
    
# print(remainder(0, -1))
# print(remainder(1, 0))
# print(remainder(-13, -13))
# print(remainder(-60, 340))

def sum_str(a, b):
    a = 0 if a == '' else int(a)
    b = 0 if b == '' else int(b)
    return a + b

# print(sum_str('4', '5'))
# print(sum_str('9', '0'))
# print(sum_str("",""))

def row_weights(array):
    return tuple((sum(array[::2]), sum(array[1::2])))

    
# print(row_weights([80]))
# print(row_weights([100,50]))
# print(row_weights([50,60,70,80]))
# print(row_weights([13,27,49]))
# print(row_weights([39,84,74,18,59,72,35,61]))

def say_hello(name, city, state):
    return (f'Hello, {" ".join(name)}! Welcome to {city}, {state}!')

# print(say_hello(['Marlo','Stanfield'],'Baltimore','Maryland'))