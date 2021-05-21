# 하나의 텐서를 두개 이상 텐서로 나누기 가정
# 분할 개수 지정
# 크기 6인 텐서 => 크기 2인 텐서 3개로 분할
tf.random.set_seed(1)
t = tf.random.uniform((6,))
print(t.numpy())
t_splits = tf.split(t, num_or_size_splits=3)
[item.numpy() for item in t_splits]
# 다른 분할 크기 전달하기
# 크기 5인 텐서 => 크기 2인 텐서 + 크기 3인 텐서
tf.random.set_seed(1)
t = tf.random.uniform((5,))
print(t.numpy())
t_splits = tf.split(t, num_or_size_splits=[3, 2])
[item.numpy() for item in t_splits]
# 여러 개의 텐서를 연결하거나 쌓아서 하나의 텐서를 만들어야 하는 경우
# 크기 3이고 1로 채워진 텐서 A + 크기 2이고 0로 채워진 텐서 B를 연결 => 1D텐서
A = tf.ones((3,))
B = tf.zeros((2,))
C = tf.concat([A, B], axis=0)
print(C.numpy())
# 크기 3이고 1로 채워진 텐서 A + 크기 3이고 0로 채워진 텐서 B를 연결 => 2D텐서 가능
A = tf.ones((3,))
B = tf.zeros((3,))
S = tf.stack([A, B], axis=1)
print(S.numpy())
