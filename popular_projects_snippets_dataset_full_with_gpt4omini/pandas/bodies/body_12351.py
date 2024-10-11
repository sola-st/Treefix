# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py
output = [{"none": "none", "number": 0}, {"none": None, "number": 1}]
output = DataFrame(output)
output["none"] = None
with tm.ensure_clean() as path:
    with pytest.raises(ValueError, match="Column `none` cannot be exported"):
        output.to_stata(path, version=version)
