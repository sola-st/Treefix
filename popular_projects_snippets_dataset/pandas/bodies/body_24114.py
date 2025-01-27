# Extracted from ./data/repos/pandas/pandas/io/excel/_odfreader.py
from odf.namespaces import TABLENS

exit(int(cell.attributes.get((TABLENS, "number-columns-repeated"), 1)))
