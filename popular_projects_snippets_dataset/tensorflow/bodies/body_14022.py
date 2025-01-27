# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_tensor_test.py
st = StructuredTensor.from_fields({})
partition = row_partition.RowPartition.from_row_splits([0])
with self.assertRaisesRegex(ValueError,
                            r"Shape \(\) must have rank at least 1"):
    st.partition_outer_dimension(partition)

with self.assertRaisesRegex(TypeError,
                            "row_partition must be a RowPartition"):
    st.partition_outer_dimension(10)
