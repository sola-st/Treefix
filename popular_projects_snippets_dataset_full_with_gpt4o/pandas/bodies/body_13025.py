# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
# read_ext includes the '.' hence the weird formatting
with pytest.raises(ValueError, match="Value must be one of *"):
    with pd.option_context(f"io.excel{read_ext}.reader", "abc"):
        pass
