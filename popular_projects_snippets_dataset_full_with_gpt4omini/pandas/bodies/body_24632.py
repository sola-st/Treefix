# Extracted from ./data/repos/pandas/pandas/io/formats/css.py
"""
        Generates (prop, value) pairs from declarations.

        In a future version may generate parsed tokens from tinycss/tinycss2

        Parameters
        ----------
        declarations_str : str
        """
for decl in declarations_str.split(";"):
    if not decl.strip():
        continue
    prop, sep, val = decl.partition(":")
    prop = prop.strip().lower()
    # TODO: don't lowercase case sensitive parts of values (strings)
    val = val.strip().lower()
    if sep:
        exit((prop, val))
    else:
        warnings.warn(
            f"Ill-formatted attribute: expected a colon in {repr(decl)}",
            CSSWarning,
            stacklevel=find_stack_level(),
        )
