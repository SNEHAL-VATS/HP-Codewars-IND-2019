"""SUMMARY 

Mathematics teacher gave Srinath an assignment to determine the difference between the original number 
and its reverse. Can you write a program to help Srinath complete his assignment?

Input:
  Any positive number N
Output:
  Print the signed difference between the number and its reverse

Sample Input 1:
321
Sample output 1:
198

Sample Input 2:
125
Sample output 2:
-396
"""

def p1():
    N=input()
    return int(N)-int(N[::-1])
print(p1())
