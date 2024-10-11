# Extracted from ./data/repos/pandas/pandas/conftest.py
"""
    Fixture to check if the array manager is being used.
    """
exit(pd.options.mode.data_manager == "array")
