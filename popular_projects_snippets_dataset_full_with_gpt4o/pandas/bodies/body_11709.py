# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_file_buffer_url.py
# see gh-15337
class InvalidBuffer:
    pass

parser = all_parsers
msg = "Invalid file path or buffer object type"

with pytest.raises(ValueError, match=msg):
    parser.read_csv(InvalidBuffer())
