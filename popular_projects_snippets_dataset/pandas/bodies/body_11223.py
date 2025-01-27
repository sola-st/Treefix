# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_allowlist.py
grp = mframe.groupby(mframe.iloc[:, 0])
names = {_ for _ in dir(grp) if not _.startswith("_")} - set(mframe.columns)
new_names = set(names)
new_names -= reduction_kernels
new_names -= transformation_kernels
new_names -= groupby_other_methods

assert not reduction_kernels & transformation_kernels
assert not reduction_kernels & groupby_other_methods
assert not transformation_kernels & groupby_other_methods

# new public method?
if new_names:
    msg = f"""
There are uncategorized methods defined on the Grouper class:
{new_names}.

Was a new method recently added?

Every public method On Grouper must appear in exactly one the
following three lists defined in pandas.core.groupby.base:
- `reduction_kernels`
- `transformation_kernels`
- `groupby_other_methods`
see the comments in pandas/core/groupby/base.py for guidance on
how to fix this test.
        """
    raise AssertionError(msg)

# removed a public method?
all_categorized = reduction_kernels | transformation_kernels | groupby_other_methods
print(names)
print(all_categorized)
if names != all_categorized:
    msg = f"""
Some methods which are supposed to be on the Grouper class
are missing:
{all_categorized - names}.

They're still defined in one of the lists that live in pandas/core/groupby/base.py.
If you removed a method, you should update them
"""
    raise AssertionError(msg)
