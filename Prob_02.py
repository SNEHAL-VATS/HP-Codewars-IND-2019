"""Problem2 (+4 Points)
Match nuts with bolts

Wooden toy contains many nuts and bolts which are of
different sizes and shapes. To assemble the toy, he
needs to pair the nuts with the matching bolts.
Write a program to help Tony match the nuts with bolts.
Each nut is represented by a unique alphabet within the alphabet range A to Z. Each corresponding bolt
is represented by numbers from 1to26. For e.g. the nut A matches to bolt 1.

Input:

The first line contains the number of nuts and bolts N.The second line contains alphabets A1,Az..An
separated by spaces denoting the nuts.The third line contains numbers B1,B2...Bn separated by spaces
denoting the bolts.

Output:

Print the bolts in one line separated by spaces in the order matching the nuts specified in the input. If any
bolt does not match with the nut print "Could not match nuts to bolts."

Constraints

0<N<27

Sample Input#1
9
AX Y B DE F IU
9 6 21 5 4 2 1 25 24
Sample Output #1
1 24 25 2 4 5 69 21
Sample Input#2
6
U JMH T F
10 21 5 6 12 14
Sample Output #2
Could not match nuts to bolts
"""
n=int(input())
ans=''
h=True
if 0<n<27:
    x=input().split()
    y=input().split()
    if len(x)==len(y)==n:
        for i in x:
            if str(ord(i)-64) in y:
                ans+=str(ord(i)-64)+' '
            else:
                h=False
                break
    else:
        print('Could not match nuts to bolts')
else:
    print('Could not match nuts to bolts')
if h:
    print(ans)
else:
    print('Could not match nuts to bolts')
