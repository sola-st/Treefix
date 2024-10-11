# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/input_data_test.py
tmp_dir = self.get_temp_dir()
wav_dir = os.path.join(tmp_dir, "wavs")
os.mkdir(wav_dir)
self._saveWavFolders(wav_dir, ["a", "b", "c"], 1)
desired_samples = 1600
model_settings = {
    "desired_samples": desired_samples,
    "fingerprint_size": 40,
    "label_count": 4,
    "window_size_samples": 100,
    "window_stride_samples": 100,
    "fingerprint_width": 40,
    "average_window_width": 6,
    "preprocess": "average",
}
with self.cached_session() as sess:
    audio_processor = input_data.AudioProcessor(
        "", wav_dir, 10, 10, ["a", "b"], 10, 10, model_settings, tmp_dir)
    sample_data = np.zeros([desired_samples, 1])
    for i in range(desired_samples):
        phase = i % 4
        if phase == 0:
            sample_data[i, 0] = 0
        elif phase == 1:
            sample_data[i, 0] = -1
        elif phase == 2:
            sample_data[i, 0] = 0
        elif phase == 3:
            sample_data[i, 0] = 1
    test_wav_path = os.path.join(tmp_dir, "test_wav.wav")
    input_data.save_wav_file(test_wav_path, sample_data, 16000)

    results = audio_processor.get_features_for_wav(test_wav_path,
                                                   model_settings, sess)
    spectrogram = results[0]
    self.assertEqual(1, spectrogram.shape[0])
    self.assertEqual(16, spectrogram.shape[1])
    self.assertEqual(11, spectrogram.shape[2])
    self.assertNear(0, spectrogram[0, 0, 0], 0.1)
    self.assertNear(200, spectrogram[0, 0, 5], 0.1)
