# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame_legend.py
kinds = ["line", "bar", "barh", "kde", "area", "hist"]
df = DataFrame(np.random.rand(3, 3), columns=["a", "b", "c"])
df2 = DataFrame(np.random.rand(3, 3), columns=["d", "e", "f"])
df3 = DataFrame(np.random.rand(3, 3), columns=["g", "h", "i"])
df4 = DataFrame(np.random.rand(3, 3), columns=["j", "k", "l"])

for kind in kinds:

    ax = df.plot(kind=kind, legend=True)
    self._check_legend_labels(ax, labels=df.columns)

    ax = df2.plot(kind=kind, legend=False, ax=ax)
    self._check_legend_labels(ax, labels=df.columns)

    ax = df3.plot(kind=kind, legend=True, ax=ax)
    self._check_legend_labels(ax, labels=df.columns.union(df3.columns))

    ax = df4.plot(kind=kind, legend="reverse", ax=ax)
    expected = list(df.columns.union(df3.columns)) + list(reversed(df4.columns))
    self._check_legend_labels(ax, labels=expected)

# Secondary Y
ax = df.plot(legend=True, secondary_y="b")
self._check_legend_labels(ax, labels=["a", "b (right)", "c"])
ax = df2.plot(legend=False, ax=ax)
self._check_legend_labels(ax, labels=["a", "b (right)", "c"])
ax = df3.plot(kind="bar", legend=True, secondary_y="h", ax=ax)
self._check_legend_labels(
    ax, labels=["a", "b (right)", "c", "g", "h (right)", "i"]
)

# Time Series
ind = date_range("1/1/2014", periods=3)
df = DataFrame(np.random.randn(3, 3), columns=["a", "b", "c"], index=ind)
df2 = DataFrame(np.random.randn(3, 3), columns=["d", "e", "f"], index=ind)
df3 = DataFrame(np.random.randn(3, 3), columns=["g", "h", "i"], index=ind)
ax = df.plot(legend=True, secondary_y="b")
self._check_legend_labels(ax, labels=["a", "b (right)", "c"])
ax = df2.plot(legend=False, ax=ax)
self._check_legend_labels(ax, labels=["a", "b (right)", "c"])
ax = df3.plot(legend=True, ax=ax)
self._check_legend_labels(ax, labels=["a", "b (right)", "c", "g", "h", "i"])

# scatter
ax = df.plot.scatter(x="a", y="b", label="data1")
self._check_legend_labels(ax, labels=["data1"])
ax = df2.plot.scatter(x="d", y="e", legend=False, label="data2", ax=ax)
self._check_legend_labels(ax, labels=["data1"])
ax = df3.plot.scatter(x="g", y="h", label="data3", ax=ax)
self._check_legend_labels(ax, labels=["data1", "data3"])

# ensure label args pass through and
# index name does not mutate
# column names don't mutate
df5 = df.set_index("a")
ax = df5.plot(y="b")
self._check_legend_labels(ax, labels=["b"])
ax = df5.plot(y="b", label="LABEL_b")
self._check_legend_labels(ax, labels=["LABEL_b"])
self._check_text_labels(ax.xaxis.get_label(), "a")
ax = df5.plot(y="c", label="LABEL_c", ax=ax)
self._check_legend_labels(ax, labels=["LABEL_b", "LABEL_c"])
assert df5.columns.tolist() == ["b", "c"]
