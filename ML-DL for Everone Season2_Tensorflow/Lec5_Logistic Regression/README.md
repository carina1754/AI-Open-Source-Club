## Lec5. Logistic Regression

### 1. Type of Logistic Classification

> a. Exam : Pass or Fail
>
> b. Spam : Not Spam or Spam
>
> c. face : Real or Fake
>
> d. Tumor : Not Malignant or Malignant
>
> ( 머신러닝을 위해 [0, 1]로 One Hot )

### 2. Logistic vs Linear

> a. Logistic Regression
>
> - 구분선을 통해 두 개의 케이스를 구분
> - ex) Y = [[0], [0], [1], [1]]         # One Hot
>
> b. Linear Regression
>
> - 연속적인 데이터 즉, 선 인근의 데이터를 예측한다.
> - ex) Y = [823, 833, 819 ,834, 852]        # Numeric

### 3. Hypothesis Representation

> a. 두 가지 class로 구분하기 위해 [0, 1]로 나누기 위한 새로운 가설이 필요.
>
> b. [ X ] -> [ Linear Function ( Y = Wx + b )] -> [ Logistic Function ( 1 >= Y >= 0) ] -> [ Decision Boundary ( > 0.5 )] -> [ Y ( 1, 0 )]

### 4. Cost Function

> a. Cost를 줄임으로써 Weight를 최적의 값으로 맞추기 위한 함수
>
> b.  실제 모델이 예측을 가장 잘 해냈을 때 Cost 값은 최소화

### 5. Optimization