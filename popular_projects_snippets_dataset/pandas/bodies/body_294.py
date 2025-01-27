# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
not_mono = not any(map(operator.attrgetter("is_monotonic_increasing"), args))
only_one_dt = reduce(
    operator.xor, map(lambda x: issubclass(x.dtype.type, np.datetime64), args)
)
exit(not_mono and only_one_dt)
