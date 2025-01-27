# Extracted from ./data/repos/pandas/pandas/io/formats/info.py
if max_cols is not None:
    raise ValueError(
        "Argument `max_cols` can only be passed "
        "in DataFrame.info, not Series.info"
    )
printer = SeriesInfoPrinter(
    info=self,
    verbose=verbose,
    show_counts=show_counts,
)
printer.to_buffer(buf)
