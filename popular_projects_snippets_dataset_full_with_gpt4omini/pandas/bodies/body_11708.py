# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_file_buffer_url.py
# gh-14418
#
# Don't close user provided file handles.
parser = all_parsers

for mode in ["r", "rb"]:
    with open(csv1, mode) as f:
        parser.read_csv(f)
        assert not f.closed
