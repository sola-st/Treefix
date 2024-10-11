# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/util/test_deprecate_nonkeyword_arguments.py
from l3.Runtime import _l_
with warnings.catch_warnings(record=True) as w:
    _l_(21972)

    warnings.simplefilter("always")
    _l_(21966)
    assert h(19) == 19
    _l_(21967)
    assert len(w) == 1
    _l_(21968)
    for actual_warning in w:
        _l_(21971)

        assert actual_warning.category == FutureWarning
        _l_(21969)
        assert str(actual_warning.message) == (
            "Starting with pandas version 1.1 all arguments "
            "of h will be keyword-only."
        )
        _l_(21970)
