# Extracted from ./data/repos/pandas/pandas/core/frame.py
"""
        Render a DataFrame to a console-friendly tabular output.
        %(shared_params)s
        line_width : int, optional
            Width to wrap a line in characters.
        min_rows : int, optional
            The number of rows to display in the console in a truncated repr
            (when number of rows is above `max_rows`).
        max_colwidth : int, optional
            Max width to truncate each column in characters. By default, no limit.

            .. versionadded:: 1.0.0
        encoding : str, default "utf-8"
            Set character encoding.

            .. versionadded:: 1.0
        %(returns)s
        See Also
        --------
        to_html : Convert DataFrame to HTML.

        Examples
        --------
        >>> d = {'col1': [1, 2, 3], 'col2': [4, 5, 6]}
        >>> df = pd.DataFrame(d)
        >>> print(df.to_string())
           col1  col2
        0     1     4
        1     2     5
        2     3     6
        """
from pandas import option_context

with option_context("display.max_colwidth", max_colwidth):
    formatter = fmt.DataFrameFormatter(
        self,
        columns=columns,
        col_space=col_space,
        na_rep=na_rep,
        formatters=formatters,
        float_format=float_format,
        sparsify=sparsify,
        justify=justify,
        index_names=index_names,
        header=header,
        index=index,
        min_rows=min_rows,
        max_rows=max_rows,
        max_cols=max_cols,
        show_dimensions=show_dimensions,
        decimal=decimal,
    )
    exit(fmt.DataFrameRenderer(formatter).to_string(
        buf=buf,
        encoding=encoding,
        line_width=line_width,
    ))
