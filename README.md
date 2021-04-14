# AI-Open-Source-Club
## AI Open Source Club for Yonsei Mirae Campus

### How to study Machine Learning

### What is Machine Learning?
 
위키피디아에 따르면 머신러닝은 "경험을 통해 자동으로 개선하는 컴퓨터 알고리즘의 연구" 라고 정의한다. 쉽게 접근하면 "특정 알고리즘을 기계가 스스로 
학습하게 만드는 것"이라 이해할 수 있다. 조금 더 풀이하면 우리가 생각하는 방식을 컴퓨터가 "최대한"비슷하게 모방할 수 있도록 훈련 시켜주는 것이 바로
머신러닝이다. 이러한 훈련을 마치면 나중에는 컴퓨터 스스로 알고리즘을 구현할 수 있게 되고, 이게 AI, 즉 인공지능이 시작되는 시점이다. 구체적으로 
머신러닝은 컴퓨터에게 어떤 방식으로, 무엇을 목표로 학습을 진행할지 인간이 '안내'해주는 것이라 생각하면 이해하기 수월할 것이다.(사실 나도 아직 모르겠다..)
그럼 이제부터 컴퓨터를 어떻게 교육시킬지, 무엇을 목표로 학습을 진행할지 알아볼건데!! 이 일련의 과정에서 머신러닝의 3가지의 중요한 수학적 모델이 등장한다!

#### 1. Linear Regression(선형회귀)

선형회귀란 "변수 사이의 선형적인 관계를 모델링한 것"이라고 하는데..(벌써 머리 아프다) 그냥 필자가 이해한 건 특정 데이터들의 관계를 그래프로 표현했을 때,
가장 직관적으로 알아보기 쉬운 선을 찾고 분석하는 것이 바로 "선형회귀"라 이해했다. 선형회귀의 중요성은 머신러닝의 근본 취지??이기도 한데, 결국 머신러닝에서
"학습을 시킨다?"라는 말은 컴퓨터한테 데이터를 던져주고 스스로 가장 합리적인 '선'을 찾게 한다는 것이다.(후...) 아래와 같은 일차방정식을 하나 보자.
<pre>
<code>
H(x) = Wx + b
</code>
</pre>
이 식에서 눈여겨 봐야 할 두 녀석이 있다
* W(Weight) = 가중치
* b(bias) = 편향

위에서 컴퓨터가 무엇을 목표로 학습을 진행할지 말했는데, 바로 이 2개다! 기울기와 y절편에 해당하는 가중치와 편향을 컴퓨터가 찾도록 교육을 시키는 것이 머신러닝의 
목표인 것이다. "컴퓨터야~~ 너가 W하고 b를 좀 찾아봐~!" 하면서 교육을 시키는 것이다. 그니까 선형회귀는 가중치와 편향을 계속 수정해 나가면서 가장 합리적인 일차방정식을 
찾아내는것!이라 이해하자! 다시 정리하면 학습 데이터를 가지고 세워본 가설식이 실제로 가장 합리적인 식이 될 수 있도록 계속해서 식을 수정해 나가고, 변경해가는 과정이 
"선형회귀법"을 이용한 머신러닝의 가장 핵심개념이라 할 수 있다.(흐아..) 그럼에도 불구하고 아무리 이놈의 컴퓨터가 학습을 많이 해도 '완벽한'식을 찾아내지는 못한다ㅠ 결론은
인간인 우리가 예측한 값과 가장 근사한 값을 찾아내는 것이다. 그럼 여기서 또 의문이 든다. 저 가중치와 편향은 어떤 기준으로 예측을 해야 되는 것일까? 아래의 loss function과
gradient descent를 통해 정제된 두 녀석을 찾도록 컴퓨터를 굴릴 것이다ㅎㅎ

#### 2. Loss Function(손실함수)

<pre>
<code>
(pre - realValue)^2
</code>
<pre>

예측값에서 실제값을 빼고 제곱한 값의 평균을 구함. 
현재의 가중치,편향값과 데이터를 이용하면 비용함수를 구할 수 있다.

#### 3. Gradient descent(경사 하강법)

* 경사를 타고 내려가서 최대한 수렴이 될 수 있도록 좋은 식을 찾는 과정이 선형회귀에서 발생한 손실을 보완하는 경사하강법
* 미분을 통해 기울기를 구하는데 그 기울기가 결과적으로 수평을 이루는것, 즉 가장 깊은 골짜기에 도달할 때까지 내려가는 것이 가장 좋은 식
* 경사를 타고 내려갈 때 너무 작게 점프하면 = 시간이 오래 걸려
* 경사를 타고 내려갈 때 너무 크게 점프하면 = 부정확한 결과가 나와


