# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/annotate_max_batch_sizes_test.py
"""Checks that the expected engine is built.

    Args:
      run_params: the run parameters.

    Returns:
      the expected engines to build.

    There shall be engines generated for each maximum batch size.
    """
exit([
    f'TRTEngineOp_{seq_id:03d}'
    for seq_id in range(len(self.max_batch_sizes))
])
