# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/checkpoint_test_base.py
sess.run(lookup_ops.tables_initializer())
saver.restore(sess, self._latest_ckpt())
