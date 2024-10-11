# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_writers.py
filename = "with_header"
df = DataFrame([["", 1, 100], ["", 2, 200], ["", 3, 300], ["", 4, 400]])

with tm.ensure_clean(ext) as path:
    df.to_excel(path, "with_header", index=False, header=True)
    result = pd.read_excel(
        path, sheet_name=filename, usecols=[0], header=header
    )

tm.assert_frame_equal(result, expected)
