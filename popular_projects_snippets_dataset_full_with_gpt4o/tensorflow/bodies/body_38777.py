# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/image_ops/extract_image_patches_grad_test.py
with test_util.AbstractGradientTape(use_tape=use_tape) as tape:
    batch_size = 4
    # Prevent OOM by setting reasonably large image size (b/171808681).
    height = 512
    width = 512
    ksize = 5
    shape = (batch_size, height, width, 1)
    images = variables.Variable(
        np.random.uniform(size=np.prod(shape)).reshape(shape), name='inputs')
    tape.watch(images)
    patches = array_ops.extract_image_patches(images,
                                              ksizes=[1, ksize, ksize, 1],
                                              strides=[1, 1, 1, 1],
                                              rates=[1, 1, 1, 1],
                                              padding='SAME')
    # Github issue: #20146
    # tf.image.extract_image_patches() gradient very slow at graph
    # construction time.
    gradients = tape.gradient(patches, images)
    # Won't time out.
    self.assertIsNotNone(gradients)
