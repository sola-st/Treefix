# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_unsupported.py
# GH 5686
sio = StringIO("a,b\n1,2")
bad_lines_func = lambda x: x
parser = all_parsers
if all_parsers.engine != "python":
    msg = "on_bad_line can only be a callable function if engine='python'"
    with pytest.raises(ValueError, match=msg):
        parser.read_csv(sio, on_bad_lines=bad_lines_func)
else:
    parser.read_csv(sio, on_bad_lines=bad_lines_func)
