"""
Print Number Pyramid
Send Feedback
Print the following pattern for a given n.
For eg. N = 6
123456
  23456
    3456
      456
        56
          6
        56
      456
    3456
  23456
123456
Sample Input 1 :
4
Sample Output 1 :
1234
  234
    34
      4
    34
  234
1234
"""

n=int(input())
for i in range(1,n+1):
    for j in range(1,i):
        print(" ",end="")
    for l in range(i,n+1):
        print(l,end="")
    print()
for a in range(1,n):
    for s in range(n-1-a,0,-1):
        print(" ",end="")
    for k in range(n-a,n+1):
        print(k,end="")
    print()