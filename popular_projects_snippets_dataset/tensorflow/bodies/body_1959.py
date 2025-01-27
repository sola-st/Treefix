# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/image_ops_test.py
boxes_data = [[[0, 0, 1, 1], [3, 3, 4, 4], [0, 0.4, 1, 1.4],
               [0, 0.6, 1, 1.6], [0, 0.8, 1, 1.8], [0, 2, 1, 2]],
              [[0, 2, 1, 2], [0, 0.8, 1, 1.8], [0, 0.6, 1, 1.6],
               [0, 0.4, 1, 1.4], [0, 0.2, 1, 1.2], [0, 0, 1, 1]]]
scores_data = [[0.9, 0.7, 0.6, 0.4, 0.3, 0.2],
               [0.8, 0.7, 0.6, 0.4, 0.3, 0.1]]
max_output_size = 3
iou_threshold = 0.5
boxes_np = np.array(boxes_data, dtype=np.float32)
scores_np = np.array(scores_data, dtype=np.float32)

with self.session() as sess:
    boxes = array_ops.placeholder(boxes_np.dtype, shape=boxes_np.shape)
    scores = array_ops.placeholder(scores_np.dtype, shape=scores_np.shape)
    with self.test_scope():
        (indices, num_valid) = image_ops.non_max_suppression_padded(
            boxes=boxes,
            scores=scores,
            max_output_size=max_output_size,
            iou_threshold=iou_threshold,
            score_threshold=0.5,
            pad_to_max_output_size=True,
            sorted_input=True,
            canonicalized_coordinates=False)

    inputs = {boxes: boxes_np, scores: scores_np}
    indices_output, num_valid_output = sess.run([indices, num_valid], inputs)
invalid_index = 0
self.assertAllEqual([3, 2], num_valid_output)
self.assertAllEqual([[0, 1, 2], [0, 1, invalid_index]], indices_output)
