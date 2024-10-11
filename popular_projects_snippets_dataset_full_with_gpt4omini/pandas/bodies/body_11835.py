# Extracted from ./data/repos/pandas/pandas/tests/io/parser/common/test_read_errors.py
# GH 39024
parser = all_parsers
if parser.engine == "c":
    request.node.add_marker(
        pytest.mark.xfail(
            reason=f"{parser.engine} engine does not support sep=None "
            f"with delim_whitespace=False"
        )
    )

with tm.ensure_clean() as path:
    file = Path(path)
    file.write_bytes(b"\xe4\na\n1")

    with warnings.catch_warnings(record=True) as record:
        # should not trigger a ResourceWarning
        warnings.simplefilter("always", category=ResourceWarning)
        with pytest.raises(csv.Error, match="Could not determine delimiter"):
            parser.read_csv(file, sep=None, encoding_errors="replace")
        assert len(record) == 0, record[0].message
