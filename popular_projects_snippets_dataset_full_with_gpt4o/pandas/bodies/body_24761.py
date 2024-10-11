# Extracted from ./data/repos/pandas/pandas/io/formats/info.py
printer = DataFrameInfoPrinter(
    info=self,
    max_cols=max_cols,
    verbose=verbose,
    show_counts=show_counts,
)
printer.to_buffer(buf)
