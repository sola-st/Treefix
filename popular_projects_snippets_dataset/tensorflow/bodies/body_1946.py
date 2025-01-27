# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/image_ops_test.py
num_boxes = 1024
boxes_np = np.random.normal(50, 10, (num_boxes, 4)).astype("f4")
scores_np = np.random.normal(0.5, 0.1, (num_boxes,)).astype("f4")

max_output_size = 128
iou_threshold_np = np.array(0.5, dtype=np.float32)
score_threshold_np = np.array(0.0, dtype=np.float32)

with self.session() as sess:
    boxes = array_ops.placeholder(boxes_np.dtype, shape=boxes_np.shape)
    scores = array_ops.placeholder(scores_np.dtype, shape=scores_np.shape)
    iou_threshold = array_ops.placeholder(iou_threshold_np.dtype,
                                          iou_threshold_np.shape)
    score_threshold = array_ops.placeholder(score_threshold_np.dtype,
                                            score_threshold_np.shape)
    with self.test_scope():
        selected_indices = image_ops.non_max_suppression_padded(
            boxes=boxes,
            scores=scores,
            max_output_size=max_output_size,
            iou_threshold=iou_threshold,
            score_threshold=score_threshold,
            pad_to_max_output_size=True)
    inputs_feed = {
        boxes: boxes_np,
        scores: scores_np,
        score_threshold: score_threshold_np,
        iou_threshold: iou_threshold_np
    }
    (indices_tf, _) = sess.run(selected_indices, feed_dict=inputs_feed)

    self.assertEqual(indices_tf.size, max_output_size)
