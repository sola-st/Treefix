# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/mlir_hlo/tests/python/attributes.py
"""Check that RngDistribution attribute is available and usable."""

attr = RngDistributionAttr.get("UNIFORM")
assert attr is not None
assert str(attr) == ("#mhlo.rng_distribution<UNIFORM>")
assert attr.rng_distribution == "UNIFORM"
