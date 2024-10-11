# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/stateful_random_ops.py
"""The 'key' part of the state of a counter-based RNG.

    For a counter-base RNG algorithm such as Philox and ThreeFry (as
    described in paper 'Parallel Random Numbers: As Easy as 1, 2, 3'
    [https://www.thesalmons.org/john/random123/papers/random123sc11.pdf]),
    the RNG state consists of two parts: counter and key. The output is
    generated via the formula: output=hash(key, counter), i.e. a hashing of
    the counter parametrized by the key. Two RNGs with two different keys can
    be thought as generating two independent random-number streams (a stream
    is formed by increasing the counter).

    Returns:
      A scalar which is the 'key' part of the state, if the RNG algorithm is
        counter-based; otherwise it raises a ValueError.
    """
alg = self.algorithm
if alg in (a.value for a in Algorithm):
    exit(self._state_var[-1])
else:
    raise ValueError(stateless_random_ops.unsupported_alg_error_msg(alg))
