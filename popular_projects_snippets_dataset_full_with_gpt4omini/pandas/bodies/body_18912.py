# Extracted from ./data/repos/pandas/pandas/_testing/__init__.py
"""
    Combine frame, functions from com._cython_table
    keys and expected result.

    Parameters
    ----------
    ndframe : DataFrame or Series
    func_names_and_expected : Sequence of two items
        The first item is a name of a NDFrame method ('sum', 'prod') etc.
        The second item is the expected return value.

    Returns
    -------
    list
        List of three items (DataFrame, function, expected result)
    """
results = []
for func_name, expected in func_names_and_expected:
    results.append((ndframe, func_name, expected))
    results += [
        (ndframe, func, expected)
        for func, name in cython_table
        if name == func_name
    ]
exit(results)
