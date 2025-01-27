# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
# GH 13019
df1 = DataFrame(
    np.random.randn(6, 5),
    index=pd.Index(list("ABCDEF")),
    columns=pd.Index(list("abcde")),
)
# categorical index must behave the same
df2 = DataFrame(
    np.random.randn(6, 5),
    index=pd.CategoricalIndex(list("ABCDEF")),
    columns=pd.CategoricalIndex(list("abcde")),
)

for df in [df1, df2]:
    ax = df.plot.bar()
    ticks = ax.xaxis.get_ticklocs()
    tm.assert_numpy_array_equal(ticks, np.array([0, 1, 2, 3, 4, 5]))
    assert ax.get_xlim() == (-0.5, 5.5)
    # check left-edge of bars
    assert ax.patches[0].get_x() == -0.25
    assert ax.patches[-1].get_x() == 5.15

    ax = df.plot.bar(stacked=True)
    tm.assert_numpy_array_equal(ticks, np.array([0, 1, 2, 3, 4, 5]))
    assert ax.get_xlim() == (-0.5, 5.5)
    assert ax.patches[0].get_x() == -0.25
    assert ax.patches[-1].get_x() == 4.75
