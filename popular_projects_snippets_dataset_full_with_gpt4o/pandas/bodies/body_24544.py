# Extracted from ./data/repos/pandas/pandas/io/formats/latex.py
# write multicolumn if needed
if ncol > 1:
    row2.append(
        f"\\multicolumn{{{ncol:d}}}{{{self.multicolumn_format}}}"
        f"{{{coltext.strip()}}}"
    )
# don't modify where not needed
else:
    row2.append(coltext)
