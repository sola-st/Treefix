# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/stateful_random_ops_test.py
"""Tests ThreeFry2x32 conforms to known results.
    """
# Based on
# https://github.com/google/jax/blob/8565a3486adf16beb388b2364c9cd930d7a0d92d/tests/random_test.py#L65-L85
# which is in turn based on
# https://github.com/DEShawResearch/Random123-Boost/blob/65e3d874b67aa7b3e02d5ad8306462f52d2079c0/libs/random/test/test_threefry.cpp#L30-L32

with ops.device(xla_device_name()):
    g = random.Generator.from_seed(seed=0, alg=random.RNG_ALG_THREEFRY)
    self._compareToKnownOutputs(
        g,
        [0x00000000, 0x00000000], [0x00000000, 0x00000000],
        [0x6b200159, 0x99ba4efe])
    self._compareToKnownOutputs(
        g,
        [0xffffffff, 0xffffffff], [0xffffffff, 0xffffffff],
        [0x1cb996fc, 0xbb002be7])
    self._compareToKnownOutputs(
        g,
        [0x243f6a88, 0x85a308d3], [0x13198a2e, 0x03707344],
        [0xc4923a9c, 0x483df7a0])
