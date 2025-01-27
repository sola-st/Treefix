# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
# Shape function requires placeholders and a graph.
with ops.Graph().as_default():
    # Test no-op fraction=1.0, with 3-D tensors.
    self._assertShapeInference([50, 60, 3], 1.0, [50, 60, 3])
    self._assertShapeInference([None, 60, 3], 1.0, [None, 60, 3])
    self._assertShapeInference([50, None, 3], 1.0, [50, None, 3])
    self._assertShapeInference([None, None, 3], 1.0, [None, None, 3])
    self._assertShapeInference([50, 60, None], 1.0, [50, 60, None])
    self._assertShapeInference([None, None, None], 1.0, [None, None, None])

    # Test no-op fraction=0.5, with 3-D tensors.
    self._assertShapeInference([50, 60, 3], 0.5, [26, 30, 3])
    self._assertShapeInference([None, 60, 3], 0.5, [None, 30, 3])
    self._assertShapeInference([50, None, 3], 0.5, [26, None, 3])
    self._assertShapeInference([None, None, 3], 0.5, [None, None, 3])
    self._assertShapeInference([50, 60, None], 0.5, [26, 30, None])
    self._assertShapeInference([None, None, None], 0.5, [None, None, None])

    # Test no-op fraction=1.0, with 4-D tensors.
    self._assertShapeInference([5, 50, 60, 3], 1.0, [5, 50, 60, 3])
    self._assertShapeInference([5, None, 60, 3], 1.0, [5, None, 60, 3])
    self._assertShapeInference([5, 50, None, 3], 1.0, [5, 50, None, 3])
    self._assertShapeInference([5, None, None, 3], 1.0, [5, None, None, 3])
    self._assertShapeInference([5, 50, 60, None], 1.0, [5, 50, 60, None])
    self._assertShapeInference([5, None, None, None], 1.0,
                               [5, None, None, None])
    self._assertShapeInference([None, None, None, None], 1.0,
                               [None, None, None, None])

    # Test no-op fraction=0.5, with 4-D tensors.
    self._assertShapeInference([5, 50, 60, 3], 0.5, [5, 26, 30, 3])
    self._assertShapeInference([5, None, 60, 3], 0.5, [5, None, 30, 3])
    self._assertShapeInference([5, 50, None, 3], 0.5, [5, 26, None, 3])
    self._assertShapeInference([5, None, None, 3], 0.5, [5, None, None, 3])
    self._assertShapeInference([5, 50, 60, None], 0.5, [5, 26, 30, None])
    self._assertShapeInference([5, None, None, None], 0.5,
                               [5, None, None, None])
    self._assertShapeInference([None, None, None, None], 0.5,
                               [None, None, None, None])
