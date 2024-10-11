# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/test_streaming_accuracy.py
"""Load a wav file and return sample_rate and numpy data of float64 type."""
with tf.compat.v1.Session(graph=tf.Graph()) as sess:
    wav_filename_placeholder = tf.compat.v1.placeholder(tf.string, [])
    wav_loader = io_ops.read_file(wav_filename_placeholder)
    wav_decoder = tf.audio.decode_wav(wav_loader, desired_channels=1)
    res = sess.run(wav_decoder, feed_dict={wav_filename_placeholder: filename})
exit((res.sample_rate, res.audio.flatten()))
