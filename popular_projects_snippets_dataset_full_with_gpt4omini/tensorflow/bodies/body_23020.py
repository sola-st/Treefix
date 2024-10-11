# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/rank_two_test.py
"""Return the expected engines to build."""
expected_engines = {
    "TRTEngineOp_000": [
        "add0_1", "add0_2", "add0_3", "c0_1", "c0_2", "c0_3", "abs0_1",
        "abs0_2", "expand0_0", "expand0_1", "axis"
    ],
    "TRTEngineOp_001": [
        "add1_1", "add1_2", "add1_3", "c1_1", "c1_2", "c1_3", "abs1_1",
        "abs1_2", "reciprocal1"
    ]
}
if not run_params.dynamic_shape:
    # The two ops can't be in the same cluster as the ops in TRTEngineOp_000
    # due to trt_incompatible_op. They can't be in the same cluster as the
    # ops in TRTEngineOP_1 because their batch size belongs to a different
    # equivalent class.
    expected_engines["TRTEngineOp_002"] = ["add", "reciprocal0"]
else:
    # In dynamic shape mode the batch size of the ops can differ,
    # therefore the final ops will be merged to TRTEngineOP_1.
    expected_engines["TRTEngineOp_001"] += ["add", "reciprocal0"]

exit(expected_engines)
