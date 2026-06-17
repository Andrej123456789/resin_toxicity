import numpy as np
from scipy.stats import tukey_hsd
import pandas as pd

k_minus = [0.330373002,0.255520505,0.300380228,0.392405063,0.315165877]
k_plus = [0.14,0.600798403,0.5,0.803149606]
v1 = [0.290640394,0.647191011,0.631163708,0.49789916,0.516666667]
a1 = [0.461065574,0.64619615,0.561349693,0.555555556,0.44648318]
u1 = [0.450704225,0.554298643,0.501818182,0.456389452]
v2 = [0.614991482,0.514588859,0.574503311,0.588990826,0.58974359]
a2 = [0.362204724,0.637630662,0.44,0.389312977,0.426559356]
u2 = [0.500974659,0.606585789,0.436149312,0.523715415,0.785234899]

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
