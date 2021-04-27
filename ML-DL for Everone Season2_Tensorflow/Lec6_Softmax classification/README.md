## Lec6. Softmax Classification Multinomial Classification

### 1. Multinomial Classification

> 세 가지 class(A, B, C)로 나누는 다중 분류 문제를 다루면 다음과 같은 독립된 classified가 세 개 나온다.
>
>   a. A or Not
>
>   b. B or Not
>
>   c. C or Not

### 2. Matrix implementation

> 위 독립된 machine을 각각 구현하게 되면 문제가 상당히 길고 복잡해지기 때문에 행렬로 구현해 문제를 단순화 시킨다.

### 3. Softmax란?

> 이전에 sigmoid를 통과한 뒤의 값은 [0 ~ 1]의 값을 가지게 되는데 이를 위의 예시와 같이 3가지 class로 분류한다고 하면 각각의 case가 나올 확률값으로 나오게 되는데 이를 Ont-Hot Encoding해 어떤 Case가 나올지 예측하는 기법이다.

### 4. Cost Function - Cross Entropy

> Softmax를 위해 정의된 Cost 함수는 사실상 이전에 배웠던 Logistic Cost Function과 같은데 이를 여러 class에 적용하기 위해 다음과 같이 정의한다.
> $$
> D(S,L) = -\sum\limits_{i}L_ilog(S_i)
> $$

### 5. Optimization

> 최적화 함수는 다른 회귀문제와 같은 Gradient Descent 알고리즘을 사용한다.

