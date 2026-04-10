# 딕셔너리 관련 함수
'''
{key : value}
'''

a = {
    'name' : 'hong',
    'age' : 20,
    'phone' : '010-1234-5678',
    'birth' : '1118'
}

# keys()
print(a.keys())
# dict_keys(['name', 'age', 'phone', 'birth'])

print(list(a.keys())) # ['name', 'age', 'phone', 'birth']

# values()
print(a.values())
# dict_values(['hong', 20, '010-1234-5678', '1118'])

print(list(a.values())) # ['hong', 20, '010-1234-5678', '1118']

# items() -> 키와 값의 묶음
print(a.items())
# dict_items([('name', 'hong'), ('age', 20), ('phone', '010-1234-5678'), ('birth', '1118')])

print(list(a.items()))
# [('name', 'hong'), ('age', 20), ('phone', '010-1234-5678'), ('birth', '1118')]
# items()로 나온 값들을 list로 담았더니 list 안에 튜플로 값이 담긴 구조가 됨.

# clear() : 아이템 삭제
a.clear()
print(a) # {}

a = {
    'name' : 'hong',
    'age' : 20,
    'phone' : '010-1234-5678',
    'birth' : '1118',
    'address' : '경기도 성남시 분당구'
}

# get() : key로 value 얻기
print(a.get('name'))
print(a['name'])

# 없는 키를 사용하면?
# print(a['address']) # error 발생
print(a.get('address')) # None

# get(key, default) -> key가 없을 때 [default]으로 반영.
print(a.get('address', '성남시 분당구')) # 경기도 성남시 분당구

# in 키워드 -> Key의 유무 판단으로 있으면 True, 없으면 False
print('name' in a) # True
print('zipcode' in a) # False

# 딕셔너리명.pop(Key, default) -> 딕셔너리 내에서 Key에 해당하는 값을 추출.
#                      원본 딕셔너리에서 해당하는 Key와 Value는 제거됨.
#                      없는 Key를 입력하면 지정했을 경우, default 값을 보여줌.
phone = a.pop('phone') # 010-1234-5678
print(phone)
print(a) # {'name': 'hong', 'age': 20, 'birth': '1118', 'address': '경기도 성남시 분당구'}

#
email = a.pop('email', '정보없음')
print(email)
print(a) # {'name': 'hong', 'age': 20, 'birth': '1118', 'address': '경기도 성남시 분당구'}