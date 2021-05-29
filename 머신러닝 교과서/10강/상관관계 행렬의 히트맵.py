from mlxtend.plotting import heatmap
import pandas as pd
import numpy as np
df = pd.read_csv('https://raw.githubusercontent.com/rickiepark/''python-machine-learning-book-3rd-edition''/master/code/ch10/housing.data.txt', header=None, sep='\s+')
cols = ['LSTAT', 'INDUS', 'NOX', 'RM', 'MEDV']
cm = np.corroef(df[cols].values.T)
hm = heatmap(cm, row_names=cols, column_names=cols)
plt.show()
