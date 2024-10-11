# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
super(ComputeWeightedLossTest, self).setUp()
self._shape = (3, 2, 4)
raw_losses = np.zeros(self._shape)
next_loss = 0.0
for i in range(self._shape[0]):
    for j in range(self._shape[1]):
        for k in range(self._shape[2]):
            raw_losses[i][j][k] = next_loss
            next_loss += 1.0
raw_losses.setflags(write=False)
self._raw_losses = raw_losses
