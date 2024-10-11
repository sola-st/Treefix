# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/cond_v2_test.py
if not feed_dict:
    feed_dict = {}
with self.session(graph=ops.get_default_graph()) as sess:
    pred = array_ops.placeholder(dtypes.bool, name="pred")

    expected = control_flow_ops.cond(
        array_ops.squeeze_v2(pred), true_fn, false_fn, name="expected")
    actual = cond_v2.cond_v2(pred, true_fn, false_fn, name="actual")

    expected_grad = gradients_impl.gradients(expected, train_vals)
    actual_grad = gradients_impl.gradients(actual, train_vals)

    sess_run_args = {pred: True}
    sess_run_args.update(feed_dict)
    expected_val, actual_val, expected_grad_val, actual_grad_val = sess.run(
        (expected, actual, expected_grad, actual_grad), sess_run_args)
    self.assertEqual(expected_val, actual_val)
    self.assertEqual(expected_grad_val, actual_grad_val)

    sess_run_args = {pred: [[True]]}
    sess_run_args.update(feed_dict)
    expected_val, actual_val, expected_grad_val, actual_grad_val = sess.run(
        (expected, actual, expected_grad, actual_grad), sess_run_args)
    self.assertEqual(expected_val, actual_val)
    self.assertEqual(expected_grad_val, actual_grad_val)

    sess_run_args = {pred: False}
    sess_run_args.update(feed_dict)
    expected_val, actual_val, expected_grad_val, actual_grad_val = sess.run(
        (expected, actual, expected_grad, actual_grad), sess_run_args)
    self.assertEqual(expected_val, actual_val)
    self.assertEqual(expected_grad_val, actual_grad_val)

    sess_run_args = {pred: [[False]]}
    sess_run_args.update(feed_dict)
    expected_val, actual_val, expected_grad_val, actual_grad_val = sess.run(
        (expected, actual, expected_grad, actual_grad), sess_run_args)
    self.assertEqual(expected_val, actual_val)
    self.assertEqual(expected_grad_val, actual_grad_val)
