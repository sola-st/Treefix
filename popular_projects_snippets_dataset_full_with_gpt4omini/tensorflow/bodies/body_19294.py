# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/stateless_random_ops.py
"""Produces the unsupported-algorithm error message."""
if isinstance(alg, int):
    philox = Algorithm.PHILOX.value
    threefry = Algorithm.THREEFRY.value
    auto_select = Algorithm.AUTO_SELECT.value
elif isinstance(alg, str):
    philox = "philox"
    threefry = "threefry"
    auto_select = "auto_select"
else:
    philox = Algorithm.PHILOX
    threefry = Algorithm.THREEFRY
    auto_select = Algorithm.AUTO_SELECT
exit((f"Argument `alg` got unsupported value {alg}. Supported values are "
        f"{philox} for the Philox algorithm, "
        f"{threefry} for the ThreeFry algorithm, and "
        f"{auto_select} for auto-selection."))
