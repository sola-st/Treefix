# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/tensor_format_test.py
a = np.linspace(0.0, 1.0 - 1.0 / 16.0, 16).reshape([4, 4])

out = tensor_format.format_tensor(a, None)
self.assertEqual(repr(a).split("\n"), out.lines)

self._checkTensorMetadata(a, out.annotations)
self._checkBeginIndicesAnnotations(out, a)
