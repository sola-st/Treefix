# Extracted from ./data/repos/pandas/pandas/tests/test_downstream.py

seaborn = import_module("seaborn")
tips = seaborn.load_dataset("tips")
seaborn.stripplot(x="day", y="total_bill", data=tips)
