# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
# https://github.com/pandas-dev/pandas/issues/12125
# smoke test for _translate
df = DataFrame({0: [1, 2, 3]})
df.style._translate(True, True)
