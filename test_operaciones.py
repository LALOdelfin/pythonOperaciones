#Pruebas unitarias de la funcion sumar
import pytest
from operaciones import *

def test_sumar1():
    res=sumar([1,2,3,4,5])
    assert res==15

def test_sumar2():
    res=sumar([-1,-2,-3,-4,-5])
    assert res==-15

def test_sumar3():
    res=sumar([0,0,0,0])
    assert res==0

def test_promediar1():
    res=promediar([10,20,30,40])
    assert res==25

