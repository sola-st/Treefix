# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2_test.py
text = "tf.train.sdca_fprint(input_tensor)"
expected_text = "tf.raw_ops.SdcaFprint(input=input_tensor)"
_, _, _, new_text = self._upgrade(text)
self.assertEqual(expected_text, new_text)

text = "tf.train.sdca_fprint(input, name=n)"
expected_text = "tf.raw_ops.SdcaFprint(input=input, name=n)"
_, _, _, new_text = self._upgrade(text)
self.assertEqual(expected_text, new_text)

text = "tf.train.sdca_shrink_l1(w, l, ll)"
expected_text = "tf.raw_ops.SdcaShrinkL1(weights=w, l1=l, l2=ll)"
_, _, _, new_text = self._upgrade(text)
self.assertEqual(expected_text, new_text)

text = (
    "tf.train.sdca_optimizer(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o)")
expected_text = (
    "tf.raw_ops.SdcaOptimizer(sparse_example_indices=a, "
    "sparse_feature_indices=b, sparse_feature_values=c, dense_features=d, "
    "example_weights=e, example_labels=f, sparse_indices=g, "
    "sparse_weights=h, dense_weights=i, example_state_data=j, loss_type=k, "
    "l1=l, l2=m, num_loss_partitions=n, num_inner_iterations=o)")
_, _, _, new_text = self._upgrade(text)
self.assertEqual(expected_text, new_text)
