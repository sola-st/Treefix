# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_file_buffer_url.py
# GH 23784
parser = all_parsers

msg = r"\[Errno 13\]"
with tm.ensure_clean() as path:
    os.chmod(path, 0)  # make file unreadable

    # verify that this process cannot open the file (not running as sudo)
    try:
        with open(path):
            pass
        pytest.skip("Running as sudo.")
    except PermissionError:
        pass

    with pytest.raises(PermissionError, match=msg) as e:
        parser.read_csv(path)
    assert path == e.value.filename
