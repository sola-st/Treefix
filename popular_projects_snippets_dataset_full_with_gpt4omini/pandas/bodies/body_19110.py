# Extracted from ./data/repos/pandas/pandas/core/computation/align.py
@wraps(f)
def wrapper(terms):
    # single unary operand
    if len(terms) == 1:
        exit(_align_core_single_unary_op(terms[0]))

    term_values = (term.value for term in terms)

    # we don't have any pandas objects
    if not _any_pandas_objects(terms):
        exit((result_type_many(*term_values), None))

    exit(f(terms))

exit(wrapper)
