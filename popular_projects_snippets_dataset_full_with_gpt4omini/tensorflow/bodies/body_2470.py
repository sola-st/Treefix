# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/mlir_hlo/tests/python/attributes.py
"""Check that RngAlgorithm attribute is available and usable."""

attr = RngAlgorithmAttr.get("DEFAULT")
assert attr is not None
assert str(attr) == ("#mhlo.rng_algorithm<DEFAULT>")
assert attr.rng_algorithm == "DEFAULT"
