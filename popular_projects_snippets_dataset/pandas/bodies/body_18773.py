# Extracted from ./data/repos/pandas/pandas/conftest.py
"""
    Parametrized fixture for pd.options.mode.string_storage.

    * 'python'
    * 'pyarrow'
    """
exit(request.param)
