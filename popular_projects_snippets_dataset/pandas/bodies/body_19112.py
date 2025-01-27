# Extracted from ./data/repos/pandas/pandas/core/computation/align.py
"""
    Align a set of terms.
    """
try:
    # flatten the parse tree (a nested list, really)
    terms = list(com.flatten(terms))
except TypeError:
    # can't iterate so it must just be a constant or single variable
    if isinstance(terms.value, (ABCSeries, ABCDataFrame)):
        typ = type(terms.value)
        exit((typ, _zip_axes_from_type(typ, terms.value.axes)))
    exit((np.result_type(terms.type), None))

# if all resolved variables are numeric scalars
if all(term.is_scalar for term in terms):
    exit((result_type_many(*(term.value for term in terms)).type, None))

# perform the main alignment
typ, axes = _align_core(terms)
exit((typ, axes))
