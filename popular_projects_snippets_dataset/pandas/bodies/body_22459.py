# Extracted from ./data/repos/pandas/pandas/core/frame.py
info = DataFrameInfo(
    data=self,
    memory_usage=memory_usage,
)
info.render(
    buf=buf,
    max_cols=max_cols,
    verbose=verbose,
    show_counts=show_counts,
)
