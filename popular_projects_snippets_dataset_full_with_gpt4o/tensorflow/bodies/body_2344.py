# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/stateful_random_ops_test.py
"""Tests Philox4x32 conforms to known results.
    """
# Based on
# https://github.com/DEShawResearch/Random123-Boost/blob/65e3d874b67aa7b3e02d5ad8306462f52d2079c0/libs/random/test/test_philox.cpp#L50-L52

with ops.device(xla_device_name()):
    g = random.Generator.from_seed(seed=0, alg=random.RNG_ALG_PHILOX)
    self._compareToKnownOutputs(
        g,
        [0x00000000, 0x00000000, 0x00000000, 0x00000000],
        [0x00000000, 0x00000000],
        [0x6627e8d5, 0xe169c58d, 0xbc57ac4c, 0x9b00dbd8])
    self._compareToKnownOutputs(
        g,
        [0xffffffff, 0xffffffff, 0xffffffff, 0xffffffff],
        [0xffffffff, 0xffffffff],
        [0x408f276d, 0x41c83b0e, 0xa20bc7c6, 0x6d5451fd])
    self._compareToKnownOutputs(
        g,
        [0x243f6a88, 0x85a308d3, 0x13198a2e, 0x03707344],
        [0xa4093822, 0x299f31d0],
        [0xd16cfe09, 0x94fdcceb, 0x5001e420, 0x24126ea1])
