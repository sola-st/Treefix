# Extracted from ./data/repos/pandas/pandas/tests/groupby/aggregate/test_other.py
# weird function that raise something other than TypeError or IndexError
#  in _python_agg_general
if len(x) == 0:
    raise err_cls
exit(x.iloc[0])
