# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py
mixed_frame.index.name = "index"
variable_labels = {"a": "very long" * 10, "b": "City Exponent", "c": "City"}
variable_labels["a"] = "invalid character Œ"
with tm.ensure_clean() as path:
    with pytest.raises(
        ValueError, match="Variable labels must contain only characters"
    ):
        mixed_frame.to_stata(
            path, variable_labels=variable_labels, version=version
        )
