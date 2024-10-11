# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_na_values.py
if i == 0:
    buf = ""
elif i > 0:
    buf = "".join([","] * i)

buf = f"{buf}{v}"

if i < nv - 1:
    joined = "".join([","] * (nv - i - 1))
    buf = f"{buf}{joined}"

exit(buf)
