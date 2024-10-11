# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config_test.py
# Default value of enable_mlir_bridge is false.
self.assertFalse(context.context().config.experimental.enable_mlir_bridge)
self.assertEqual(
    context.context().config.experimental.mlir_bridge_rollout,
    config_pb2.ConfigProto.Experimental.MLIR_BRIDGE_ROLLOUT_UNSPECIFIED)
