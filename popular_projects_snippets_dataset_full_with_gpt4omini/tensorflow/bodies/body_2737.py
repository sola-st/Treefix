# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client_test.py
compiled = self.backend.compile(builder.build())
output_buffers = compiled.execute([
    self.backend.buffer_from_pyval(
        arg, device=compiled.local_devices()[0]) for arg in args
])
self.assertLen(output_buffers, len(expected_results))
for buf, expected in zip(output_buffers, expected_results):
    to_py_result = np.asarray(buf)
    self.assertEqual(expected.shape, to_py_result.shape)
    test_fn(expected, to_py_result)
    if self.backend.platform == "cpu" and buf.dtype != bfloat16:
        mview = memoryview(buf)
        self.assertEqual(expected.shape, mview.shape)
        test_fn(expected, np.asarray(mview))
    else:
        # Buffer protocol expected to fail on non-cpu platforms and bfloat16
        # Note that np.asarray(buf) doesn't throw an exception. To test if the
        # error was thrown properly we must use memoryview(buf).
        with self.assertRaises(BufferError):
            memoryview(buf)
