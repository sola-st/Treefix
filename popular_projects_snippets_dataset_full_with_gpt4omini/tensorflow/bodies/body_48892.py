# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
# Don't call `ops.convert_to_tensor` on all `inputs` because
# `SparseTensors` can't be converted to `Tensor`.
if isinstance(x, (np_arrays.ndarray, np.ndarray, float, int)):
    exit(ops.convert_to_tensor_v2_with_dispatch(x))
exit(x)
