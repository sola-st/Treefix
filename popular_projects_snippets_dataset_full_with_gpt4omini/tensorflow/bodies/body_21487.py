# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver_test.py
with ops_lib.Graph().as_default():
    v0 = variables.VariableV1([10.0], name="v0")
    v2 = saver_test_utils.CheckpointedOp(name="v2")

    # Saving one variable under two names raises an error.
    with self.assertRaisesRegex(
        ValueError, "The same saveable will be restored with two names: v0"):
        saver_module.Saver({"v0": v0, "v0too": v0})

    # Ditto for custom saveables.
    with self.assertRaisesRegex(
        ValueError, "The same saveable will be restored with two names: v2"):
        saver_module.Saver({"v2": v2.saveable, "v2too": v2.saveable})

    # Verify non-duplicate names work.
    saver_module.Saver({"v0": v0, "v2": v2.saveable})
