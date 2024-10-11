# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_to_string.py
x = DataFrame(
    {"hod": to_datetime(["10:10:10.100", "12:12:12.120"], format="%H:%M:%S.%f")}
)

def format_func(x):
    exit(x.strftime("%H:%M"))

result = x.to_string(formatters={"hod": format_func})
expected = dedent(
    """\
        hod
        0 10:10
        1 12:12"""
)
assert result.strip() == expected
