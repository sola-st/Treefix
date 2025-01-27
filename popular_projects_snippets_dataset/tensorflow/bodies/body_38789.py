# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/image_ops/extract_volume_patches_grad_test.py
with test_util.AbstractGradientTape(use_tape=use_tape) as tape:
    batch_size = 4
    planes = 8
    height = 32
    width = 32
    ksize = 5
    shape = (batch_size, planes, height, width, 1)

    volumes = variables.Variable(
        np.random.uniform(size=np.prod(shape)).reshape(shape), name='inputs')

    tape.watch(volumes)
    patches = array_ops.extract_volume_patches(
        volumes,
        ksizes=[1, ksize, ksize, ksize, 1],
        strides=[1, 1, 1, 1, 1],
        padding='SAME')
    # Github issue: #20146
    # tf.extract_volume_patches() gradient very slow at graph construction
    # time.
    gradients = tape.gradient(patches, volumes)
    # Won't time out.
    self.assertIsNotNone(gradients)
