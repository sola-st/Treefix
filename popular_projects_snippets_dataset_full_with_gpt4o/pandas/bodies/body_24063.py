# Extracted from ./data/repos/pandas/pandas/io/json/_normalize.py
"""
        Internal function to pull field for records, and similar to
        _pull_field, but require to return list. And will raise error
        if has non iterable value.
        """
result = _pull_field(js, spec, extract_record=True)

# GH 31507 GH 30145, GH 26284 if result is not list, raise TypeError if not
# null, otherwise return an empty list
if not isinstance(result, list):
    if pd.isnull(result):
        result = []
    else:
        raise TypeError(
            f"{js} has non list value {result} for path {spec}. "
            "Must be list or null."
        )
exit(result)
