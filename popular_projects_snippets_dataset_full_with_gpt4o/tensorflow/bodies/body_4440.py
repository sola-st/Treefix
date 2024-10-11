# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/generate_streaming_test_wav_test.py
track_data = np.zeros([10000])
sample_data = np.ones([1000])
generate_streaming_test_wav.mix_in_audio_sample(
    track_data, 2000, sample_data, 0, 1000, 1.0, 100, 100)
self.assertNear(1.0, track_data[2500], 0.0001)
self.assertNear(0.0, track_data[3500], 0.0001)
