# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numpy_ops/np_random_test.py
onp_dtype = kw_args.pop('onp_dtype', None)
allow_float64 = kw_args.pop('allow_float64', True)
old_allow_float64 = np_dtypes.is_allow_float64()
np_dtypes.set_allow_float64(allow_float64)
old_func = getattr(self, 'onp_func', None)
# TODO(agarwal): Note that onp can return a scalar type while np returns
# ndarrays. Currently np does not support scalar types.
self.onp_func = lambda *args, **kwargs: onp.asarray(  # pylint: disable=g-long-lambda
    old_func(*args, **kwargs))
np_out = self.np_func(*args, **kw_args)
onp_out = onp.asarray(self.onp_func(*args, **kw_args))
if onp_dtype is not None:
    onp_out = onp_out.astype(onp_dtype)
self.assertEqual(np_out.shape, onp_out.shape)
self.assertEqual(np_out.dtype, onp_out.dtype)
np_dtypes.set_allow_float64(old_allow_float64)
