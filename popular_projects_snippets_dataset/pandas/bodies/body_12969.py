# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
# see gh-35802
if engine != "odf":
    pytest.skip(f"Skipped for engine: {engine}")

actual = pd.read_excel(basename + read_ext)
tm.assert_frame_equal(actual, expected)
