# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
with self.cached_session():
    # Verifies that thresholds passed in to the `thresholds` parameter are
    # used correctly.
    # The default thresholds do not split the second and third predictions.
    # Thus, when we provide manual thresholds which correctly split it, we get
    # an accurate AUC value.
    predictions = constant_op.constant(
        [0.12, 0.3001, 0.3003, 0.72], shape=(1, 4), dtype=dtypes_lib.float32)
    labels = constant_op.constant([0, 1, 0, 1], shape=(1, 4))
    weights = constant_op.constant([1, 1, 1, 1], shape=(1, 4))
    thresholds = [0.0, 0.2, 0.3002, 0.6, 1.0]
    default_auc, default_update_op = metrics.auc(labels,
                                                 predictions,
                                                 weights=weights)
    manual_auc, manual_update_op = metrics.auc(labels,
                                               predictions,
                                               weights=weights,
                                               thresholds=thresholds)

    self.evaluate(variables.local_variables_initializer())
    self.assertAlmostEqual(0.875, self.evaluate(default_update_op), 3)
    self.assertAlmostEqual(0.875, self.evaluate(default_auc), 3)

    self.assertAlmostEqual(0.75, self.evaluate(manual_update_op), 3)
    self.assertAlmostEqual(0.75, self.evaluate(manual_auc), 3)
