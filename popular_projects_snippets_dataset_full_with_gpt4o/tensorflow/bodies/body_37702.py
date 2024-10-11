# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/checkpoint_ops_test.py
"""Tests offset and num_new_vocab logic."""
remapping, num_present = gen_checkpoint_ops.generate_vocab_remapping(
    new_vocab_file=self.new_vocab_file,
    old_vocab_file=self.old_vocab_file,
    num_new_vocab=1,
    new_vocab_offset=1)
expected_remapping = [0]
expected_num_present = 1
with self.cached_session():
    self.assertAllEqual(expected_remapping, self.evaluate(remapping))
    self.assertAllEqual(expected_num_present, self.evaluate(num_present))
