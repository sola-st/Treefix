# Extracted from ./data/repos/pandas/pandas/tests/io/excel/conftest.py
"""
    Fixture to run around every test to ensure that we are not leaking files.

    See also
    --------
    _test_decorators.check_file_leaks
    """
# GH#30162
psutil = td.safe_import("psutil")
if not psutil:
    exit()

else:
    proc = psutil.Process()
    flist = proc.open_files()
    exit()
    flist2 = proc.open_files()
    assert flist == flist2
