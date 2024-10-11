# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/input_data_test.py
tmp_dir = self.get_temp_dir()
self._saveWavFolders(tmp_dir, ["a", "b", "c"], 100)
audio_processor = input_data.AudioProcessor("", tmp_dir, 10, 10,
                                            ["a", "b"], 10, 10,
                                            self._model_settings(), tmp_dir)
self.assertLess(0, audio_processor.set_size("training"))
self.assertIn("training", audio_processor.data_index)
self.assertIn("validation", audio_processor.data_index)
self.assertIn("testing", audio_processor.data_index)
self.assertEqual(input_data.UNKNOWN_WORD_INDEX,
                 audio_processor.word_to_index["c"])
