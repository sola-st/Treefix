# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_values_test.py
if context.num_gpus() < 1 and context.executing_eagerly():
    # Graph mode can work without GPU because the Placer "moves" the
    # variable to a CPU. In other words, if there is no GPU available, but
    # user requested to create a variable on GPU, Placer will ignore the
    # user request and assign the VarHandleOp to CPU. This requires
    # soft_placement, which is on by default.
    self.skipTest("A GPU is not available for this test in eager mode.")

save_path = self._save_mirrored(distribution)
self._restore_mirrored(save_path, distribution)
