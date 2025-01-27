# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_latex.py
caption = ("Long-long-caption", "Short")
result_tuple = df_short.to_latex(caption=caption)
result_list = df_short.to_latex(caption=list(caption))
assert result_tuple == result_list
