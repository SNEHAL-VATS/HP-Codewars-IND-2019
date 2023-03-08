"""
Problem 3 +4
Higher Powers Points

Summary:
Surya,a 7th standard student is playing simple math game with
his twin sister Tanya. The game is about one person telling 2
integers (N & K) and the other having to reply with "Yes" or "No"
depending on whether N i sa power of K. As the questions are
getting harder to calculate mentally, help Surya and Tanya write
a program to do this calculation quickly.

Input:
The input consists of a single line N and K positive numbers separated by space.

Output:

If N is a power of K, print Yes other wise print No

Constraints

0<N,K <106
Sample Input#1
9 3
Sample Output#1
Yes
Sample Input#2
25 4
Sample Output#2
No
"""
n,k=map(int,input().split())
while n>1:
    n/=k
print("Yes" if n==1 else "No")
