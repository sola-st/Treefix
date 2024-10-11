# Extracted from ./data/repos/tensorflow/tensorflow/core/function/trace_type/trace_type_test.py
context = trace_type.InternalTracingContext()
tensor_a = array_ops.zeros([11, 3, 5],
                           dtype=dtypes.int32).__tf_tracing_type__(context)
tensor_b = array_ops.zeros([11, 4, 5],
                           dtype=dtypes.int32).__tf_tracing_type__(context)
tensor_c = array_ops.zeros(
    [11, 3, 5], dtype=dtypes.float32).__tf_tracing_type__(context)
tensor_d = array_ops.ones([11, 3, 5],
                          dtype=dtypes.int32).__tf_tracing_type__(context)

self.assertNotEqual(tensor_a, tensor_b)
self.assertNotEqual(tensor_a, tensor_c)
self.assertNotEqual(tensor_b, tensor_c)
self.assertEqual(tensor_a, tensor_d)
