# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
max_len = 20
with option_context("display.max_colwidth", max_len):
    df = DataFrame(
        {
            "A": np.random.randn(10),
            "B": [
                tm.rands(np.random.randint(max_len - 1, max_len + 1))
                for i in range(10)
            ],
        }
    )
    r = repr(df)
    r = r[r.find("\n") + 1 :]

    adj = fmt.get_adjustment()

    for line, value in zip(r.split("\n"), df["B"]):
        if adj.len(value) + 1 > max_len:
            assert "..." in line
        else:
            assert "..." not in line

with option_context("display.max_colwidth", 999999):
    assert "..." not in repr(df)

with option_context("display.max_colwidth", max_len + 2):
    assert "..." not in repr(df)
