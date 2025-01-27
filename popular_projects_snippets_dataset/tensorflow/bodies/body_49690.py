# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/utils/layer_utils.py
line = ''
for i in range(len(fields)):
    if i > 0:
        line = line[:-1] + ' '
    line += str(fields[i])
    line = line[:positions[i]]
    line += ' ' * (positions[i] - len(line))
print_fn(line)
