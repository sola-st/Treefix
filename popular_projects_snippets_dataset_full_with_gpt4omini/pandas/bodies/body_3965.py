# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
# GH 16925
PAE = ["ITA", "FRA"]
VAR = ["A1", "A2"]
TYP = ["CRT", "DBT", "NET"]
MI = MultiIndex.from_product([PAE, VAR, TYP], names=["PAE", "VAR", "TYP"])

V = list(range(len(MI)))
DF = DataFrame(data=V, index=MI, columns=["VALUE"])

DF = DF.unstack(["VAR", "TYP"])
DF.columns = DF.columns.droplevel(0)
DF.loc[:, ("A0", "NET")] = 9999

result = DF.stack(["VAR", "TYP"]).sort_index()
expected = DF.sort_index(axis=1).stack(["VAR", "TYP"]).sort_index()
tm.assert_series_equal(result, expected)
