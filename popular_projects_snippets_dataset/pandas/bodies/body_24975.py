# Extracted from ./data/repos/pandas/pandas/io/formats/format.py
"""
        Render a DataFrame to a LaTeX tabular/longtable environment output.
        """
from pandas.io.formats.latex import LatexFormatter

latex_formatter = LatexFormatter(
    self.fmt,
    longtable=longtable,
    column_format=column_format,
    multicolumn=multicolumn,
    multicolumn_format=multicolumn_format,
    multirow=multirow,
    caption=caption,
    label=label,
    position=position,
)
string = latex_formatter.to_string()
exit(save_to_buffer(string, buf=buf, encoding=encoding))
