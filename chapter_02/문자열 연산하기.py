#1. 문자열 더해서 연결하기
head = "python"
tail = " is fun!"
print(head + tail)
# 'Python is fun!'

print("=" * 50)

#2. 문자열 곱하기
a = "python"
print(a * 5)

# multistring.py

#3. 문자열 곱하기 응용
print("=" * 50)
print("My Program")
print("=" * 50)

#4. 문자열 길이 구하기
a = "Life is too short"
print(len(a))

# -6 -5 -4 -3 -2 -1
# P  y  t  h  o  n 
# Life is too short, You need Python
# 0123456789

#문자열 인덱싱
a = "Life is too short, You need Python"
print("=" * 50)
print(a[3])
print("=" * 50)
print(a[0])
print("=" * 50)
print(a[12])
print("=" * 50)
print(a[-1])
print("=" * 50)
print(a[-0])
print("=" * 50)
print(a[-2])
print("=" * 50)
print(a[-5])
print("=" * 50)
print(a[-6])

#문자열 슬라이싱이란?
b = a[0] + a[1] + a[2] + a[3]
print("=" * 50)
print(b)

print(a[0:4])
print(a)

print(a[0:3])
print(a)

#문자열을 슬라이싱하는 방법
print(a[0:5])
print(a)
print(a[0:2])
print("=" * 50)
print(a)
print("=" * 50)
print(a[5:7])
print("=" * 50)
print(a)
print("=" * 50)
print(a[12:17])
print("=" * 50)
print(a)
print("=" * 50)
print(a[19:])
print("=" * 50)
print(a)
print("=" * 50)
print(a[:17])
print("=" * 50)
print(a)
print("=" * 50)
print(a[:])
print("=" * 50)
print(a)
print("=" * 50)
print(a[19:-7])
print(a)

#슬라이싱으로 문자열 나누기
a = "20010331Rainy"
date = a[:8]
weather = a[8:]
print(date)
print(weather)