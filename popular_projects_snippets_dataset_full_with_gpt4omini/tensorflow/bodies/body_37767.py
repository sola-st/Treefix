# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/io_ops/parsing_ops_test.py
outputs = []
if fixed_length is None:
    fixed_length = len(words[0])

for word in words:
    output = []
    for i in range(fixed_length):
        if i < len(word):
            output.append(ord(word[i]))
        else:
            output.append(0)
    outputs.append(output)
exit(np.array(outputs))
