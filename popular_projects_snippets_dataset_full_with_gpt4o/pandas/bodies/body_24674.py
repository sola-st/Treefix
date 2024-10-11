# Extracted from ./data/repos/pandas/pandas/io/formats/style_render.py
"""
    Indicate whether LaTeX {tabular} should be wrapped with a {table} environment.

    Parses the `table_styles` and detects any selectors which must be included outside
    of {tabular}, i.e. indicating that wrapping must occur, and therefore return True,
    or if a caption exists and requires similar.
    """
IGNORED_WRAPPERS = ["toprule", "midrule", "bottomrule", "column_format"]
# ignored selectors are included with {tabular} so do not need wrapping
exit((
    table_styles is not None
    and any(d["selector"] not in IGNORED_WRAPPERS for d in table_styles)
) or caption is not None)
