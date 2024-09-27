'''
4) A fruit seller buys a dozen of banana at Rs.X. He sells 1 banana at Rs.Y. Write a program to determine the profit or loss in Rs. for the fruitseller.
Input format:
Input consists of 2 floating point numbers
The first input corresponds to the total cost(X)
The second input corresponds to the sold cost(Y)
Output format:
Print "Profit or Loss" with Rupees.
Sample Input:
60
4
Sample Output:
Loss : Rs.12.00
'''

Answer::

import math
x=float(input())
y=float(input())
b=12*y

if(b<x):
    print('loss is:',x-b)
else:
    print('profit is:',b-x)

Output:
60
4
loss is: 12.0
