# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
@def_function.function
def test_fn():
    ds = dataset_ops.Dataset.range(3)._variant_tensor

    ds.op.experimental_set_type(
        full_type_pb2.FullTypeDef(type_id=full_type_pb2.TFT_PRODUCT))

    self.assertEqual(ds.op.node_def.experimental_type.type_id,
                     full_type_pb2.TFT_PRODUCT)

test_fn()
