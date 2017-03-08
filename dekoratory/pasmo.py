#!/usr/bin/python
# Copyright (C) 2017 Michał Nieznański
"""
Demonstarcja dekoratorów
"""

class dekclass:
    def __init__(self, f):
        self.f = f
    def __call__(self, *args, **kwargs):
        print("class Start")
        print(args)
        self.f(*args, **kwargs)
        print("class Stop")


def deko(f):
    """
    Wypisuje "Start" przed wywołaniem i "Stop" po wywołaniu
    funkcji.
    """
    def new_f(*args, **kwargs):
        print("Start")
        f(*args, **kwargs)
        print("Stop")
    return new_f

class Pasmo:
    def __init__(self, a, *args, **kwargs):
        self.a = a
        self._args = args # niepubliczne
        self._kwargs = kwargs

    @classmethod
    def f(cls):
        print(cls, "f")

    @staticmethod
    def g():
        print("g")

    @deko
    def h(self):
        print(self, "h")

def f(a,b):
    print(a,b)

@dekclass
def f(a):
    print(a)

if __name__ == "__main__":
    Pasmo.f()
    Pasmo(1).f()

    Pasmo.g()
    Pasmo(2).g()

    #Pasmo.h()
    Pasmo(3).h()

    f(1)
