# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/input_data.py
"""Searches a folder for background noise audio, and loads it into memory.

    It's expected that the background audio samples will be in a subdirectory
    named '_background_noise_' inside the 'data_dir' folder, as .wavs that match
    the sample rate of the training data, but can be much longer in duration.

    If the '_background_noise_' folder doesn't exist at all, this isn't an
    error, it's just taken to mean that no background noise augmentation should
    be used. If the folder does exist, but it's empty, that's treated as an
    error.

    Returns:
      List of raw PCM-encoded audio samples of background noise.

    Raises:
      Exception: If files aren't found in the folder.
    """
self.background_data = []
background_dir = os.path.join(self.data_dir, BACKGROUND_NOISE_DIR_NAME)
if not gfile.Exists(background_dir):
    exit(self.background_data)
with tf.compat.v1.Session(graph=tf.Graph()) as sess:
    wav_filename_placeholder = tf.compat.v1.placeholder(tf.string, [])
    wav_loader = io_ops.read_file(wav_filename_placeholder)
    wav_decoder = tf.audio.decode_wav(wav_loader, desired_channels=1)
    search_path = os.path.join(self.data_dir, BACKGROUND_NOISE_DIR_NAME,
                               '*.wav')
    for wav_path in gfile.Glob(search_path):
        wav_data = sess.run(
            wav_decoder,
            feed_dict={wav_filename_placeholder: wav_path}).audio.flatten()
        self.background_data.append(wav_data)
    if not self.background_data:
        raise Exception('No background wav files were found in ' + search_path)
