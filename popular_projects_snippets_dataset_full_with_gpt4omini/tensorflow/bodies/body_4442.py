# Extracted from ./data/repos/tensorflow/tensorflow/examples/speech_commands/accuracy_utils.py
"""Load ground truth and timestamp pairs and store it in time order."""
with open(file_name, 'r') as f:
    for line in f:
        line_split = line.strip().split(',')
        if len(line_split) != 2:
            continue
        timestamp = round(float(line_split[1]))
        label = line_split[0]
        self._gt_occurrence.append([label, timestamp])
self._gt_occurrence = sorted(self._gt_occurrence, key=lambda item: item[1])
