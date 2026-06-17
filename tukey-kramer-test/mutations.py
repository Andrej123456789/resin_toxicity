import numpy as np
from scipy.stats import tukey_hsd
import pandas as pd

k_minus = [0,0.001577287,0.001901141,0,0]
k_plus = [0.002,0.007984032,0.004032258,0]
v1 = [0,0,0,0,0.006666667]
a1 = [0,0.002749771,0.001533742,0,0]
u1 = [0.001760563,0.004524887,0,0.014198783]
v2 = [0.005110733,0.00265252,0,0,0.011655012]
a2 = [0,0,0,0.001908397,0]
u2 = [0.003898635,0.012131716,0.011787819,0.001976285,0]

res = tukey_hsd(k_minus, k_plus, v1, a1, u1, v2, a2, u2)
print(res)

# Extract matrices
stat_matrix = res.statistic
pval_matrix = res.pvalue
ci = res.confidence_interval(confidence_level=0.95)

# Collect unique pairs (i < j)
rows = []
n_groups = stat_matrix.shape[0]
for i in range(n_groups):
    for j in range(i+1, n_groups):
        rows.append([
            i, j,
            stat_matrix[i,j],
            pval_matrix[i,j],
            ci.low[i,j],
            ci.high[i,j]
        ])

# Make a DataFrame and print
df = pd.DataFrame(rows, columns=["Group1", "Group2", "Statistic", "PValue", "CI_Low", "CI_High"])
pd.set_option("display.float_format", "{:.6f}".format)  # 6 decimals
print(df)
