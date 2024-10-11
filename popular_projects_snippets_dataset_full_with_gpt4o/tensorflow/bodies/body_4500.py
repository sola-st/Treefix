# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/label_wav_test.py
tmp_dir = self.get_temp_dir()
wav_data = self._getWavData()
wav_filename = os.path.join(tmp_dir, "wav_file.wav")
self._saveTestWavFile(wav_filename, wav_data)
input_name = "test_input"
output_name = "test_output"
graph_filename = os.path.join(tmp_dir, "test_graph.pb")
with tf.compat.v1.Session() as sess:
    tf.compat.v1.placeholder(tf.string, name=input_name)
    tf.zeros([1, 3], name=output_name)
    with open(graph_filename, "wb") as f:
        f.write(sess.graph.as_graph_def().SerializeToString())
labels_filename = os.path.join(tmp_dir, "test_labels.txt")
with open(labels_filename, "w") as f:
    f.write("a\nb\nc\n")
label_wav.label_wav(wav_filename, labels_filename, graph_filename,
                    input_name + ":0", output_name + ":0", 3)
