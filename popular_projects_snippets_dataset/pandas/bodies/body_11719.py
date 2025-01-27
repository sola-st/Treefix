# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_file_buffer_url.py
# GH 31488

parser = all_parsers
with tm.ensure_clean() as path:

    def test():
        with pytest.raises(EmptyDataError, match="No columns to parse from file"):
            parser.read_csv(path)

    td.check_file_leaks(test)()
