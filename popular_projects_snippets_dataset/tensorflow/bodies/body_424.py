# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/testdata/test_file_v0_11.py
with self.cached_session() as s:
    var = tf.Variable([1, 2, 3], dtype=tf.float32)
    s.run(tf.global_variables_initializer())
    x, y = np.meshgrid(np.linspace(-10, 10, 256), np.linspace(-10, 10, 256))
    image = np.sin(x**2 + y**2) / np.sqrt(x**2 + y**2) * .5 + .5
    image = image[None, :, :, None]

    # make a dummy sound
    freq = 440  # A = 440Hz
    sampling_frequency = 11000
    audio = np.sin(2 * np.pi * np.linspace(0, 1, sampling_frequency) * freq)
    audio = audio[None, :, None]
    test_dir = tempfile.mkdtemp()
    # test summaries
    writer = tf.train.SummaryWriter(test_dir)
    summaries = [
        tf.scalar_summary("scalar_var", var[0]),
        tf.scalar_summary("scalar_reduce_var", tf.reduce_sum(var)),
        tf.histogram_summary("var_histogram", var),
        tf.image_summary("sin_image", image),
        tf.audio_summary("sin_wave", audio, sampling_frequency),
    ]
    run_summaries = s.run(summaries)
    writer.add_summary(s.run(tf.merge_summary(inputs=run_summaries)))
    # This is redundant, but we want to be able to rewrite the command
    writer.add_summary(s.run(tf.merge_all_summaries()))
    writer.close()
    shutil.rmtree(test_dir)
