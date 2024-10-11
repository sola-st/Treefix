# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/input_data_test.py
tmp_dir = self.get_temp_dir()
background_dir = os.path.join(tmp_dir, "_background_noise_")
os.mkdir(background_dir)
wav_data = self._getWavData()
for i in range(10):
    file_path = os.path.join(background_dir, "background_audio_%d.wav" % i)
    self._saveTestWavFile(file_path, wav_data)
self._saveWavFolders(tmp_dir, ["a", "b", "c"], 100)
audio_processor = input_data.AudioProcessor("", tmp_dir, 10, 10,
                                            ["a", "b"], 10, 10,
                                            self._model_settings(), tmp_dir)
self.assertEqual(10, len(audio_processor.background_data))
