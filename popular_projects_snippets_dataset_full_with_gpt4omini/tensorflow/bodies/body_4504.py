# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/wav_to_features_test.py
tmp_dir = self.get_temp_dir()
wav_dir = os.path.join(tmp_dir, "wavs")
os.mkdir(wav_dir)
self._saveWavFolders(wav_dir, ["a", "b", "c"], 100)
input_file_path = os.path.join(tmp_dir, "input.wav")
output_file_path = os.path.join(tmp_dir, "output.c")
wav_data = self._getWavData()
self._saveTestWavFile(input_file_path, wav_data)
wav_to_features.wav_to_features(16000, 1000, 10, 10, 40, True, "average",
                                input_file_path, output_file_path)
with open(output_file_path, "rb") as f:
    content = f.read()
    self.assertIn(b"const unsigned char g_input_data", content)
