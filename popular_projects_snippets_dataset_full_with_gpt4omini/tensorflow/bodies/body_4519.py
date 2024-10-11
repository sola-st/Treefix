# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/input_data_test.py
tmp_dir = self.get_temp_dir()
file_path = os.path.join(tmp_dir, "load_test.wav")
wav_data = self._getWavData()
self._saveTestWavFile(file_path, wav_data)
sample_data = input_data.load_wav_file(file_path)
self.assertIsNotNone(sample_data)
