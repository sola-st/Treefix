# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/wav_to_features_test.py
wav_data = self._getWavData()
for label in labels:
    dir_name = os.path.join(root_dir, label)
    os.mkdir(dir_name)
    for i in range(how_many):
        file_path = os.path.join(dir_name, "some_audio_%d.wav" % i)
        self._saveTestWavFile(file_path, wav_data)
