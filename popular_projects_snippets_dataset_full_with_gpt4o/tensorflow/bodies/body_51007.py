# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/saved_model_test.py
export_dir = self._get_export_dir("test_main_op_with_non_empty_collection")
self._testInitOpsWithNonEmptyCollection(export_dir, constants.MAIN_OP_KEY)
