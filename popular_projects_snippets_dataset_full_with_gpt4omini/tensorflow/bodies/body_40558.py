# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/ops_test.py
# Uses default
ctx = context.context()
allowed_dtypes = [dtypes.int32, dtypes.int64]

# Follows standard int conversion rules
t, r = execute.args_to_matching_eager([[3, 4]], ctx, allowed_dtypes,
                                      dtypes.int32)
self.assertEqual(t, dtypes.int32)
self.assertEqual(r[0].dtype, dtypes.int32)
t, r = execute.args_to_matching_eager([[3, 4]], ctx, allowed_dtypes,
                                      dtypes.int64)
self.assertEqual(t, dtypes.int32)
self.assertEqual(r[0].dtype, dtypes.int32)
# Use int64 since it is a better fit
t, r = execute.args_to_matching_eager([[2**48]], ctx, allowed_dtypes,
                                      dtypes.int32)
self.assertEqual(t, dtypes.int64)
self.assertEqual(r[0].dtype, dtypes.int64)

# When the regular tensor conversion fails, then use the default type as a
# hint.
allowed_dtypes = [dtypes.uint32, dtypes.uint32]
t, r = execute.args_to_matching_eager([[3, 4]], ctx, allowed_dtypes,
                                      dtypes.uint32)
self.assertEqual(t, dtypes.uint32)
self.assertEqual(r[0].dtype, dtypes.uint32)
t, r = execute.args_to_matching_eager([[3, 4]], ctx, allowed_dtypes,
                                      dtypes.uint64)
self.assertEqual(t, dtypes.uint64)
self.assertEqual(r[0].dtype, dtypes.uint64)

t, r = execute.args_to_matching_eager([], ctx, allowed_dtypes, dtypes.int64)
self.assertEqual(t, dtypes.int64)

# Doesn't use default
allowed_dtypes = [dtypes.int32, dtypes.string]
t, r = execute.args_to_matching_eager([['string', 'arg']], ctx,
                                      allowed_dtypes, dtypes.int32)
self.assertEqual(t, dtypes.string)
self.assertEqual(r[0].dtype, dtypes.string)
