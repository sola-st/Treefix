# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/image_ops_test.py
boxes_data = [[[0, 0, 1, 1], [3, 3, 4, 4], [0, 0.4, 1, 1.4],
               [0, 0.6, 1, 1.6], [0, 0.8, 1, 1.8], [0, 2, 1, 2]],
              [[0, 2, 1, 2], [0, 0.8, 1, 1.8], [0, 0.6, 1, 1.6],
               [0, 0.4, 1, 1.4], [0, 0.2, 1, 1.2], [0, 0, 1, 1]]]
scores_data = [[0.9, 0.7, 0.6, 0.5, 0.4, 0.3],
               [0.8, 0.7, 0.6, 0.5, 0.4, 0.3]]
max_output_size = 6
iou_threshold = 0.5
boxes_np = np.array(boxes_data, dtype=np.float32)
scores_np = np.array(scores_data, dtype=np.float32)

with self.session() as sess:
    boxes = array_ops.placeholder(boxes_np.dtype)
    scores = array_ops.placeholder(scores_np.dtype)

    with self.test_scope():
        (indices, num_valid) = image_ops.non_max_suppression_padded(
            boxes=boxes,
            scores=scores,
            max_output_size=max_output_size,
            iou_threshold=iou_threshold,
            pad_to_max_output_size=True,
            sorted_input=True,
            canonicalized_coordinates=True)

    inputs = {boxes: boxes_np, scores: scores_np}
    indices_output, num_valid_output = sess.run([indices, num_valid], inputs)
invalid_index = 0
self.assertAllEqual([[0, 1, 2, 4, 5, invalid_index],
                     [0, 1, 3, 5, invalid_index, invalid_index]],
                    indices_output)
self.assertAllEqual([5, 4], num_valid_output)
