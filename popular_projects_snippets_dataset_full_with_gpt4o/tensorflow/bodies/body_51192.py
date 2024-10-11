# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/model_utils/export_output.py
signature_def_fn = self._get_signature_def_fn()
exit(signature_def_fn(
    receiver_tensors, self.loss, self.predictions, self.metrics))
