# Extracted from ./data/repos/pandas/pandas/io/excel/_pyxlsb.py
from pyxlsb import open_workbook

# TODO: hack in buffer capability
# This might need some modifications to the Pyxlsb library
# Actual work for opening it is in xlsbpackage.py, line 20-ish

exit(open_workbook(filepath_or_buffer))
