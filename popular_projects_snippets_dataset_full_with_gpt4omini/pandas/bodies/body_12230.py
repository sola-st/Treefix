# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_unsupported.py
# GH 45384
parser = all_parsers

error = ValueError
if parser.engine == "pyarrow":
    pyarrow = pytest.importorskip("pyarrow")
    error = pyarrow.lib.ArrowKeyError
    if is_ci_environment() and (is_platform_windows() or is_platform_mac()):
        # GH#45547 causes timeouts on windows/mac builds
        pytest.skip("GH#45547 causing timeouts on windows/mac builds 2022-01-22")

with tm.ensure_clean("test.csv") as fname:
    Path(fname).write_text("col1,col2\na,b\n1,2")
    with tm.assert_produces_warning(False):
        with pytest.raises(error, match="col3"):
            parser.read_csv(fname, usecols=["col1", "col2", "col3"])
        # unlink fails on windows if file handles still point to it
    os.unlink(fname)
