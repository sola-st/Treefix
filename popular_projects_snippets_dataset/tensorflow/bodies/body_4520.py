# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/input_data_test.py
tmp_dir = self.get_temp_dir()
file_path = os.path.join(tmp_dir, "load_test.wav")
save_data = np.zeros([16000, 1])
input_data.save_wav_file(file_path, save_data, 16000)
loaded_data = input_data.load_wav_file(file_path)
self.assertIsNotNone(loaded_data)
self.assertEqual(16000, len(loaded_data))
