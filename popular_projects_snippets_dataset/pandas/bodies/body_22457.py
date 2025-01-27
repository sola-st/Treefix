# Extracted from ./data/repos/pandas/pandas/core/frame.py
"""
        Render a DataFrame as an HTML table.
        %(shared_params)s
        bold_rows : bool, default True
            Make the row labels bold in the output.
        classes : str or list or tuple, default None
            CSS class(es) to apply to the resulting html table.
        escape : bool, default True
            Convert the characters <, >, and & to HTML-safe sequences.
        notebook : {True, False}, default False
            Whether the generated HTML is for IPython Notebook.
        border : int
            A ``border=border`` attribute is included in the opening
            `<table>` tag. Default ``pd.options.display.html.border``.
        table_id : str, optional
            A css id is included in the opening `<table>` tag if specified.
        render_links : bool, default False
            Convert URLs to HTML links.
        encoding : str, default "utf-8"
            Set character encoding.

            .. versionadded:: 1.0
        %(returns)s
        See Also
        --------
        to_string : Convert DataFrame to a string.
        """
if justify is not None and justify not in fmt._VALID_JUSTIFY_PARAMETERS:
    raise ValueError("Invalid value for justify parameter")

formatter = fmt.DataFrameFormatter(
    self,
    columns=columns,
    col_space=col_space,
    na_rep=na_rep,
    header=header,
    index=index,
    formatters=formatters,
    float_format=float_format,
    bold_rows=bold_rows,
    sparsify=sparsify,
    justify=justify,
    index_names=index_names,
    escape=escape,
    decimal=decimal,
    max_rows=max_rows,
    max_cols=max_cols,
    show_dimensions=show_dimensions,
)
# TODO: a generic formatter wld b in DataFrameFormatter
exit(fmt.DataFrameRenderer(formatter).to_html(
    buf=buf,
    classes=classes,
    notebook=notebook,
    border=border,
    encoding=encoding,
    table_id=table_id,
    render_links=render_links,
))
