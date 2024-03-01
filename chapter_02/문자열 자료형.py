# 1. 큰따옴표(")로 양쪽 둘러싸기
print("Hello world")

# 2. 작은따옴표(')로 양쪽 둘러싸기
print('python is fun')

# 3. 큰따옴표 3개를 연속(""")으로 써서 양쪽 둘러싸기
print("""Life is too short, You need python""")

# 4. 작은따옴표 3개를 연속(""")으로 써서 양쪽 둘러싸기
print('''life is too short, You need python''')

#문자열 안에 작은따옴표나 큰따옴표를 포함시키고 싶을 때

# 1. 문자열에 작은 따옴표 (') 포함시키기
print("Python's favorite food is perl")

# 2. 문자열에 큰따옴표(") 포함시키기
print('"Python is very easy." he says.')

# 3. 백슬래시(/)을 사용해서 작은따옴표(')와 큰따옴표("")를 문자열에 포함시키기
print('Python\'s favorite food is perl')
print("\"Python is very easy.\" he says.")

#여러 줄인 문자열에 변수에 대입하고 싶을 때

# 1. 줄을 바꾸는 이스케이프 코드 '\n' 삽입하기
multiline = "Life is too short\nYou need python"
print(multiline)

# 2. 연속된 작은 따옴표 3개(''') 또는 큰따옴표 3개(""") 사용하기
multiline='''
Life is too short
You need python
'''
print(multiline)