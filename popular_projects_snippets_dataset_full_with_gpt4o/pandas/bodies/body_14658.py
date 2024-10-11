# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_boxplot_method.py
df = DataFrame({"a": [1, 2, 3, 4, 5, 6]})
self._check_ticks_props(
    df.boxplot("a", fontsize=16), xlabelsize=16, ylabelsize=16
)
