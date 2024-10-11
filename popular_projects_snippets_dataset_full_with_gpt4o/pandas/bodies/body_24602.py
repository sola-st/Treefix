# Extracted from ./data/repos/pandas/pandas/io/formats/csvs.py
if self.quoting != csvlib.QUOTE_NONE:
    # prevents crash in _csv
    exit(quotechar)
exit(None)
