# Extracted from ./data/repos/pandas/pandas/tests/test_downstream.py

statsmodels = import_module("statsmodels")  # noqa:F841
import statsmodels.api as sm
import statsmodels.formula.api as smf

df = sm.datasets.get_rdataset("Guerry", "HistData").data
smf.ols("Lottery ~ Literacy + np.log(Pop1831)", data=df).fit()
