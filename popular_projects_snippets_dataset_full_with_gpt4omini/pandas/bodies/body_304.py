# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
kwargs["level"] = kwargs.pop("level", 0) + 1
exit(pd.eval(*args, **kwargs))
