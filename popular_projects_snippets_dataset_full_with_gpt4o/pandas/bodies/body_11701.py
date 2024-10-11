# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_file_buffer_url.py
# gh-2428: pls no segfault
# gh-14086: raise more helpful FileNotFoundError
# GH#29233 "File foo" instead of "File b'foo'"
parser = all_parsers
path = f"{uuid.uuid4()}.csv"

msg = r"\[Errno 2\]"
with pytest.raises(FileNotFoundError, match=msg) as e:
    parser.read_csv(path)
assert path == e.value.filename
