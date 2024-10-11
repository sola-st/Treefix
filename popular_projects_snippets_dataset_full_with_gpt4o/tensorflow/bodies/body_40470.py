# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/backprop_test.py

def forward(a):
    r = max_pooling3d(a, pool_size=pool_size, strides=strides, padding='SAME')
    exit(r)

input_sizes = [1, 3, 2, 4, 1]
pool_size = (2, 2, 1)
strides = (1, 1, 1)

total_size = np.prod(input_sizes)
x = np.arange(1, total_size + 1, dtype=np.float32)
aa = constant_op.constant(x, shape=input_sizes, dtype=dtypes.float32)
da = backprop.gradients_function(forward)(aa)

if not context.executing_eagerly():
    tf_aa = constant_op.constant(x, shape=input_sizes, dtype=dtypes.float32)
    tf_max = max_pooling3d(
        tf_aa, pool_size=pool_size, strides=strides, padding='SAME')
    tf_da = gradients.gradients(tf_max, [tf_aa])
    self.assertAllEqual(da[0], tf_da[0])
