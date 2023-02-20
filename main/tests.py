from django.test import TestCase

# Create your tests here.

import multiprocessing as mp

def calc1(num):
    res = []
    for n in range(num):
        print(n)

def calc2(num):
    res = []
    for n in range(num):
        print(n*10)

def calc3(num):
    res = []
    for n in range(num):
        print(n*100)

p1 = mp.Process(target=calc1, args=(9, ))
p2 = mp.Process(target=calc2, args=(9, ))
p3 = mp.Process(target=calc3, args=(9, ))
