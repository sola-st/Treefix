# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py
original = DataFrame({"a": [1 + 2j, 2 + 4j]})

msg = "Data type complex128 not supported"
with pytest.raises(NotImplementedError, match=msg):
    with tm.ensure_clean() as path:
        original.to_stata(path)
