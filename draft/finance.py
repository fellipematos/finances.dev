#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## FINANCE$.dev
## Tem como funcionalidade controlar seus gastos
## Author: Fellipe Matos
## Page: fellipematos.github.io/myportifolio
## E-mail: box.fellipematos@gmail.com.br

from controls import *

#Inicia Cabecalho
header = "FINANCE$.dev\nGerencie seus gastos"
print(header)

#Inicia Menu Principal
menu()
user = int(input("--> "))

while True:

    if user == 1:
        newTransaction()
        menu()
        user = int(input("--> "))

    if user == 2:
        showTransaction()
        menu()
        user = int(input("--> "))
    
    if user == 3:
        removeTransaction()
        menu()
        user = int(input("--> "))
    
    if user == 4:
        extract()
        menu()
        user = int(input("--> "))

    if user == 5:
        report()
        menu()
        user = int(input("--> "))

    if user == 0:
        resetTransaction()
        menu()
        user = int(input("--> "))
    
    if user == 9:
        close()
