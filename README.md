# get_random.py

## function get_zero_or_one()
  - 파이썬의 random 모듈 사용해서 0 or 1 출력.
  
## function get_random(N)

### 1. 10진수 N을 2진수로 변환해서 최대 자리수(2진수 기준) 구하기.

```python
max_bin = ""
while num >= 1:
  if num == 1:
    max_bin = "1" + max_bin
    break
  num, left_num = num // 2, num % 2
  max_bin = str(left_num) + max_bin
```

__example__ <br/>
if N == 5 이라면 N의 2진수는 101 <br />
그래서 최대 랜덤수의 최대 2진수형 자리수는 세자리 수.

### 2. 1번 값 자리수만큼의 length를 지닌 Array 생성.

### 3. Array length만큼 get_zero_or_one() 호출.

```python
random_bin_elements = [get_zero_or_one() for _ in range(len(max_bin))]
```

### 4. 3번 Array의 element들로 2진수 만든 뒤 10진수로 변환.

```python
decimal = 0
for i in range(len(random_bin_elements[::-1])):
  if random_bin_elements[i] == 1:
    decimal += (2**i)
```

### 5. 4의 값이 N보다 크면 다시 3번으로. N보다 작다면 해당 값 반환.

<br />

# get_random_test.py
1. 각 테스트케이스마다 maxNum(get_random()의 인자값)값과 testRange(랜덤 수 생성 정도)값 생성
2. get_random(N)의 값을 testRange 값만큼 담고 있는 __testData => type : list__ 생성
3. testData의 각 element의 count값을 담고 있는 __testDataCounter => type : dictionary__ 생성
4. testData의 가장 큰 값이 maxNum보다 크지 않은지 테스트.
5. testData의 가장 작은 값이 0보다 작지 않은지 테스트.
6. testDataCounter의 가장 큰 value값이 전체의 절반이 넘어가지 않는지 테스트.
