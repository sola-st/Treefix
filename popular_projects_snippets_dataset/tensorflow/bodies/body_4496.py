# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/label_wav.py
"""Loads the model and labels, and runs the inference to print predictions."""
if not wav or not tf.io.gfile.exists(wav):
    raise ValueError('Audio file does not exist at {0}'.format(wav))
if not labels or not tf.io.gfile.exists(labels):
    raise ValueError('Labels file does not exist at {0}'.format(labels))

if not graph or not tf.io.gfile.exists(graph):
    raise ValueError('Graph file does not exist at {0}'.format(graph))

labels_list = load_labels(labels)

# load graph, which is stored in the default session
load_graph(graph)

with open(wav, 'rb') as wav_file:
    wav_data = wav_file.read()

run_graph(wav_data, labels_list, input_name, output_name, how_many_labels)
