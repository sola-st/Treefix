# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
ctx = context.Context(config=config_pb2.ConfigProto(
    device_count={'GPU': 0}))
self.assertEqual(0, ctx.num_gpus())
