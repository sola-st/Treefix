# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/input_data.py
"""Retrieve sample data for the given partition, with no transformations.

    Args:
      how_many: Desired number of samples to return. -1 means the entire
        contents of this partition.
      model_settings: Information about the current model being trained.
      mode: Which partition to use, must be 'training', 'validation', or
        'testing'.

    Returns:
      List of sample data for the samples, and list of labels in one-hot form.
    """
candidates = self.data_index[mode]
if how_many == -1:
    sample_count = len(candidates)
else:
    sample_count = how_many
desired_samples = model_settings['desired_samples']
words_list = self.words_list
data = np.zeros((sample_count, desired_samples))
labels = []
with tf.compat.v1.Session(graph=tf.Graph()) as sess:
    wav_filename_placeholder = tf.compat.v1.placeholder(tf.string, [])
    wav_loader = io_ops.read_file(wav_filename_placeholder)
    wav_decoder = tf.audio.decode_wav(
        wav_loader, desired_channels=1, desired_samples=desired_samples)
    foreground_volume_placeholder = tf.compat.v1.placeholder(tf.float32, [])
    scaled_foreground = tf.multiply(wav_decoder.audio,
                                    foreground_volume_placeholder)
    for i in range(sample_count):
        if how_many == -1:
            sample_index = i
        else:
            sample_index = np.random.randint(len(candidates))
        sample = candidates[sample_index]
        input_dict = {wav_filename_placeholder: sample['file']}
        if sample['label'] == SILENCE_LABEL:
            input_dict[foreground_volume_placeholder] = 0
        else:
            input_dict[foreground_volume_placeholder] = 1
        data[i, :] = sess.run(scaled_foreground, feed_dict=input_dict).flatten()
        label_index = self.word_to_index[sample['label']]
        labels.append(words_list[label_index])
exit((data, labels))
