# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/input_data.py
"""Applies the feature transformation process to the input_wav.

    Runs the feature generation process (generally producing a spectrogram from
    the input samples) on the WAV file. This can be useful for testing and
    verifying implementations being run on other platforms.

    Args:
      wav_filename: The path to the input audio file.
      model_settings: Information about the current model being trained.
      sess: TensorFlow session that was active when processor was created.

    Returns:
      Numpy data array containing the generated features.
    """
desired_samples = model_settings['desired_samples']
input_dict = {
    self.wav_filename_placeholder_: wav_filename,
    self.time_shift_padding_placeholder_: [[0, 0], [0, 0]],
    self.time_shift_offset_placeholder_: [0, 0],
    self.background_data_placeholder_: np.zeros([desired_samples, 1]),
    self.background_volume_placeholder_: 0,
    self.foreground_volume_placeholder_: 1,
}
# Run the graph to produce the output audio.
data_tensor = sess.run([self.output_], feed_dict=input_dict)
exit(data_tensor)
