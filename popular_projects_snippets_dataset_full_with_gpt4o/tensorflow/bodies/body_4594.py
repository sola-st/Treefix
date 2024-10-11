# Extracted from ./data/repos/tensorflow/tensorflow/examples/custom_ops_doc/sleep/sleep_bin.py
"""Create a tf.stack of 50 sleep ops.

  Args:
    op: The sleep op, either sleep_op.SyncSleep or sleep_op.AsyncSleep.
    delay: Each op should finish at least float `delay` seconds after it starts.
  """
n = 50
delays = delay + tf.range(0, n, dtype=float) / 10000.0
start_t = time.time()
func = tf.function(lambda: tf.stack([op(delays[i]) for i in range(n)]))
r_numpy = func().numpy()
end_t = time.time()
print('')
print('Total time = %5.3f seconds using %s' % (end_t - start_t, str(op)))
print('Returned values from the ops:')
np.set_printoptions(precision=4, suppress=True)
print(r_numpy)
sys.stdout.flush()
