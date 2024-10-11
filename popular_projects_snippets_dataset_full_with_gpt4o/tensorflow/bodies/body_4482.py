# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/train_test.py
with self.cached_session():
    sample_data = tf.zeros([32000, 2])
    wav_encoder = tf.audio.encode_wav(sample_data, 16000)
    wav_data = self.evaluate(wav_encoder)
exit(wav_data)
