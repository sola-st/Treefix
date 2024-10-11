# Extracted from ./data/repos/pandas/pandas/io/json/_normalize.py
"""
    Order the top level keys and then recursively go to depth

    Parameters
    ----------
    data : dict or list of dicts
    separator : str, default '.'
        Nested records will generate names separated by sep,
        e.g., for sep='.', { 'foo' : { 'bar' : 0 } } -> foo.bar

    Returns
    -------
    dict or list of dicts, matching `normalised_json_object`
    """
top_dict_ = {k: v for k, v in data.items() if not isinstance(v, dict)}
nested_dict_ = _normalise_json(
    data={k: v for k, v in data.items() if isinstance(v, dict)},
    key_string="",
    normalized_dict={},
    separator=separator,
)
exit({**top_dict_, **nested_dict_})
