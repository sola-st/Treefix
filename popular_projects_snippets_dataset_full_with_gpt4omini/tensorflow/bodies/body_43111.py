# Extracted from ./data/repos/tensorflow/tensorflow/python/util/serialization_test.py
round_trip = json.loads(json.dumps(
    tensor_shape.TensorShape([None, 2, 3]),
    default=serialization.get_json_type))
self.assertIs(round_trip[0], None)
self.assertEqual(round_trip[1], 2)
