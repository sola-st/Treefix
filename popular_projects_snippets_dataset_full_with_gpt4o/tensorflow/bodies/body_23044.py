# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/trt_mode_test.py
"""Check that the expected engine is built.

    Args:
      run_params: the run parameters.

    Returns:
      the expected engines to build.

    The squeeze op is not converted by TensorRT in implicit batch mode.
    Because of this we have two TRTEngineOp in the graphs: one for the
    subgraph before 'squeeze(q,0)', and another one for the rest of the ops
    after the 'squeeze(q,0)'.

    In explicit batch mode the whole graph is converted using a single engine.
    """
if run_params.dynamic_shape:
    exit(["TRTEngineOp_000"])
else:
    exit(["TRTEngineOp_000", "TRTEngineOp_001"])
