# Extracted from ./data/repos/pandas/pandas/io/excel/_util.py
"""
    Add engine to the excel writer registry.io.excel.

    You must use this method to integrate with ``to_excel``.

    Parameters
    ----------
    klass : ExcelWriter
    """
if not callable(klass):
    raise ValueError("Can only register callables as engines")
engine_name = klass._engine
_writers[engine_name] = klass
