# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/image_ops_test.py
# Build an arbitrary RGB image
np.random.seed(7)
batch_size = 5
shape = (batch_size, 2, 7, 3)

for nptype in [np.float32, np.float64]:
    inp = np.random.rand(*shape).astype(nptype)

    # Convert to YIQ and back, as a batch and individually
    with self.cached_session():
        batch0 = constant_op.constant(inp)
        batch1 = image_ops.rgb_to_yiq(batch0)
        batch2 = image_ops.yiq_to_rgb(batch1)
        split0 = array_ops.unstack(batch0)
        split1 = list(map(image_ops.rgb_to_yiq, split0))
        split2 = list(map(image_ops.yiq_to_rgb, split1))
        join1 = array_ops.stack(split1)
        join2 = array_ops.stack(split2)
        batch1, batch2, join1, join2 = self.evaluate(
            [batch1, batch2, join1, join2])

    # Verify that processing batch elements together is the same as separate
    self.assertAllClose(batch1, join1, rtol=1e-4, atol=1e-4)
    self.assertAllClose(batch2, join2, rtol=1e-4, atol=1e-4)
    self.assertAllClose(batch2, inp, rtol=1e-4, atol=1e-4)
