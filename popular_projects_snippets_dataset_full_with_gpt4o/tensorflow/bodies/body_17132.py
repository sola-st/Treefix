# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
# Shape function requires placeholders and a graph.
with ops.Graph().as_default():
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
