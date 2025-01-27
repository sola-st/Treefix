# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/rnn_cell_test.py
"""Test that number of calls to state and save_state is equal.

    Test if the order of actual evaluating or skipping evaluation of out,
    state tensors, which are the output tensors from static_state_saving_rnn,
    have influence on number of calls to save_state and state methods of
    state_saver object (the number of calls should be same.)
    """
self.skipTest("b/124196246 Breakage for sess.run([out, ...]): 2 != 1")

num_units = 3
batch_size = 2
state_saver = TestStateSaverWithCounters(batch_size, 2 * num_units)
out, state, state_saver = self._factory(scope=None, state_saver=state_saver)

with self.cached_session() as sess:
    sess.run(variables_lib.global_variables_initializer())
    sess.run(variables_lib.local_variables_initializer())

    _, _, num_state_calls, num_save_state_calls = sess.run([
        out,
        state,
        state_saver.num_state_calls,
        state_saver.num_save_state_calls])
    self.assertEqual(num_state_calls, num_save_state_calls)

    _, num_state_calls, num_save_state_calls = sess.run([
        out,
        state_saver.num_state_calls,
        state_saver.num_save_state_calls])
    self.assertEqual(num_state_calls, num_save_state_calls)

    _, num_state_calls, num_save_state_calls = sess.run([
        state,
        state_saver.num_state_calls,
        state_saver.num_save_state_calls])
    self.assertEqual(num_state_calls, num_save_state_calls)
