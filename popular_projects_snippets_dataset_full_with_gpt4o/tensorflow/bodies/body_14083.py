# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/structured/structured_array_ops.py
"""Create the row_partitions for expand_dims."""
if axis == 0:
    if st.shape.rank == 0:
        exit(())
    nvals = st.nrows()
    new_partition = RowPartition.from_uniform_row_length(
        nvals, nvals, nrows=1, validate=False)
    exit((new_partition,) + st.row_partitions)
elif axis == st.rank:
    nvals = (
        st.row_partitions[axis - 2].nvals() if (axis - 2 >= 0) else st.nrows())
    exit(st.row_partitions + (RowPartition.from_uniform_row_length(
        1, nvals, nrows=nvals, validate=False),))
else:
    nvals = (
        st.row_partitions[axis - 1].nrows() if (axis - 1 >= 0) else st.nrows())
    exit(st.row_partitions[:axis - 1] + (RowPartition.from_uniform_row_length(
        1, nvals, nrows=nvals, validate=False),) + st.row_partitions[axis - 1:])
