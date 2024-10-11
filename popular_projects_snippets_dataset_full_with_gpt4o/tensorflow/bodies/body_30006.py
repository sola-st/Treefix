# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/constant_op_eager_test.py
ctx = context.context()
device = "GPU:0" if (use_gpu and ctx.num_gpus()) else "CPU:0"
with ops.device(device):
    tf_ans = array_ops.fill(dims, val, name="fill")
    out = tf_ans.numpy()
self.assertAllClose(np_ans, out)
