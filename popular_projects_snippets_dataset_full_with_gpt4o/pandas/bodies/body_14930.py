# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_converter.py
units = pytest.importorskip("matplotlib.units")

# Can't make any assertion about the start state.
# We we check that toggling converters off removes it, and toggling it
# on restores it.

with cf.option_context("plotting.matplotlib.register_converters", True):
    with cf.option_context("plotting.matplotlib.register_converters", False):
        assert Timestamp not in units.registry
    assert Timestamp in units.registry
