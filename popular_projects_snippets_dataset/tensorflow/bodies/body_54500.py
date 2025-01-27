# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
pre_added_input_shapes = self.setUpInputShapes(pre_add_input_shapes=True)
post_added_input_shapes = self.setUpInputShapes(pre_add_input_shapes=False)
self.assertProtoEquals(pre_added_input_shapes, post_added_input_shapes)
