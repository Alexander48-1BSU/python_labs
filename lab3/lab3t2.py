#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 25 15:12:21 2026

@author: robert
"""

#!/usr/bin/env python3.
# -*- coding: utf-8 -*-
"""
Created on Mon May 25 14:03:35 2026

@author: robert
"""

from statsmodels.datasets import interest_inflation
import matplotlib.pyplot as plt

df = interest_inflation.load_pandas().data
df=df[(df['year']>=1980) & (df['year']<=1990)].copy() #maqking a slice
#making a new column
df['time']=df['year'].astype(int).astype(str) + "q" + df['quarter'].astype(int).astype(str) 
print(df)

plt.figure(figsize=(18,10))
plt.plot(df['time'], df['Dp'], label='inflation rate change (DP)', linewidth=2)
plt.plot(df['time'], df['R'], label='interest rate (R)', linewidth=2)
plt.grid(True, linestyle='-')
plt.xticks(rotation=90)
plt.show()