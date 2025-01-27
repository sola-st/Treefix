# Extracted from ./data/repos/pandas/pandas/conftest.py
"""
    Fixture to check if Copy-on-Write is enabled.
    """
exit(pd.options.mode.copy_on_write and pd.options.mode.data_manager == "block")
