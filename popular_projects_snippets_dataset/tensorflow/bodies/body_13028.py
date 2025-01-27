# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_test.py
arr = np.linspace(0., 1, 12).reshape(3, 4)
x_neg_axis = nn_ops.softmax_v2(arr, axis=-2)
y_pos_axis = nn_ops.softmax_v2(arr, axis=0)
z_gt_axis = nn_ops.softmax_v2(arr, axis=0)
x_neg_axis_tf = self.evaluate(x_neg_axis)
y_pos_axis_tf = self.evaluate(y_pos_axis)
z_gt_axis_tf = self.evaluate(z_gt_axis)
eps = 1e-3
self.assertAllClose(x_neg_axis_tf, y_pos_axis_tf, eps)
self.assertAllClose(y_pos_axis_tf, z_gt_axis_tf, eps)
