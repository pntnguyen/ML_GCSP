import mglearn
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
## setting working directory
os.getcwd()
os.chdir("./Term_project")

## read data
data = pd.read_csv("./data/METABRIC_RNA_Mutation.csv")

clinical_documented_cols = data.columns[:31].tolist()
mutation_cols = [c for c in data.columns if c.lower().endswith("_mut")]
expression_cols = [
    c for c in data.columns[31:]
    if c not in mutation_cols
]

data[clinical_documented_cols]

np.random.seed(1)
np.random.rand(1)

from sklearn.model_selection import train_test_split 

data["surv"] = np.where(data["overall_survival"] == 1, 0, 1)

X_train, X_test, y_train, y_test = train_test_split(
    data[clinical_documented_cols], data["surv"], random_state=0, test_size=0.25
)

import mglearn

pd.plotting.scatter_matrix(
    data[["age_at_diagnosis", "nottingham_prognostic_index", "hormone_therapy"]],
    figsize=(15, 15),
    marker="o",
    hist_kwds={"bins": 20},
    c=data["surv"],
    s=60,
    alpha=0.8,
    cmap=mglearn.cm3,
)

plt.show()

