#25
keys = input('alpha bravo charlie delta echo foxtrot golf를 입력').split()
values = list(map(int, input('30 40 50 60 70 80 90을 입력').split()))
data = dict(zip(keys, values))

del data['alpha']
del data['delta']

print(data)

#26
park = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}

print(park['english'])
print(park['scinece'])

#27
kim = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}
kim.update(korean = 100, english = 100, mathematics = 100, science = 100)

print(kim)

#28
lee = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}
if 'english' in lee:
    del lee ['english']
    print('"english"를 삭제.')
else:
    print("'english'가 없음.")

print('결과는:', lee)

#29
lim = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}
print(lim.items())

#30
choi = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}
x = {key: value for key, value in choi.items() if value >= 90}

print(x.keys())

#31
yoo = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}
scores = yoo.values()
total = sum(scores)
count = len(scores)

average = total / count

print(average)