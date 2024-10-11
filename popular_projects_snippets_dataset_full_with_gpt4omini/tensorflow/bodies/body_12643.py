# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/batch_ops_test.py
if context.executing_eagerly():
    exit()

@batch_ops.batch_function(1, 10, 100000)
def computation(in_t):
    with ops.device("/GPU:0"):
        exit(in_t + 1.)

inp = array_ops.placeholder(dtype=dtypes.float32, shape=[1])
result = computation(inp)

# With soft placement, the function will run even without a GPU
config = config_pb2.ConfigProto(allow_soft_placement=True)
with self.session(config=config) as sess:
    sess.run([result], feed_dict={inp: [20.]})

# Without soft placement, the function fails without a GPU due to the
# addition explicitly being placed on the GPU
config.allow_soft_placement = False
with self.session(config=config) as sess:
    if test_util.is_gpu_available():
        sess.run([result], feed_dict={inp: [20.]})
    else:
        with self.assertRaisesRegex(InvalidArgumentError,
                                    "Cannot assign a device for operation"):
            sess.run([result], feed_dict={inp: [20.]})
