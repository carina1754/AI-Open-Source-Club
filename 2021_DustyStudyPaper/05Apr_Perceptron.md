# Perceptron

> ## <u>Basic Rule</u>
각각 weight을 가지는 input들이 입력되고,

input들을 weight과 연결하여 임계치를 넘으면, 1 아니면 -1로 출력한다. (z>=0일 때, 1 아니면 0을 반환하는 단위 계단 함수를 변형함.)

1. 초기 weight은 0 혹은 랜덤한 작은 수로 설정.
2. 각 training ssample에서 output을 계산 -> weight update를 수행한다.

- _모든 학습 데이터를 정확히 분류할 때까지 반복하므로, 선형적 분리에 적합한 Algorithm이다._

- _기계 학습 분야에서는 모델의 과적합을 주의할 것. 모든 Data를 대입해도 general하게 작동 되어야 한다._

> ## <u>Bias</u>
input+weight가 넘어야하는 임계값... 높을수록 그 model의 분류는 엄격하다. 그렇기에 model은 단순화된다. 분류가 적어지니까...
-> 과소적합(underfitting) 위험성 증가.

반면, 허용성이 증가되면 (bias 감소) model이 복잡해지고, 허용범위가 넓어진다. 때문에 noise가 생길 가능성이 증가함.

이 때문에, noise를 얼마나 잘 거르는지에 대한 연구가 필요하다.

### *weight= 가중치. input이 어느 정도 output에 영향을 미치는지? || bias= perceptron이 얼마나 쉽게 활성화되는가?*

> ## 한계점
비선형 분류는 불가하다. 다층 perceptron으로 해결.