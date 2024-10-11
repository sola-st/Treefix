# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_na_values.py
_NA_VALUES = {
    "-1.#IND",
    "1.#QNAN",
    "1.#IND",
    "-1.#QNAN",
    "#N/A",
    "N/A",
    "n/a",
    "NA",
    "<NA>",
    "#NA",
    "NULL",
    "null",
    "NaN",
    "nan",
    "-NaN",
    "-nan",
    "#N/A N/A",
    "",
    "None",
}
assert _NA_VALUES == STR_NA_VALUES

parser = all_parsers
nv = len(_NA_VALUES)

def f(i, v):
    if i == 0:
        buf = ""
    elif i > 0:
        buf = "".join([","] * i)

    buf = f"{buf}{v}"

    if i < nv - 1:
        joined = "".join([","] * (nv - i - 1))
        buf = f"{buf}{joined}"

    exit(buf)

data = StringIO("\n".join([f(i, v) for i, v in enumerate(_NA_VALUES)]))
expected = DataFrame(np.nan, columns=range(nv), index=range(nv))

result = parser.read_csv(data, header=None)
tm.assert_frame_equal(result, expected)
