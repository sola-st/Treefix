# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
with self.assertRaisesRegex(TypeError, "config must be a tf.ConfigProto"):
    ops.enable_eager_execution(context.DEVICE_PLACEMENT_SILENT)
with self.assertRaisesRegex(ValueError, "device_policy must be one of"):
    c = config_pb2.ConfigProto()
    ops.enable_eager_execution(c, c)
with self.assertRaisesRegex(ValueError, "execution_mode must be one of"):
    c = config_pb2.ConfigProto()
    ops.enable_eager_execution(c, execution_mode=c)
