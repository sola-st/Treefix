# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/input_data_test.py
tmp_dir = self.get_temp_dir()
wav_dir = os.path.join(tmp_dir, "wavs")
os.mkdir(wav_dir)
self._saveWavFolders(wav_dir, ["a", "b", "c"], 100)
background_dir = os.path.join(wav_dir, "_background_noise_")
os.mkdir(background_dir)
wav_data = self._getWavData()
for i in range(10):
    file_path = os.path.join(background_dir, "background_audio_%d.wav" % i)
    self._saveTestWavFile(file_path, wav_data)
model_settings = models.prepare_model_settings(
    4, 16000, 1000, window_length_ms, 20, 40, preprocess)
with self.cached_session() as sess:
    audio_processor = input_data.AudioProcessor(
        "", wav_dir, 10, 10, ["a", "b"], 10, 10, model_settings, tmp_dir)
    result_data, result_labels = audio_processor.get_data(
        10, 0, model_settings, 0.3, 0.1, 100, "training", sess)
    self.assertEqual(10, len(result_data))
    self.assertEqual(10, len(result_labels))
