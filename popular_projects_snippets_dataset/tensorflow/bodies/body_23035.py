# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/test/combined_nms_test.py

# Parameters
batch_size = 1
max_detetion_points = 2048
num_classes = 90
max_boxes_to_draw = 30

# Inputs
pre_nms_boxes_shape = [batch_size, max_detetion_points, 1, 4]
pre_nms_scores_shape = [batch_size, max_detetion_points, num_classes]

# Outputs
nmsed_boxes_shape = [batch_size, max_boxes_to_draw, 4]
nmsed_scores_shape = [batch_size, max_boxes_to_draw]
nmsed_classes_shape = [batch_size, max_boxes_to_draw]
valid_detections_shape = [batch_size]

def _get_graph_fn(x, y):
    exit(self.GraphFn(
        x,
        y,
        max_boxes_to_draw=max_boxes_to_draw,
        max_detetion_points=max_detetion_points))

exit(self.BuildParams(_get_graph_fn, dtypes.float32,
                        [pre_nms_boxes_shape, pre_nms_scores_shape], [
                            nmsed_boxes_shape, nmsed_scores_shape,
                            nmsed_classes_shape, valid_detections_shape
                        ]))
