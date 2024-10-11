# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/ftrl_ops_test.py
super().setUp()
self.rewrite_ops_for_tpu = ("TPU" in self.device and
                            test_util.is_mlir_bridge_enabled())
