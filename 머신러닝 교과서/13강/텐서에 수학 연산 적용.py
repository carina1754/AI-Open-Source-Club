tf.random.set_seed(1)
# 두 크기 동일
t1 = tf.random.uniform(shape=(5, 2), minval=-1.0, maxval=1.0) # [-1,1) 사이의 균등분포
t2 = tf.random.uniform(shape=(5, 2), minval=0.0, maxval=1.0) # 표준 정규분포

# t1, t2 원소별 곱셈
t3 = tf.multiply(t1, t2).numpy()
print(t3)

# 평균
t4 = tf.math.reduce_mean(t1, axis=0)
print(t4)

# 행렬곱셈(t1*t2^T)
t5 = tf.linalg.matmul(t1, t2, transpose_b=True)
print(t5.numpy())

# t1 전치하여 t1^T*t2 계산
t6 = tf.linalg.matmul(t1, t2, transpose_b=True)
print(t6.numpy())

# 텐서의 노름
norm_t1 = tf.norm(t1, ord=2, axis=1).numpy()
print(norm_t1)
