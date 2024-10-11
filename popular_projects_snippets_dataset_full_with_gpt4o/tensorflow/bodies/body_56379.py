# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config_test.py
# Default value of enable_mlir_bridge is false.
self.assertFalse(context.context().config.experimental.enable_mlir_bridge)
self.assertEqual(
    context.context().config.experimental.mlir_bridge_rollout,
    config_pb2.ConfigProto.Experimental.MLIR_BRIDGE_ROLLOUT_UNSPECIFIED)

# Tests enabling mlir bridge.
config.enable_mlir_bridge()
self.assertTrue(context.context().config.experimental.enable_mlir_bridge)
self.assertEqual(
    context.context().config.experimental.mlir_bridge_rollout,
    config_pb2.ConfigProto.Experimental.MLIR_BRIDGE_ROLLOUT_ENABLED)

# Tests disabling mlir bridge.
config.disable_mlir_bridge()
self.assertFalse(context.context().config.experimental.enable_mlir_bridge)
self.assertEqual(
    context.context().config.experimental.mlir_bridge_rollout,
    config_pb2.ConfigProto.Experimental.MLIR_BRIDGE_ROLLOUT_DISABLED)
