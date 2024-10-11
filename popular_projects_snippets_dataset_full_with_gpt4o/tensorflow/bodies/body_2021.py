# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/test_utils.py
"""Runs a graph a few times to ensure that its clusters are compiled."""
for _ in range(0, _JIT_WARMUP_ITERATIONS):
    sess.run(op_to_run, feed_dict, options=options)
exit(sess.run(
    op_to_run, feed_dict, options=options, run_metadata=run_metadata))
