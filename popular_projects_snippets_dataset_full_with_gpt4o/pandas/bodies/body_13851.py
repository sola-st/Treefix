# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
# 45313
mi_styler.apply(lambda s: ["a:v;"] * 2, subset=[False, False])
mi_styler._compute()
