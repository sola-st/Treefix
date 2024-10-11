# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
# Ensure the max_output_size_per_class doesn't result in overflows.
boxes = [[[
    [0, 0, 1, 1],
    [0, 0.1, 1, 1.1],
    [0, -0.1, 1, 0.9],
    [0, 10, 1, 11],
    [0, 10.1, 1, 11.1],
    [0, 100, 1, 101],
]]]
scores = [[[0.9, 0.75, 0.6, 0.95, 0.5, 0.3]]]
nmsed_boxes, nmsed_scores, nmsed_classes, valid_detections = (
    image_ops.combined_non_max_suppression(
        boxes=boxes,
        scores=scores,
        max_output_size_per_class=2**31 - 1,
        max_total_size=8,
        pad_per_class=True,
        clip_boxes=False,
    )
)

self.assertAllClose(
    nmsed_boxes,
    [[
        [0, 10, 1, 11],
        [0, 0, 1, 1],
        [0, 0.1, 1.0, 1.1],
        [0, -0.1, 1, 0.9],
        [0, 10.1, 1, 11.1],
        [0, 100, 1, 101],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]],
)
self.assertAllClose(nmsed_classes, [[3, 0, 1, 2, 4, 5, 0, 0]])
self.assertAllClose(
    nmsed_scores, [[0.95, 0.9, 0.75, 0.6, 0.5, 0.3, 0.0, 0.0]]
)
self.assertAllClose(valid_detections, [6])
