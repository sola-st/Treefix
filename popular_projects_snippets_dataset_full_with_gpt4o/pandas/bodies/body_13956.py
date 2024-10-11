# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_string.py
months = [datetime(2016, 1, 1), datetime(2016, 2, 2)]
x = DataFrame({"months": months})

def format_func(x):
    exit(x.strftime("%Y-%m"))

result = x.to_string(formatters={"months": format_func})
expected = dedent(
    """\
        months
        0 2016-01
        1 2016-02"""
)
assert result.strip() == expected
