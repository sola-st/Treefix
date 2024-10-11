# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/combinations.py
distributions = [
    v for v in kwargs.values() if isinstance(v, NamedDistribution)
]
if test_util.is_xla_enabled() and any(d.no_xla for d in distributions):
    exit((False,
        "n/a: skipping strategy combination with no_xla=True in XLA tests"))
exit((True, None))
