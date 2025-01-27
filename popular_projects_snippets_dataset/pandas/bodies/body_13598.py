# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_to_latex.py
cidx = MultiIndex.from_tuples([("Z", "a"), ("Z", "b"), ("Y", "c")])
ridx = MultiIndex.from_tuples([("A", "a"), ("A", "b"), ("B", "c")])
df_ext.index, df_ext.columns = ridx, cidx
styler = df_ext.style

latex1 = styler.to_latex()
with option_context(option, value):
    latex2 = styler.to_latex()
assert (latex1 == latex2) is value
