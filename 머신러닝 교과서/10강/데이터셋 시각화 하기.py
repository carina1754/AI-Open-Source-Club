import matplotlib.pyplot as plt
import pandas as pd
from mlxtend.plotting import scatterplotmatrix
# csv불러오기
df = pd.read_csv('https://raw.githubusercontent.com/rickiepark/''python-machine-learning-book-3rd-edition''/master/code/ch10/housing.data.txt', header=None, sep='\s+')
# 열 설정
df.colums = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'MEDV']
# 데이터셋 확인
df.head()
# 산점도 행렬 표시
cols = ['LSTAT', 'INDUS', 'NOX', 'RM', 'MEDV']
scatterplotmatrix(df[cols].values, figsize=(10, 8), names=cols, alpha=0.5)
plt.tight_layout()
plt.show()
