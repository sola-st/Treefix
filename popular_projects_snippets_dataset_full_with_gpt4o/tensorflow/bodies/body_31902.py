# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/losses_test.py
with ops.Graph().as_default():
    random_seed.set_random_seed(0)

    height = 3
    width = 4
    shape = (1, height, width, 1)

    labels0 = random_ops.random_uniform(
        shape, minval=0, maxval=1, dtype=dtypes.float32)
    predictions0 = random_ops.random_uniform(
        shape, minval=0, maxval=1, dtype=dtypes.float32)

    labels1 = random_ops.random_uniform(
        shape, minval=0, maxval=1, dtype=dtypes.float32)
    predictions1 = random_ops.random_uniform(
        shape, minval=0, maxval=1, dtype=dtypes.float32)

    loss0 = losses.mean_pairwise_squared_error(
        labels=labels0,
        predictions=predictions0)
    loss1 = losses.mean_pairwise_squared_error(
        labels=labels1,
        predictions=predictions1)
    loss0_1 = losses.mean_pairwise_squared_error(
        labels=array_ops.concat([labels0, labels1], 0),
        predictions=array_ops.concat([predictions0, predictions1], 0))

    with self.cached_session() as session:
        loss0, loss1, loss0_1 = session.run([loss0, loss1, loss0_1])

        self.assertTrue(loss0 > 0)
        self.assertTrue(loss1 > 0)
        self.assertAlmostEqual(loss0 + loss1, loss0_1, 5)
