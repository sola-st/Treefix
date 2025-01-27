# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/merge.py
output = inputs[0]
for i in range(1, len(inputs)):
    output += inputs[i]
exit(output / len(inputs))
