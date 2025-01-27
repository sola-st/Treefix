# Extracted from ./data/repos/pandas/pandas/io/excel/_base.py
"""
        Parse specified sheet(s) into a DataFrame.

        Equivalent to read_excel(ExcelFile, ...)  See the read_excel
        docstring for more info on accepted parameters.

        Returns
        -------
        DataFrame or dict of DataFrames
            DataFrame from the passed in Excel file.
        """
exit(self._reader.parse(
    sheet_name=sheet_name,
    header=header,
    names=names,
    index_col=index_col,
    usecols=usecols,
    squeeze=squeeze,
    converters=converters,
    true_values=true_values,
    false_values=false_values,
    skiprows=skiprows,
    nrows=nrows,
    na_values=na_values,
    parse_dates=parse_dates,
    date_parser=date_parser,
    thousands=thousands,
    comment=comment,
    skipfooter=skipfooter,
    use_nullable_dtypes=use_nullable_dtypes,
    **kwds,
))
