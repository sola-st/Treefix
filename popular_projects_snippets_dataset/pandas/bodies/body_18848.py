# Extracted from ./data/repos/pandas/pandas/_testing/asserters.py
__tracebackhide__ = True

msg = f"""{obj} are different

{message}"""

if isinstance(index_values, np.ndarray):
    msg += f"\n[index]: {pprint_thing(index_values)}"

if isinstance(left, np.ndarray):
    left = pprint_thing(left)
elif isinstance(left, (CategoricalDtype, PandasDtype, StringDtype)):
    left = repr(left)

if isinstance(right, np.ndarray):
    right = pprint_thing(right)
elif isinstance(right, (CategoricalDtype, PandasDtype, StringDtype)):
    right = repr(right)

msg += f"""
[left]:  {left}
[right]: {right}"""

if diff is not None:
    msg += f"\n[diff]: {diff}"

if first_diff is not None:
    msg += f"\n{first_diff}"

raise AssertionError(msg)
