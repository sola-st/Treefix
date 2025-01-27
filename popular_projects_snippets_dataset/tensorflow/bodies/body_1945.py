# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/image_ops_test.py
boxes_data = [[0, 0, 1, 1], [0, 0.1, 1, 1.1], [0, -0.1, 1, 0.9],
              [0, 10, 1, 11], [0, 10.1, 1, 11.1], [0, 100, 1, 101]]
boxes_np = np.array(boxes_data, dtype=np.float32)

scores_data = [0.9, 0.75, 0.6, 0.95, 0.5, 0.3]
scores_np = np.array(scores_data, dtype=np.float32)
max_output_size = 6
iou_threshold_np = np.array(0.5, dtype=np.float32)
with self.session() as sess:
    boxes = array_ops.placeholder(boxes_np.dtype, shape=boxes_np.shape)
    scores = array_ops.placeholder(scores_np.dtype, shape=scores_np.shape)
    iou_threshold = array_ops.placeholder(iou_threshold_np.dtype,
                                          iou_threshold_np.shape)
    with self.test_scope():
        selected_indices = image_ops.non_max_suppression_v3(
            boxes=boxes,
            scores=scores,
            max_output_size=max_output_size,
            iou_threshold=iou_threshold,
            score_threshold=float("-inf"))
    inputs_feed = {
        boxes: boxes_np,
        scores: scores_np,
        iou_threshold: iou_threshold_np
    }
    (indices_tf) = sess.run(selected_indices, feed_dict=inputs_feed)

    self.assertEqual(indices_tf.size, 3)
    self.assertAllClose(indices_tf[:3], [3, 0, 5])
