# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_file_buffer_url.py
with pytest.raises(EmptyDataError, match="No columns to parse from file"):
    parser.read_csv(path)
