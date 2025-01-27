# Extracted from ./data/repos/pandas/pandas/tests/io/parser/test_unsupported.py
# GH#45957
parser = all_parsers
if parser.engine == "python":
    request.node.add_marker(
        pytest.mark.xfail(reason=f"{parser.engine} engine supports lists.")
    )

with pytest.raises(ValueError, match="Invalid"):
    parser.read_csv([])
