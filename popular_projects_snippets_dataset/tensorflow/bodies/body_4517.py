# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/input_data_test.py
tmp_dir = self.get_temp_dir()
self._saveWavFolders(tmp_dir, ["a", "b", "c"], 100)
with self.assertRaises(Exception) as e:
    _ = input_data.AudioProcessor("", tmp_dir, 10, 10, ["a", "b", "d"], 10,
                                  10, self._model_settings(), tmp_dir)
self.assertIn("Expected to find", str(e.exception))
