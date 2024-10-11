# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
# Shape function requires placeholders and a graph.
with ops.Graph().as_default():
    # Test with 3-D tensors.
    self._assertShapeInference([55, 66, 3], 55, 66, [55, 66, 3])
    self._assertShapeInference([50, 60, 3], 55, 66, [55, 66, 3])
    self._assertShapeInference([None, 66, 3], 55, 66, [55, 66, 3])
    self._assertShapeInference([None, 60, 3], 55, 66, [55, 66, 3])
    self._assertShapeInference([55, None, 3], 55, 66, [55, 66, 3])
    self._assertShapeInference([50, None, 3], 55, 66, [55, 66, 3])
    self._assertShapeInference([None, None, 3], 55, 66, [55, 66, 3])
    self._assertShapeInference([55, 66, None], 55, 66, [55, 66, None])
    self._assertShapeInference([50, 60, None], 55, 66, [55, 66, None])
    self._assertShapeInference([None, None, None], 55, 66, [55, 66, None])
    self._assertShapeInference(None, 55, 66, [55, 66, None])

    # Test with 4-D tensors.
    self._assertShapeInference([5, 55, 66, 3], 55, 66, [5, 55, 66, 3])
    self._assertShapeInference([5, 50, 60, 3], 55, 66, [5, 55, 66, 3])
    self._assertShapeInference([5, None, 66, 3], 55, 66, [5, 55, 66, 3])
    self._assertShapeInference([5, None, 60, 3], 55, 66, [5, 55, 66, 3])
    self._assertShapeInference([5, 55, None, 3], 55, 66, [5, 55, 66, 3])
    self._assertShapeInference([5, 50, None, 3], 55, 66, [5, 55, 66, 3])
    self._assertShapeInference([5, None, None, 3], 55, 66, [5, 55, 66, 3])
    self._assertShapeInference([5, 55, 66, None], 55, 66, [5, 55, 66, None])
    self._assertShapeInference([5, 50, 60, None], 55, 66, [5, 55, 66, None])
    self._assertShapeInference([5, None, None, None], 55, 66,
                               [5, 55, 66, None])
    self._assertShapeInference([None, None, None, None], 55, 66,
                               [None, 55, 66, None])
