# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_converter.py
units = pytest.importorskip("matplotlib.units")
dates = pytest.importorskip("matplotlib.dates")

# make a copy, to reset to
original = dict(units.registry)

try:
    # get to a known state
    units.registry.clear()
    date_converter = dates.DateConverter()
    units.registry[datetime] = date_converter
    units.registry[date] = date_converter

    register_matplotlib_converters()
    assert units.registry[date] is not date_converter
    deregister_matplotlib_converters()
    assert units.registry[date] is date_converter

finally:
    # restore original stater
    units.registry.clear()
    for k, v in original.items():
        units.registry[k] = v
