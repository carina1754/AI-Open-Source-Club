## Lec7+. Data set, Learning, Sample

### Data sets

#### Training and Validation

> 전체 Data set 중 일정 비율의 데이터를 학습, 검증 파트로 나누어 새로운 Test 데이터에 대한 정확도를 높일 수 있다.

#### Good Case

>  Learning Rate 값을 최적의 값으로 찾는 과정, Optimizer의 종류의 변화 등 하이퍼파라미터 및 네트워크 구조를 바꿔가며 실제 우리가 원하는 모델을 찾기 위해 일련의 과정을 반복한다.

#### Evaluating a Hypothesis

> 어느정도 모델이 선정된 후에는 실제 데이터를 가지고 학습 및 테스트를 할 수 있게 되는데 또 다른 실제 데이터를 가지고 학습 및 구현하는 부분 또한 중요하다.

#### Anomaly detection

> 정상 데이터만을 학습한 모델을 가지고 비정상적인. 즉 Anomaly한 데이터가 입력되었을 때 이상 데이터를 감지하는 기법이다.

### Learning

#### Online Learning

> 데이터가 인터넷이 연결된 상태에서 학습하며 지속적으로 변하는 학습

#### Batch(Offline) Learning

> 고정된 데이터 자체가 Static한 상태로 학습(표를 참고)

#### Fine Tuning 

> 기존의 학습된 모델에 새로운 데이터를 추가 학습해 기존의 Weight 값을 미세 조정해 모델을 구성하는 것을 Fine Tuning이라 한다.

#### Feature Extarction

> 기존의 학습된 모델에 새로운 Task에 대해서만 새로 학습을 시켜 새로운 모델을 추가하는 방식을 Feature Extraction이라 한다.

#### Efficient Models

> 실제 여러 방법을 통해 모델을 만들었더라도 사용을 위해서는 효율적인 모델을 만들어야 하는데 최종적으로는 Inference time 을 최소화하고 모델의 Weight 값을 경량화 하는 것이 중요하다.
>
> 때문에 차원을 줄이는 것과 같이 여러 기법을 통해 모델의 속도를 높이는 것 또한 중요다하고 할 수 있다.