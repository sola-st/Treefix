# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load_optimizer_test.py
# Make sure that a SavedModel w/ optimizer can be loaded without the Keras
# module imported.
save_path = test.test_src_dir_path(
    "cc/saved_model/testdata/OptimizerSlotVariableModule")
loaded = load.load(save_path)
self.assertIsInstance(
    loaded.opt.get_slot(loaded.v, "v"), variables.Variable)
