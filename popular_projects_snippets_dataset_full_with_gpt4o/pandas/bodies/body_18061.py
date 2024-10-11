# Extracted from ./data/repos/pandas/pandas/tests/util/test_deprecate_nonkeyword_arguments.py
with warnings.catch_warnings(record=True) as w:
    warnings.simplefilter("always")
    assert f(6, 3, 3) == 12
    assert len(w) == 1
    for actual_warning in w:
        assert actual_warning.category == FutureWarning
        assert str(actual_warning.message) == (
            "Starting with pandas version 1.1 all arguments of f_add_inputs "
            "except for the arguments 'a' and 'b' will be keyword-only."
        )
