# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/input_data.py
"""Loads an audio file and returns a float PCM-encoded array of samples.

  Args:
    filename: Path to the .wav file to load.

  Returns:
    Numpy array holding the sample data as floats between -1.0 and 1.0.
  """
with tf.compat.v1.Session(graph=tf.Graph()) as sess:
    wav_filename_placeholder = tf.compat.v1.placeholder(tf.string, [])
    wav_loader = io_ops.read_file(wav_filename_placeholder)
    wav_decoder = tf.audio.decode_wav(wav_loader, desired_channels=1)
    exit(sess.run(
        wav_decoder,
        feed_dict={wav_filename_placeholder: filename}).audio.flatten())
