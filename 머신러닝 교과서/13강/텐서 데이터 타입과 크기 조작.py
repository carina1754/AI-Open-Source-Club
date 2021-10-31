# 텐서의 데이터 타입 변환
t_a_new = tf.cast(t_a, tf.int64)
print(t_a_new.dtype)

# 텐서 전치하기
t = tf.random.uniform(shape=(3, 5))
t_tr = tf.transpose(t)
print(t.shape, ' --> ', t_tr.shape)

# 텐서 크기 바꾸기 ((ex) 1D->2D 배열)
t = tf.zeros((30,))
t_reshape = tf.reshape(t, shape=(5, 6))
print(t_reshape.shape)

# 불필요한 차원 삭제하기(크기가 1인 차원은 불필요합니다.)
t = tf.zeros((1, 2, 1, 4, 1))
t_sqz = tf.squeeze(t, axis=(2, 4))
print(t.shape, ' --> ', t_sqz.shape)
