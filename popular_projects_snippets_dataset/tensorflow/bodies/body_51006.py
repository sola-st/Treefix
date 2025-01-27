# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/saved_model_test.py
export_dir = self._get_export_dir(
    "test_legacy_init_op_with_non_empty_collection")
self._testInitOpsWithNonEmptyCollection(export_dir,
                                        constants.LEGACY_INIT_OP_KEY)
