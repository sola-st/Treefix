# Extracted from ./data/repos/pandas/pandas/_testing/asserters.py
"""
    iter1, iter2: iterables that produce elements
    comparable with assert_almost_equal

    Checks that the elements are equal, but not
    the same object. (Does not check that items
    in sequences are also not the same object)
    """
for elem1, elem2 in zip(iter1, iter2):
    assert_almost_equal(elem1, elem2, **eql_kwargs)
    msg = (
        f"Expected object {repr(type(elem1))} and object {repr(type(elem2))} to be "
        "different objects, but they were the same object."
    )
    assert elem1 is not elem2, msg
