# py05_10_hw

## 강의노트#5 10주차 과제

## 파일 구성

a.py : 여러 문제를 모은 파일
README.md : 설명 문서

25번
p.6 p.28 참고

표준 입력:
alpha bravo charlie delta echo foxtrot golf
30 40 50 60 70 80 90

    k = input().split()
    v = map(int, input().split())
    ky = dict(zip(k, v))
    kys = {key: value for key, value in ky.items() if value != 30 and value != 60}
    print(kys)

키의 값은 문자열, 벨류의 값은 정수로 변환하여 받음.
zip 방법을 사용하여 딕셔너리로 만들었음.
딕셔너리 표현식을 사용하여 30과 60의 값을 제외하여 출력함.

26번
p.11 참고

    park = {'korean':94, 'english':91, 'mathematics':89, 'science':83}
    print(park['english'])
    print(park['science'])

변수명[]을 사용하여 원하는 키에 접근함.

27번
p.18-19 참고

    kim = {'korean':94, 'english':91, 'mathematics':89, 'science':83}
    kim.update(korean=100, english=100, mathematics=100, science=100)
    print(kim)

update를 사용하여 키-값을 수정하고 출력함.

28번
p.14 p.22-23 참고

    lee = {'korean':94, 'english':91, 'mathematics':89, 'science':83}
    print('english' in lee)
    del lee['english']
    print(lee)

in 연산자를 사용하여 특정 키가 있는지 확인함.
del를 사용하여 특정 키를 삭제함.

29번 p.28

    lim = {'korean':94, 'english':91, 'mathematics':89, 'science':83}
    print(lim.items())

items를 사용하여 키-값 모두 출력함.

30번 p.35 p.28

    choi = {'korean':94, 'english':91, 'mathematics':89, 'science':83}
    choi = {key: value for key, value in choi.items() if value >= 90}
    print(choi.keys())

딕셔너리 표현식을 사용하여 90점 이상을 출력함.
keys을 사용하여 키만 출력함.

31번

    yoo = {'korean':94, 'english':91, 'mathematics':89, 'science':83}
    yv = yoo.values()
    nn = sum(yv) / 4
    print(nn)

sum 함수를 사용하여 합계를 구하고, 4와 나누어 평균을 계산함.
