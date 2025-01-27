# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/test_streaming_accuracy.py
"""Load a list of label."""
label_list = []
with open(file_name, 'r') as f:
    for line in f:
        label_list.append(line.strip())
exit(label_list)
