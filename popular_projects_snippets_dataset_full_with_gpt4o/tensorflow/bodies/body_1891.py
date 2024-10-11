# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/image_ops_test.py
# Build an arbitrary RGB image
np.random.seed(7)
batch_size = 5
shape = (batch_size, 2, 7, 3)

for nptype in self.float_types:
    inp = _generate_numpy_random_rgb(shape).astype(nptype)

    # Convert to HSV and back, as a batch and individually
    with self.session() as sess:
        batch0 = array_ops.placeholder(nptype, shape=shape)
        with self.test_scope():
            batch1 = image_ops.rgb_to_hsv(batch0)
            batch2 = image_ops.hsv_to_rgb(batch1)
        split0 = array_ops.unstack(batch0)
        with self.test_scope():
            split1 = list(map(image_ops.rgb_to_hsv, split0))
            split2 = list(map(image_ops.hsv_to_rgb, split1))
        join1 = array_ops.stack(split1)
        join2 = array_ops.stack(split2)
        batch1, batch2, join1, join2 = sess.run([batch1, batch2, join1, join2],
                                                {batch0: inp})

    # Verify that processing batch elements together is the same as separate
    self.assertAllCloseAccordingToType(batch1, join1, half_rtol=0.000002)
    self.assertAllCloseAccordingToType(batch2, join2, half_rtol=0.000002)
    self.assertAllCloseAccordingToType(
        batch2, inp, bfloat16_atol=0.03, half_rtol=0.02)
