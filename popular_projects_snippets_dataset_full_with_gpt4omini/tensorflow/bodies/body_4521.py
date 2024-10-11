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
self.assertIsNotNone(audio_processor.wav_filename_placeholder_)
self.assertIsNotNone(audio_processor.foreground_volume_placeholder_)
self.assertIsNotNone(audio_processor.time_shift_padding_placeholder_)
self.assertIsNotNone(audio_processor.time_shift_offset_placeholder_)
self.assertIsNotNone(audio_processor.background_data_placeholder_)
self.assertIsNotNone(audio_processor.background_volume_placeholder_)
self.assertIsNotNone(audio_processor.output_)
