#25번
k = input().split()
v = map(int, input().split())
ky = dict(zip(k, v))
kys = {key: value for key, value in ky.items() if value != 30 and value != 60}
print(kys)

#26번
park = {'korean':94, 'english':91, 'mathematics':89, 'science':83}
print(park['english'])
print(park['science'])

#27번
kim = {'korean':94, 'english':91, 'mathematics':89, 'science':83}
kim.update(korean=100, english=100, mathematics=100, science=100)
print(kim)

#28번
lee = {'korean':94, 'english':91, 'mathematics':89, 'science':83}
print('english' in lee)
del lee['english']
print(lee)

#29번
lim = {'korean':94, 'english':91, 'mathematics':89, 'science':83}
print(lim.items())

#30번
choi = {'korean':94, 'english':91, 'mathematics':89, 'science':83}
choi = {key: value for key, value in choi.items() if value >= 90}
print(choi.keys())

#31번
yoo = {'korean':94, 'english':91, 'mathematics':89, 'science':83}
yv = yoo.values()
nn = sum(yv) / 4
print(nn)