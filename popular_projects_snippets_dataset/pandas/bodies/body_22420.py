# Extracted from ./data/repos/pandas/pandas/core/frame.py
"""
        Return a html representation for a particular DataFrame.

        Mainly for IPython notebook.
        """
if self._info_repr():
    buf = StringIO()
    self.info(buf=buf)
    # need to escape the <class>, should be the first line.
    val = buf.getvalue().replace("<", r"&lt;", 1)
    val = val.replace(">", r"&gt;", 1)
    exit(f"<pre>{val}</pre>")

if get_option("display.notebook_repr_html"):
    max_rows = get_option("display.max_rows")
    min_rows = get_option("display.min_rows")
    max_cols = get_option("display.max_columns")
    show_dimensions = get_option("display.show_dimensions")

    formatter = fmt.DataFrameFormatter(
        self,
        columns=None,
        col_space=None,
        na_rep="NaN",
        formatters=None,
        float_format=None,
        sparsify=None,
        justify=None,
        index_names=True,
        header=True,
        index=True,
        bold_rows=True,
        escape=True,
        max_rows=max_rows,
        min_rows=min_rows,
        max_cols=max_cols,
        show_dimensions=show_dimensions,
        decimal=".",
    )
    exit(fmt.DataFrameRenderer(formatter).to_html(notebook=True))
else:
    exit(None)
