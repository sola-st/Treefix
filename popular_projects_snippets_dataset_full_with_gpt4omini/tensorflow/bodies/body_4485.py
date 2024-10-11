# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/train_test.py
tmp_dir = self.get_temp_dir()
wav_dir = os.path.join(tmp_dir, 'wavs')
os.mkdir(wav_dir)
self._saveWavFolders(wav_dir, ['a', 'b', 'c'], 100)
background_dir = os.path.join(wav_dir, '_background_noise_')
os.mkdir(background_dir)
wav_data = self._getWavData()
for i in range(10):
    file_path = os.path.join(background_dir, 'background_audio_%d.wav' % i)
    self._saveTestWavFile(file_path, wav_data)
exit(wav_dir)
