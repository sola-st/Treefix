# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/input_data_test.py
tmp_dir = self.get_temp_dir()
wav_dir = os.path.join(tmp_dir, "wavs")
os.mkdir(wav_dir)
self._saveWavFolders(wav_dir, ["a", "b", "c"], 100)
model_settings = {
    "desired_samples": 160,
    "fingerprint_size": 40,
    "label_count": 4,
    "window_size_samples": 100,
    "window_stride_samples": 100,
    "fingerprint_width": 40,
    "preprocess": "mfcc",
}
audio_processor = input_data.AudioProcessor("", wav_dir, 10, 10, ["a", "b"],
                                            10, 10, model_settings, tmp_dir)
result_data, result_labels = audio_processor.get_unprocessed_data(
    10, model_settings, "training")
self.assertEqual(10, len(result_data))
self.assertEqual(10, len(result_labels))
