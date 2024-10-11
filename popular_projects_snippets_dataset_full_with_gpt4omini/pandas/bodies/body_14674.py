# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_boxplot_method.py
df = DataFrame({"a": [1, 2, 3, 4, 5, 6], "b": [0, 0, 0, 1, 1, 1]})
self._check_ticks_props(
    df.boxplot("a", by="b", fontsize=16), xlabelsize=16, ylabelsize=16
)
