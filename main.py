# Num 1
def num1fun():
    y = ((5+2-5)**2*5+8/2-30)/2*5-3
    return y

def num2fun():
    z = 5
    n = 3
    m = z-n
    y = (((z+2-n)**2*m+8/2-30)/2*5-3)**5+15*3-9/3
    return y

def num3fun():
    z = 5
    n = ((8+2-4)**2*5+8+7/2-30*5)/2*5-3;
    m = z**2*3+n;
    y = ((((z+2-n)**2*m+8/2-30)/2*5-3)**5+15*3-9/3)**2-5/4
    return y

# Num 2
def num1(p, v, t):
    return (p * v) / (0.37 * (t + 460))

def num2(age):
    return (200 - age) / 10

def num3(inv1, inv2, inv3):
    total = inv1 + inv2 + inv3
    porcentaje1 = inv1 * 100 / total
    porcentaje2 = inv2 * 100 / total
    porcentaje3 = inv3 * 100 / total
    return porcentaje1, porcentaje2, porcentaje3

def num4(balance):
    return balance + (balance * 0.015)

def num5(salary):
    law = salary * 0.01
    social_sec = salary * 0.04
    force_ins = salary * 0.005
    cash = salary * 0.05
    salary_end = salary - law - social_sec - force_ins - cash

    return law, social_sec, force_ins, cash, salary_end

def num6(num_words, tam, col):
    return (num_words * 20000) + (tam * 15000) + (col * 25000)

def num7(time):
    return 100000 + (120000 * (time - 1))

def num8(time_horas):
    descuento = (time_horas * 20000) * 0.05
    pago = time_horas * 20000 - descuento
    return pago, descuento

def num9(init, end):
    return (init - end) - ((init - end) * 0.2)

def num10(num_pics):
    return (num_pics * 1500) + ((num_pics * 1500) * 0.16)

def num11(amount):
    gynec =  amount * 0.4
    traumat = amount * 0.3
    pediac = amount * 0.3
    return gynec, traumat, pediac

def num12(num_movies, num_days):
    return ((num_movies - 1) * 1500) * num_days

def num13(n_personas, num_days):
    total = (n_personas * 25000) * num_days
    total_iva = total + total * 0.12
    return total_iva

def num14(num_days):
    return ((num_days - 1) * 200000) + 100000


