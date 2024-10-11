# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py
mixed_frame.index.name = "index"
variable_labels = {"a": "very long" * 10, "b": "City Exponent", "c": "City"}
with tm.ensure_clean() as path:
    msg = "Variable labels must be 80 characters or fewer"
    with pytest.raises(ValueError, match=msg):
        mixed_frame.to_stata(
            path, variable_labels=variable_labels, version=version
        )
