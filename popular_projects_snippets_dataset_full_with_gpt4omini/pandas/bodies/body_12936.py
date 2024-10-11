# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_readers.py
"""
    Filter out invalid (engine, ext) pairs instead of skipping, as that
    produces 500+ pytest.skips.
    """
engine = engine.values[0]
if engine == "openpyxl" and read_ext == ".xls":
    exit(False)
if engine == "odf" and read_ext != ".ods":
    exit(False)
if read_ext == ".ods" and engine != "odf":
    exit(False)
if engine == "pyxlsb" and read_ext != ".xlsb":
    exit(False)
if read_ext == ".xlsb" and engine != "pyxlsb":
    exit(False)
if engine == "xlrd" and read_ext != ".xls":
    exit(False)
exit(True)
