# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/input_data.py
"""Gather samples from the data set, applying transformations as needed.

    When the mode is 'training', a random selection of samples will be returned,
    otherwise the first N clips in the partition will be used. This ensures that
    validation always uses the same samples, reducing noise in the metrics.

    Args:
      how_many: Desired number of samples to return. -1 means the entire
        contents of this partition.
      offset: Where to start when fetching deterministically.
      model_settings: Information about the current model being trained.
      background_frequency: How many clips will have background noise, 0.0 to
        1.0.
      background_volume_range: How loud the background noise will be.
      time_shift: How much to randomly shift the clips by in time.
      mode: Which partition to use, must be 'training', 'validation', or
        'testing'.
      sess: TensorFlow session that was active when processor was created.

    Returns:
      List of sample data for the transformed samples, and list of label indexes

    Raises:
      ValueError: If background samples are too short.
    """
# Pick one of the partitions to choose samples from.
candidates = self.data_index[mode]
if how_many == -1:
    sample_count = len(candidates)
else:
    sample_count = max(0, min(how_many, len(candidates) - offset))
# Data and labels will be populated and returned.
data = np.zeros((sample_count, model_settings['fingerprint_size']))
labels = np.zeros(sample_count)
desired_samples = model_settings['desired_samples']
use_background = self.background_data and (mode == 'training')
pick_deterministically = (mode != 'training')
# Use the processing graph we created earlier to repeatedly to generate the
# final output sample data we'll use in training.
for i in range(offset, offset + sample_count):
    # Pick which audio sample to use.
    if how_many == -1 or pick_deterministically:
        sample_index = i
    else:
        sample_index = np.random.randint(len(candidates))
    sample = candidates[sample_index]
    # If we're time shifting, set up the offset for this sample.
    if time_shift > 0:
        time_shift_amount = np.random.randint(-time_shift, time_shift)
    else:
        time_shift_amount = 0
    if time_shift_amount > 0:
        time_shift_padding = [[time_shift_amount, 0], [0, 0]]
        time_shift_offset = [0, 0]
    else:
        time_shift_padding = [[0, -time_shift_amount], [0, 0]]
        time_shift_offset = [-time_shift_amount, 0]
    input_dict = {
        self.wav_filename_placeholder_: sample['file'],
        self.time_shift_padding_placeholder_: time_shift_padding,
        self.time_shift_offset_placeholder_: time_shift_offset,
    }
    # Choose a section of background noise to mix in.
    if use_background or sample['label'] == SILENCE_LABEL:
        background_index = np.random.randint(len(self.background_data))
        background_samples = self.background_data[background_index]
        if len(background_samples) <= model_settings['desired_samples']:
            raise ValueError(
                'Background sample is too short! Need more than %d'
                ' samples but only %d were found' %
                (model_settings['desired_samples'], len(background_samples)))
        background_offset = np.random.randint(
            0, len(background_samples) - model_settings['desired_samples'])
        background_clipped = background_samples[background_offset:(
            background_offset + desired_samples)]
        background_reshaped = background_clipped.reshape([desired_samples, 1])
        if sample['label'] == SILENCE_LABEL:
            background_volume = np.random.uniform(0, 1)
        elif np.random.uniform(0, 1) < background_frequency:
            background_volume = np.random.uniform(0, background_volume_range)
        else:
            background_volume = 0
    else:
        background_reshaped = np.zeros([desired_samples, 1])
        background_volume = 0
    input_dict[self.background_data_placeholder_] = background_reshaped
    input_dict[self.background_volume_placeholder_] = background_volume
    # If we want silence, mute out the main sample but leave the background.
    if sample['label'] == SILENCE_LABEL:
        input_dict[self.foreground_volume_placeholder_] = 0
    else:
        input_dict[self.foreground_volume_placeholder_] = 1
    # Run the graph to produce the output audio.
    summary, data_tensor = sess.run(
        [self.merged_summaries_, self.output_], feed_dict=input_dict)
    self.summary_writer_.add_summary(summary)
    data[i - offset, :] = data_tensor.flatten()
    label_index = self.word_to_index[sample['label']]
    labels[i - offset] = label_index
exit((data, labels))
