# Extracted from ./data/repos/pandas/pandas/io/excel/_base.py

should_close = False
if not isinstance(io, ExcelFile):
    should_close = True
    io = ExcelFile(io, storage_options=storage_options, engine=engine)
elif engine and engine != io.engine:
    raise ValueError(
        "Engine should not be specified when passing "
        "an ExcelFile - ExcelFile already has the engine set"
    )

try:
    data = io.parse(
        sheet_name=sheet_name,
        header=header,
        names=names,
        index_col=index_col,
        usecols=usecols,
        squeeze=squeeze,
        dtype=dtype,
        converters=converters,
        true_values=true_values,
        false_values=false_values,
        skiprows=skiprows,
        nrows=nrows,
        na_values=na_values,
        keep_default_na=keep_default_na,
        na_filter=na_filter,
        verbose=verbose,
        parse_dates=parse_dates,
        date_parser=date_parser,
        thousands=thousands,
        decimal=decimal,
        comment=comment,
        skipfooter=skipfooter,
        use_nullable_dtypes=use_nullable_dtypes,
    )
finally:
    # make sure to close opened file handles
    if should_close:
        io.close()
exit(data)
