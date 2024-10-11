# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor_test.py
rt = ragged_factory_ops.constant([[1, 2], [3]])
struct1 = StructuredTensor.from_fields(shape=[], fields={"x": [1, 2]})
struct2 = StructuredTensor.from_fields(shape=[2], fields={"x": [1, 2]})
struct3 = StructuredTensor.from_fields(
    shape=[], fields={
        "r": rt,
        "s": struct1
    })
struct4 = StructuredTensor.from_fields(
    shape=[2], fields={
        "r": rt,
        "s": struct2
    })

self.assertEqual(struct3.shape.as_list(), [])
self.assertEqual(struct3.rank, 0)
self.assertEqual(set(struct3.field_names()), set(["r", "s"]))
self.assertAllEqual(struct3.field_value("r"), rt)
self.assertAllEqual(struct3.field_value("s"), struct1)

self.assertEqual(struct4.shape.as_list(), [2])
self.assertEqual(struct4.rank, 1)
self.assertEqual(set(struct4.field_names()), set(["r", "s"]))
self.assertAllEqual(struct4.field_value("r"), rt)
self.assertAllEqual(struct4.field_value("s"), struct2)
