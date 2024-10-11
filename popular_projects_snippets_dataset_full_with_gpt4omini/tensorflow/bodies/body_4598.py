# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_replicated_variable_test.py
batch_size = 32
num_feature_in = 16

x = np.random.rand(batch_size, num_feature_in).astype(np.float32)
w_init = np.random.rand(batch_size, num_feature_in).astype(np.float32)

w0 = variables_lib.Variable(w_init, dtype=dtypes.float32, name='w0')
w1 = variables_lib.Variable(w_init, dtype=dtypes.float32, name='w1')
self.evaluate(variables_lib.global_variables_initializer())
w = tpu_replicated_variable.TPUReplicatedVariable([w0, w1])

# Make a copy of x so that `w` and `x` do not share the same buffer.
# See b/195972684.
self.evaluate(w.assign(x.copy()))
result = self.evaluate(w.read_value())
self.assertAllClose(result, x)
self.check_replicated_variables_all_the_same(w)

x1 = np.random.rand(batch_size, num_feature_in).astype(np.float32)
self.evaluate(w.assign_sub(x1))
result = self.evaluate(w.read_value())
self.assertAllClose(result, np.subtract(x, x1))
self.check_replicated_variables_all_the_same(w)

x2 = np.random.rand(batch_size, num_feature_in).astype(np.float32)
self.evaluate(w.assign(x.copy()))
self.evaluate(w.assign_add(x2))
result = self.evaluate(w.read_value())
self.assertAllClose(result, np.add(x, x2))
self.check_replicated_variables_all_the_same(w)
