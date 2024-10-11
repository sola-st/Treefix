# Extracted from ./data/repos/pandas/pandas/util/_doctools.py
import matplotlib.pyplot as plt

p = TablePlotter()

df1 = pd.DataFrame({"A": [10, 11, 12], "B": [20, 21, 22], "C": [30, 31, 32]})
df2 = pd.DataFrame({"A": [10, 12], "C": [30, 32]})

p.plot([df1, df2], pd.concat([df1, df2]), labels=["df1", "df2"], vertical=True)
plt.show()

df3 = pd.DataFrame({"X": [10, 12], "Z": [30, 32]})

p.plot(
    [df1, df3], pd.concat([df1, df3], axis=1), labels=["df1", "df2"], vertical=False
)
plt.show()

idx = pd.MultiIndex.from_tuples(
    [(1, "A"), (1, "B"), (1, "C"), (2, "A"), (2, "B"), (2, "C")]
)
column = pd.MultiIndex.from_tuples([(1, "A"), (1, "B")])
df3 = pd.DataFrame({"v1": [1, 2, 3, 4, 5, 6], "v2": [5, 6, 7, 8, 9, 10]}, index=idx)
df3.columns = column
p.plot(df3, df3, labels=["df3"])
plt.show()
