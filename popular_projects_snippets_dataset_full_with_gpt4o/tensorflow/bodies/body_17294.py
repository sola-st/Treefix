# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
with context.eager_mode():
    boxes_tensor = constant_op.constant([[6.625, 6.688, 272., 158.5],
                                         [6.625, 6.75, 270.5, 158.4],
                                         [5.375, 5., 272., 157.5]])
    scores_tensor = constant_op.constant([0.84, 0.7944, 0.7715])
    max_output_size = 100
    iou_threshold = 0.5
    score_threshold = 0.3
    soft_nms_sigma = 0.25
    pad_to_max_output_size = False

    # gen_image_ops.non_max_suppression_v5.
    for dtype in [np.float16, np.float32]:
        boxes = math_ops.cast(boxes_tensor, dtype=dtype)
        scores = math_ops.cast(scores_tensor, dtype=dtype)
        _, _, num_selected = gen_image_ops.non_max_suppression_v5(
            boxes, scores, max_output_size, iou_threshold, score_threshold,
            soft_nms_sigma, pad_to_max_output_size)
        self.assertEqual(num_selected.numpy(), 1)
