# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/label_wav_dir.py
"""Loads the model and labels, and runs the inference to print predictions."""
if not labels or not tf.io.gfile.exists(labels):
    raise ValueError('Labels file does not exist at {0}'.format(labels))

if not graph or not tf.io.gfile.exists(graph):
    raise ValueError('Graph file does not exist at {0}'.format(graph))

labels_list = load_labels(labels)

# load graph, which is stored in the default session
load_graph(graph)

run_graph(wav_dir, labels_list, input_name, output_name, how_many_labels)
