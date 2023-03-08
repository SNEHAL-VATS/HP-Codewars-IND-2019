"""
Problem 4 +4 Points

Find a Number

Summary
Drithi and Jivika are playing with numbers during the summer
time. Both are very good at number games but they place a bet on 
finding out the answer in the least amount of time. The game  
involves knowing basic mathematics like Highest common factor
(HCF) and Least Common Multiple(LCM) of two numbers. If HCF
and LCM of two numbers are given and one of the numbers is provided, find out the other number.
Highest Common Factor (HCF) oftwo numbers isthegreatestnumber thatdivideseach ofthem exactly.
Least Common Multipl(eLCM) is the lowest number which is exactly divisible by each one of the given
numbers.
Can you beat Drithi and jivika by writing a program to find the second number given HCF, LCM and one of
the number?

Input

A singlelinecontainsthe HCF H,LCML and number A separated by space.

Output

Print he second number.

Constraints
0<A,H,L<106
Sample Input#1
13 1989 117
Sample Output#1
221
Sample Input#2
8 6784 128
Sample Output#2
424
"""
h,l,a=map(int,input().split())
print(h*l//a)
