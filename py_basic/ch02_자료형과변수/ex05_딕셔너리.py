'''
# 시퀀스 타입 : 리스트[], 튜플() -> 순서(인덱스) 있음

# 맵핑 타입 : 딕셔너리{'K1':V1, V2, ... , 'K2':V01, ...}
             -> 원래는 순서(인덱스) 없었음, 파이썬 3.7+ 이후로 순서 보장

             딕셔너리의 Key는 기본적으로 문자열
'''
di1 = {
    'name' : 'hong',
    'age' : 30,
    'phone' : '010-1234-5678',
    'birth' : '1118'
}
print(di1)

# 딕셔너리 쌍{'Key' : Value} 추가하기
a = {1 : 'a'}

# 딕셔너리명[키] = 값
a[2] = 'b' # 인덱싱 방식으로 키와 값 추가
print(a) # {1: 'a', 2: 'b'}

a['name'] = 'hong'
print(a) # {1: 'a', 2: 'b', 'name': 'hong'}

a[3] = [1, 2, 3]
print(a) # {1: 'a', 2: 'b', 'name': 'hong', 3: [1, 2, 3]}

# 키(Key)를 사용하여 값(Value) 얻기
grade = {'pey':10, 'julliet':99}
print(grade['pey']) # 10
print(grade['julliet']) # 99

# 키는 중복될 수 없음.
# -> 같은 키를 지정하여 입력하면 마지막의 값으로 나타냄.
a = {1:'a', 1:'b', 1:'c'}
print(a[1]) # -> 'c'

# 리스트는 키로 사용 불가능
# a = {[1, 2]:'hi'} # error
# print(a)

# keys()
# values()
# items()