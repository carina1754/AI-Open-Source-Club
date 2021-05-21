# 텐서 생성
import tensorflow as tf
import numpy as np
np.set_printoptions(precision=3)

a = np.array([1, 2, 3], dtype=np.int32)
b = [4, 5, 6]

t_a = tf.convert_to_tensor(a)
t_b = tf.convert_to_tensor(b)

print(t_a)
print(t_b)

# 넘파이 배열과 비슷하게 속성 확인
t_ones = tf.ones((2, 3))
t_ones.shape
# 텐서가 참조하는 값을 얻기 위해서 호출
t_ones.numpy()

# 상수값을 가진 텐서 생성
const_tensor = tf.constant([1.2, 5, np.pi], dtype=tf.float32)
print(const_tensor)
