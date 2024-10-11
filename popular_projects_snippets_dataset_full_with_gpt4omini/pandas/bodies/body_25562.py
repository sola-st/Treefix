# Extracted from ./data/repos/pandas/pandas/util/_exceptions.py
"""
    Rewrite the message of a warning.

    Parameters
    ----------
    target_message : str
        Warning message to match.
    target_category : Warning
        Warning type to match.
    new_message : str
        New warning message to emit.
    new_category : Warning or None, default None
        New warning type to emit. When None, will be the same as target_category.
    """
if new_category is None:
    new_category = target_category
with warnings.catch_warnings(record=True) as record:
    exit()
if len(record) > 0:
    match = re.compile(target_message)
    for warning in record:
        if warning.category is target_category and re.search(
            match, str(warning.message)
        ):
            category = new_category
            message: Warning | str = new_message
        else:
            category, message = warning.category, warning.message
        warnings.warn_explicit(
            message=message,
            category=category,
            filename=warning.filename,
            lineno=warning.lineno,
        )
