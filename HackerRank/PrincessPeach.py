#!/bin/python
def displayPathtoPrincess(n,grid):
    if grid[0][0] == 'p':
        moveLeft((n-1)/2)
        moveUp((n-1)/2)

    elif grid[0][n-1] == 'p':
        moveRight((n-1)/2)
        moveUp((n-1)/2)

    elif grid[n-1][0] == 'p':
        moveLeft((n-1)/2)
        moveDown((n-1)/2)

    elif grid[n-1][n-1] == 'p':
        moveRight((n-1)/2)
        moveDown((n-1)/2)

def moveLeft(n):
    i=0
    while i < n:
        print "LEFT"
        i+=1
def moveRight(n):
    i=0
    while i < n:
        print "RIGHT"
        i+=1
def moveUp(n):
    i=0
    while i < n:
        print "UP"
        i+=1
def moveDown(n):
    i=0
    while i < n:
        print "DOWN"
        i+=1




#print all the moves here
m = input()

grid = []
for i in xrange(0, m):
    grid.append(raw_input().strip())

displayPathtoPrincess(m,grid)
