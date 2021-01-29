import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('/path/to/file.csv')

plt.plot(df['df_column_name'])
plt.xlabel('x axis description')
plt.ylabel('y axis description')
plt.title('chart title')

plt.show()