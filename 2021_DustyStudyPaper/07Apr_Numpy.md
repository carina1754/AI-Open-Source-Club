*reference by http://pythonstudy.xyz/python/article/402-numpy-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0*
## Numpy
> 과학 계산을 위한 Library. 다차원 배열을 처리하는데 필요한 기능 제공.
---

1. Numpy 배열
- 배열은 동일한 type의 value를 가짐.
- 배열의 차원은 rank라 함.
- 각 차원의 크기를 tuple로 표기하는 것을 shape라 부름.<br>*2행 3열이면 rank=2 shape=(2,3), 10행 5열이면 rank=2 shape=(10,5)*

2. 생성방법
- python list 사용, numpy 제공 function 사용.

``` python
import numpy as np
 
list1 = [1, 2, 3, 4]
a = np.array(list1)
print(a.shape) # (4, ) 
 
b = np.array([[1,2,3],[4,5,6]])
print(b.shape) # (2, 3)
print(b[0,0])  # 1
```

- numpy 제공 function 사용.
    - zeros(): 해당 배열에 모두 0 대입.
    - ones(): 모두 1 대입.
    - full(): 배열에 사용자가 지정한 값 대입.
    - eye(): 대각선 1, 나머지 0인 2차원 배열 생성.

``` python
import numpy as np
 
a = np.zeros((2,2))
print(a)
# 출력:
# [[ 0.  0.]
#  [ 0.  0.]]
 
a = np.ones((2,3))
print(a)
# 출력:
# [[ 1.  1.  1.]
#  [ 1.  1.  1.]]
 
a = np.full((2,3), 5)
print(a)
# 출력:
# [[5 5 5]
#  [5 5 5]]
 
a = np.eye(3)
print(a)
# 출력:
# [[ 1.  0.  0.]
#  [ 0.  1.  0.]
#  [ 0.  0.  1.]]
 
a = np.array(range(20)).reshape((4,5))
print(a)
# 출력:
# [[ 0  1  2  3  4]
#  [ 5  6  7  8  9]
#  [10 11 12 13 14]
#  [15 16 17 18 19]]
```