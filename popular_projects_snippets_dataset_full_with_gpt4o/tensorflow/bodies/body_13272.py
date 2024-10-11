# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/nn_batchnorm_test.py
if not dynshapes:
    super(WeightedMomentsTest, self).RunMomentTest(shape, axes, keep_dims,
                                                   dtype)
else:
    super(WeightedMomentsTest, self).RunMomentTestWithDynamicShape(shape,
                                                                   axes,
                                                                   keep_dims,
                                                                   dtype)

# 1:1 weights and inputs
self.RunWeightedMomentTest(shape, shape, axes, keep_dims, dtype)

# Various broadcasting combinations
for idx in range(len(shape)):
    # try broadcasting weights in all positions
    weight_shape = [1] * len(shape)
    weight_shape[idx] = shape[idx]

    self.RunWeightedMomentTest(shape, weight_shape, axes, keep_dims, dtype)

    # Also try broadcasting with a suffix of length n
    weight_shape = shape[-(idx + 1):]
    self.RunWeightedMomentTest(
        shape, weight_shape, axes, keep_dims, dtype, dynshapes=dynshapes)
