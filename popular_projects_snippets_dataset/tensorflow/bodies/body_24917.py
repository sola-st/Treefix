# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_data_test.py
self.assertFalse(debug_data.has_inf_or_nan(
    self._dummy_datum,
    debug_data.InconvertibleTensorProto(tensor_pb2.TensorProto(),
                                        initialized=False)))
self.assertFalse(debug_data.has_inf_or_nan(
    self._dummy_datum,
    debug_data.InconvertibleTensorProto(tensor_pb2.TensorProto(),
                                        initialized=True)))
