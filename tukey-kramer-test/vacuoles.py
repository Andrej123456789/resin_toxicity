import numpy as np
from scipy.stats import tukey_hsd
import pandas as pd

k_minus = [0.071047957,0.072555205,0.068441065,0.057866184,0.042654028]
k_plus = [0.094,0.053892216,0.161290323,0.11023622]
v1 = [0.140394089,0,0.015779093,0.136554622,0.205]
a1 = [0.341530055,0.198900092,0.18404908,0.011695906,0.474006116]
u1 = [0.23943662,0.031674208,0.101818182,0.113590264]
v2 = [0.03407155,0.167108753,0.089403974,0.086238532,0.17016317]
a2 = [0.293307087,0.12543554,0.136,0.255725191,0.110663984]
u2 = [0.155945419,0,0.188605108,0.177865613,0]

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
