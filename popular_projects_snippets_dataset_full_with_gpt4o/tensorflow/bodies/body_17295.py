# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
# Test case for GitHub issue 20199.
boxes_np = [[0, 0, 1, 1], [0, 0.1, 1, 1.1], [0, -0.1, 1, 0.9],
            [0, 10, 1, 11], [0, 10.1, 1, 11.1], [0, 100, 1, 101]]
scores_np = [0.9, 0.75, 0.6, 0.95, 0.5, 0.3]
max_output_size_np = 3
iou_threshold_np = 0.5
score_threshold_np = float("-inf")
# Note: There are multiple versions of non_max_suppression v2, v3, v4.
# gen_image_ops.non_max_suppression_v2:
for input_dtype in [np.float16, np.float32]:
    for threshold_dtype in [np.float16, np.float32]:
        with self.cached_session():
            boxes = constant_op.constant(boxes_np, dtype=input_dtype)
            scores = constant_op.constant(scores_np, dtype=input_dtype)
            max_output_size = constant_op.constant(max_output_size_np)
            iou_threshold = constant_op.constant(
                iou_threshold_np, dtype=threshold_dtype)
            selected_indices = gen_image_ops.non_max_suppression_v2(
                boxes, scores, max_output_size, iou_threshold)
            selected_indices = self.evaluate(selected_indices)
            self.assertAllClose(selected_indices, [3, 0, 5])
    # gen_image_ops.non_max_suppression_v3
for input_dtype in [np.float16, np.float32]:
    for threshold_dtype in [np.float16, np.float32]:
        # XLA currently requires dtypes to be equal.
        if input_dtype == threshold_dtype or not test_util.is_xla_enabled():
            with self.cached_session():
                boxes = constant_op.constant(boxes_np, dtype=input_dtype)
                scores = constant_op.constant(scores_np, dtype=input_dtype)
                max_output_size = constant_op.constant(max_output_size_np)
                iou_threshold = constant_op.constant(
                    iou_threshold_np, dtype=threshold_dtype)
                score_threshold = constant_op.constant(
                    score_threshold_np, dtype=threshold_dtype)
                selected_indices = gen_image_ops.non_max_suppression_v3(
                    boxes, scores, max_output_size, iou_threshold, score_threshold)
                selected_indices = self.evaluate(selected_indices)
                self.assertAllClose(selected_indices, [3, 0, 5])
    # gen_image_ops.non_max_suppression_v4.
for input_dtype in [np.float16, np.float32]:
    for threshold_dtype in [np.float16, np.float32]:
        with self.cached_session():
            boxes = constant_op.constant(boxes_np, dtype=input_dtype)
            scores = constant_op.constant(scores_np, dtype=input_dtype)
            max_output_size = constant_op.constant(max_output_size_np)
            iou_threshold = constant_op.constant(
                iou_threshold_np, dtype=threshold_dtype)
            score_threshold = constant_op.constant(
                score_threshold_np, dtype=threshold_dtype)
            selected_indices, _ = gen_image_ops.non_max_suppression_v4(
                boxes, scores, max_output_size, iou_threshold, score_threshold)
            selected_indices = self.evaluate(selected_indices)
            self.assertAllClose(selected_indices, [3, 0, 5])
    # gen_image_ops.non_max_suppression_v5.
soft_nms_sigma_np = float(0.0)
for dtype in [np.float16, np.float32]:
    with self.cached_session():
        boxes = constant_op.constant(boxes_np, dtype=dtype)
        scores = constant_op.constant(scores_np, dtype=dtype)
        max_output_size = constant_op.constant(max_output_size_np)
        iou_threshold = constant_op.constant(iou_threshold_np, dtype=dtype)
        score_threshold = constant_op.constant(score_threshold_np, dtype=dtype)
        soft_nms_sigma = constant_op.constant(soft_nms_sigma_np, dtype=dtype)
        selected_indices, _, _ = gen_image_ops.non_max_suppression_v5(
            boxes, scores, max_output_size, iou_threshold, score_threshold,
            soft_nms_sigma)
        selected_indices = self.evaluate(selected_indices)
        self.assertAllClose(selected_indices, [3, 0, 5])
