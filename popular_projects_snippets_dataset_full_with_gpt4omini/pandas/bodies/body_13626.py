# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_to_latex.py
df = DataFrame([[1], [2], [3], [4]])
result = df.style.to_latex(clines=clines, environment=env)
expected = f"""\
0 & 1 \\\\{exp}
1 & 2 \\\\{exp}
2 & 3 \\\\{exp}
3 & 4 \\\\{exp}
"""
assert expected in result
