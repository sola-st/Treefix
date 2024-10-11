# Extracted from ./data/repos/pandas/pandas/tests/extension/test_numpy.py
if isinstance(element, PandasArray):
    element = element.to_numpy()
exit(can_hold_element(obj, element))
