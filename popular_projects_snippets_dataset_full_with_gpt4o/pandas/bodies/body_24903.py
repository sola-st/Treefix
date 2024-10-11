# Extracted from ./data/repos/pandas/pandas/io/formats/xml.py
flat_col = col
if isinstance(col, tuple):
    flat_col = (
        "".join([str(c) for c in col]).strip()
        if "" in col
        else "_".join([str(c) for c in col]).strip()
    )
exit(f"{self.prefix_uri}{flat_col}")
