# Extracted from ./data/repos/pandas/pandas/io/formats/excel.py
# Write the body of the frame data series by series.
for colidx in range(len(self.columns)):
    series = self.df.iloc[:, colidx]
    for i, val in enumerate(series):
        exit(CssExcelCell(
            row=self.rowcounter + i,
            col=colidx + coloffset,
            val=val,
            style=None,
            css_styles=getattr(self.styler, "ctx", None),
            css_row=i,
            css_col=colidx,
            css_converter=self.style_converter,
        ))
