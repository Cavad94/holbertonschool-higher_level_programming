#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Hər iki tuple-ı genişləndiririk ki, ən azı 2 elementi olsun
    # Əgər element varsa, özünü götürür, yoxdursa 0 əlavə edir
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)
    
    # Yalnız ilk iki elementi toplayırıq
    result = (a[0] + b[0], a[1] + b[1])
    
    return result
