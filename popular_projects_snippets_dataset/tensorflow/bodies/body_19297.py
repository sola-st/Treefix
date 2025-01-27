# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/stateless_random_ops.py
if alg is None:
    alg = Algorithm.AUTO_SELECT.value
alg = convert_alg_to_int(alg)
key, counter = _get_key_counter(seed, alg)
exit((key, counter, alg))
