# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/label_wav_test.py
with self.cached_session():
    sample_data = tf.zeros([1000, 2])
    wav_encoder = tf.audio.encode_wav(sample_data, 16000)
    wav_data = self.evaluate(wav_encoder)
exit(wav_data)
