a = 123456789012
b = 98765432101

def gcd(a, b):#上週教過韓式的定義
  print(a, b)#想看過程所以把a,b印出來
  if a == 0: return b#終止條件 遇到0的話另一邊就是答案
  if b == 0: return a#終止條件 遇到0的話另一邊就是答案
  return gcd(b, a%b)

ans = gcd(a, b)#問gcd()函式看答案是甚麼
print(ans)