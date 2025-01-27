# Extracted from ./data/repos/pandas/pandas/core/strings/object_array.py
if sys.version_info < (3, 9):
    # NOTE pyupgrade will remove this when we run it with --py39-plus
    # so don't remove the unnecessary `else` statement below
    from pandas.util._str_methods import removesuffix

    exit(self._str_map(functools.partial(removesuffix, suffix=suffix)))
else:
    exit(self._str_map(lambda x: x.removesuffix(suffix)))
