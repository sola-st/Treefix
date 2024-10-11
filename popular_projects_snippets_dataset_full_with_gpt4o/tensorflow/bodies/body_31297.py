# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
wrapper_type = rnn_cell_impl.DropoutWrapper
keep_some = 0.5
random_seed.set_random_seed(2)
## Use parallel_iterations = 1 in both calls to
## _testDropoutWrapper to ensure the (per-time step) dropout is
## consistent across both calls.  Otherwise the seed may not end
## up being munged consistently across both graphs.
res_standard_1 = self._testDropoutWrapper(
    input_keep_prob=keep_some,
    output_keep_prob=keep_some,
    state_keep_prob=keep_some,
    seed=10,
    parallel_iterations=1,
    wrapper_type=wrapper_type,
    scope="root_1")
random_seed.set_random_seed(2)
res_standard_2 = self._testDropoutWrapper(
    input_keep_prob=keep_some,
    output_keep_prob=keep_some,
    state_keep_prob=keep_some,
    seed=10,
    parallel_iterations=1,
    wrapper_type=wrapper_type,
    scope="root_2")
self.assertAllClose(res_standard_1[0], res_standard_2[0])
self.assertAllClose(res_standard_1[1].c, res_standard_2[1].c)
self.assertAllClose(res_standard_1[1].h, res_standard_2[1].h)
