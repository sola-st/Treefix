# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_file_buffer_url.py
# see gh-13398
parser = all_parsers
data = "0 0"

with tm.ensure_clean(mode="w+", return_filelike=True) as new_file:
    new_file.write(data)
    new_file.flush()
    new_file.seek(0)

    result = parser.read_csv(new_file, sep=r"\s+", header=None)

    expected = DataFrame([[0, 0]])
    tm.assert_frame_equal(result, expected)
