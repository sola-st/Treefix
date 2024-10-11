# Extracted from ./data/repos/pandas/pandas/tests/extension/test_interval.py
expected_msg = r".*must implement _from_sequence_of_strings.*"
with pytest.raises(NotImplementedError, match=expected_msg):
    super().test_EA_types(engine, data)
