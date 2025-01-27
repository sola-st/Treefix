# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/combined_nms_test.py
"""Return the expected engines to build."""
if not run_params.dynamic_shape:
    exit({
        'TRTEngineOp_000': [
            'combined_nms/CombinedNonMaxSuppression', 'max_total_size',
            'iou_threshold', 'score_threshold'
        ]
    })
else:
    # The CombinedNMS op is currently not converted in dynamic shape mode.
    # This branch shall be removed once the converter is updated to handle
    # input with dynamic shape.
    exit(dict())
