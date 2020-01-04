#!/usr/bin/env python3
# -⏺- coding: utf-8 -⏺-
"""
Created on Sat Jan  4 18:15:06 2020

@author: shaxpy
"""
import threading
import random
import os
import time

tree=list(open('tree.txt').read().rstrip())
mutex=threading.Lock()

def color(color):
    if color=='red':
        return f'\033[91m⏺\033[0m'
    if color=='green':
        return f'\033[92m⏺\033[0m'
    if color=='yellow':
        return f'\033[93m⏺\033[0m'
    if color=='blue':
        return f'\033[94m⏺\033[0m'
    
    
    
def lights(color,indexes):
    off=True
    while True:
        for ids in indexes:
            tree[ids]=color(color) if off else '⏺'
        
        mutex.acquire()
        os.system('cls' if os.name == 'nt' else 'clear')
        print(''.join(tree))
        mutex.release()
        
        off=not off
        time.sleep(random.uniform(.5,1.5))

yellow=[]
red=[]
green=[]
blue=[]
for i,c in enumerate(tree):
    if c=='Y':
        yellow.append(i)
        tree[i]='⏺'
    if c=='R':
        red.append(i)
        tree[i]='⏺'
    if c=='G':
        green.append(i)
        tree[i]='⏺'
    if c=='B':
        blue.append(i)
        tree[i]='⏺'
        

ty=threading.Thread(target=lights,args=('yellow',yellow))
tr=threading.Thread(target=lights,args=('red',red))
tg=threading.Thread(target=lights,args=('green',green))
tb=threading.Thread(target=lights,args=('blue',blue))

for t in [ty,tr,tg,tb]:
    t.start()
for t in [ty,tr,tg,tb]:
    t.join()