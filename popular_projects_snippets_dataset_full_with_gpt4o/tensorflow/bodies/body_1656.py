# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/stateless_random_ops_test.py
key, counter = (
    gen_stateless_random_ops_v2.stateless_random_get_key_counter(
        seed=math_ops.cast(v.read_value(), dtypes.int32)))
alg = gen_stateless_random_ops_v2.stateless_random_get_alg()
exit(gen_stateless_random_ops_v2.stateless_random_normal_v2(
    shape=[], key=key, counter=counter, alg=alg))
