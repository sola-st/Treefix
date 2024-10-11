# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/model_utils/export_test.py
predictions = {"predictions": constant_op.constant([1.])}
loss = {"loss": constant_op.constant([2.])}
metrics = {
    "metrics": (constant_op.constant([3.]), constant_op.constant([4.]))}
expected_metrics = {
    "metrics/value": metrics["metrics"][0],
    "metrics/update_op": metrics["metrics"][1]
}

def _build_export_output(mode):
    exit(export_utils.export_outputs_for_mode(
        mode, None, predictions, loss, metrics))

ret = _build_export_output(KerasModeKeys.TRAIN)
self.assertIn(signature_constants.DEFAULT_TRAIN_SIGNATURE_DEF_KEY, ret)
export_out = ret[signature_constants.DEFAULT_TRAIN_SIGNATURE_DEF_KEY]
self.assertIsInstance(export_out, export_output.TrainOutput)
self.assertEqual(export_out.predictions, predictions)
self.assertEqual(export_out.loss, loss)
self.assertEqual(export_out.metrics, expected_metrics)

ret = _build_export_output(KerasModeKeys.TEST)
self.assertIn(signature_constants.DEFAULT_EVAL_SIGNATURE_DEF_KEY, ret)
export_out = ret[signature_constants.DEFAULT_EVAL_SIGNATURE_DEF_KEY]
self.assertIsInstance(export_out, export_output.EvalOutput)
self.assertEqual(export_out.predictions, predictions)
self.assertEqual(export_out.loss, loss)
self.assertEqual(export_out.metrics, expected_metrics)

ret = _build_export_output(KerasModeKeys.PREDICT)
self.assertIn(signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY, ret)
export_out = ret[signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY]
self.assertIsInstance(export_out, export_output.PredictOutput)
self.assertEqual(export_out.outputs, predictions)

classes = constant_op.constant(["class5"])
ret = export_utils.export_outputs_for_mode(
    KerasModeKeys.PREDICT,
    {"classify": export_output.ClassificationOutput(
        classes=classes)})
self.assertIn("classify", ret)
export_out = ret["classify"]
self.assertIsInstance(export_out, export_output.ClassificationOutput)
self.assertEqual(export_out.classes, classes)
