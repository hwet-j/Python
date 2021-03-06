import numpy as np

# 1) step1 : array 관련 문제
print(' 정규분포를 따르는 난수를 이용하여\n 5행 4열 구조의 다차원 배열 객체를 생성하고,\n 각 행 단위로 합계, 최댓값, 최소값을 구하시오.')
a = np.random.randn(20).reshape(5, 4)
print(a)
print('\n\n')
for i in range(len(a[:, 0])):
    print(i, '행 합계 : ', sum(a[i]), ' ', np.sum(a[i]))
    print(i, '행 최댓값 : ', max(a[i]), ' ', np.max(a[i]))

# 다른 방법
print(np.sum(a, axis = 1))  # 행단위 합계
print(np.max(a, axis = 1))

# 2) step2 : indexing 관련 문제
print('\n문2-1) 6행 6열의 다차원 zero 행렬 객체를 생성한 후 다음과 같이 indexing 하시오.')
b = np.zeros((6, 6))
print(b)

print('\n36개의 셀에 1~36까지 정수 채우기')
count = 1
for i in range(len(b[0])):
    for j in range(len(b[:, 0])):
        b[i][j] = count
        count = count + 1
print(b)

print('\n2번째 행 전체 원소 출력하기 ')
print('출력결과 : ', b[1])

print('\n5번째 열 전체 원소 출력하기')
print('출력결과 : ', b[:, 4])

print('\n15~29 까지 블럭으로 출력하기')
print(b[2:5, 2:5])

print('문2-2) 6행 4열의 다차원 zero 행렬 객체를 생성한 후 아래와 같이 처리하시오.')
print('조건1> 20~100 사이의 난수 정수를 6개 발생시켜 각 행의 시작열에 난수 정수를 저장하고\n, 두 번째 열부터는 1씩 증가시켜 원소 저장하기')
# 1. zero 다차원 배열 객체
c = np.zeros((6, 4))
print(c)

print()
# 2. 난수 정수 발생
for i in range(len(c[0])):
    c[:, 0] =  np.random.randint(20, 100, size=6)
print(c)

# 3. 두 번째 열부터는 1씩 증가시켜 원소 저장하기
print('\n')
for i in range(len(c[0]) - 1):
    c[:, i + 1] = c[:, i] + 1
print(c)


print('\n')
# 4. 첫 번째 행에 1000, 마지막 행에 6000으로 수정
c[0, :] = 1000
c[-1, :] = 6000
print(c)

# 3) step3 : unifunc 관련문제
print("\n표준정규분포를 따르는 난수를 이용하여 4행 5열 구조의 다차원 배열을 생성한 후\n\
아래와 같이 넘파이 내장함수유니버설 함수를 이용하여 기술통계량을 구하시오.\n\
배열 요소의 누적합을 출력하시오")
#d = np.random.normal(size=20).reshape(4, 5)
d = np.random.randn(4, 5)
print(d)
print('평균 : ', np.mean(d))
print('합계 : ', np.sum(d))
print('분산 : ', np.var(d))
print('표준편차 : ', np.std(d))
print('최댓값 : ', np.max(d))
print('최솟값 : ', np.min(d))
print('1사분위수: ', np.percentile(d, [25]))
print('2사분위수: ', np.percentile(d, [50]))
print('3사분위수: ', np.percentile(d, [75]))
print('요소값 누적합: ', np.cumsum(d))