## Lec7. Application and Tips

### Learning rate - Good and bad

> Learning rate의 값이 너무 높은 경우 오히려 Epoch 마다 Cost 값이 커지게 되는 현상이 발생할 수 있으며 (Over Shooting) 너무 작은 경우 너무 많은 시간이 소요되어 효율적인 학습이 이루어지지 않기 때문에 적절한 Learning Rate를 선정하는 것은 아주 중요한 부분이다.

### Learning rate decay

> 학습 특정 구간마다 Learning Rate 값을 재조정해가며 적절한 Learning rate를 찾는 기법을 말한다.
>
> ex) tf.train.exponential_decay, tf.train.inverse _time_decay

### Data Preprocessing - Feature Scaling

> Standardization ( 표준화 )
>
> > x값을 평균으로 뺀 값을 표준편차로 나눈다. (Mean Distance_평균과의 거리)
>
> Normalization
>
> > [0-1]사이의 데이터로 값을 변환

### Data Preprocessing - Noisy Data

> 범위 이상의 큰 데이터로 인해 깔끔하지 못한 데이터를 가지고 있을 때 전처리를 통해 정규화된 데이터를 만들어 낸다.
>
> 자연어처리의 경우 쓸모없는 조동사를 제거하고 핵심 어구만 남기는 전처리를 통해 데이터 학습에 최적화된 데이터를 만들어 낸다.
>
> 얼굴 이미지의 경우 머리스타일, 배경, 옷차림 등의 Noizy한 요소들을 제거하기 위한 전처리 과정을 통해 최적화된 데이터를 만들어 낸다.

### Overfitting

> '과적합' 이라는 의미로 학습이 반복될수록 Model이 가설에 과하게 맞춰 학습하는 경우로 Test Data가 입력되었을 때 오히려 정확도가 떨어져버리는 결과가 나타날 수 있다.
>
> > High bias (underfit) - 학습이 덜 된상태
> >
> > High variance(overfit) - 데이터에만 맞게 모델이 형성되는 경우_변화량이 많다.
>
> Set a Features
>
> > Get more Training data - 데이터 증량
> >
> > Smaller set of features - Feature(차원) 감소
> >
> > Add additional features - 의미를 가진 Feature 추가
>
> Regularization - Add term to loss
>
> > 학습 과정에서 Loss Function에서 Noizy 한 Weight를 정규화 함으로써 해결할 수 있다.

