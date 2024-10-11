# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/combined_nms_test.py
# Parameters
q = 1
batch_size = 2
num_classes = 2
max_total_size = 3

boxes_shape = [batch_size, self.num_boxes, q, 4]
scores_shape = [batch_size, self.num_boxes, num_classes]
nmsed_boxes_shape = [batch_size, max_total_size, 4]
nmsed_scores_shape = [batch_size, max_total_size]
nmsed_classes_shape = [batch_size, max_total_size]
valid_detections_shape = [batch_size]
exit(self.BuildParams(self.GraphFn, dtypes.float32,
                        [boxes_shape, scores_shape], [
                            nmsed_boxes_shape, nmsed_scores_shape,
                            nmsed_classes_shape, valid_detections_shape
                        ]))
