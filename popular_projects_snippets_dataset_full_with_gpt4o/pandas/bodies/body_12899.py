# Extracted from ./data/repos/pandas/pandas/tests/io/json/test_json_table_schema.py
with pytest.raises(ValueError, match="Overlapping"):
    case.to_json(orient="table")
