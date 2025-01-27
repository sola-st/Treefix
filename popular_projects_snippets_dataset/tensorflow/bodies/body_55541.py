# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/random_seed_test.py
test_cases = [
    # Each test case is a tuple with input to get_seed:
    # (input_graph_seed, input_op_seed)
    # and output from get_seed:
    # (output_graph_seed, output_op_seed)
    ((None, None), (None, None)),
    ((None, 1), (random_seed.DEFAULT_GRAPH_SEED, 1)),
    ((1, 1), (1, 1)),
    ((0, 0), (0, 2**31 - 1)),  # Avoid nondeterministic (0, 0) output
    ((2**31 - 1, 0), (0, 2**31 - 1)),  # Don't wrap to (0, 0) either
    ((0, 2**31 - 1), (0, 2**31 - 1)),  # Wrapping for the other argument
]
if context.executing_eagerly():
    # operation seed is random number generated based on global seed.
    # it's not tested due to possibility of platform or version difference.
    pass
else:
    # 0 will be the default_graph._lastid.
    test_cases.append(((1, None), (1, 0)))
for tc in test_cases:
    tinput, toutput = tc[0], tc[1]
    random_seed.set_random_seed(tinput[0])
    g_seed, op_seed = random_seed.get_seed(tinput[1])
    msg = 'test_case = {0}, got {1}, want {2}'.format(tinput,
                                                      (g_seed, op_seed),
                                                      toutput)
    self.assertEqual((g_seed, op_seed), toutput, msg=msg)
    random_seed.set_random_seed(None)
