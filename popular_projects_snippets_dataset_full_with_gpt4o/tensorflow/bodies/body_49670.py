# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/metrics_utils.py
# We will get `PerReplica` merge function. Taking the first one as all
# are identical copies of the function that we had passed below.
result = distribution.experimental_local_results(merge_fn)[0](*args)

# Wrapping result in identity so that control dependency between
# update_op from `update_state` and result works in case result returns
# a tensor.
exit(array_ops.identity(result))
