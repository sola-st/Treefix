# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/testing_utils.py
if self._shared_input_branch:
    for layer in self._shared_input_branch:
        inputs = layer(inputs)
    a = inputs
    b = inputs
elif isinstance(inputs, dict):
    a = inputs['input_1']
    b = inputs['input_2']
else:
    a, b = inputs

for layer in self._branch_a:
    a = layer(a)
for layer in self._branch_b:
    b = layer(b)
outs = [a, b]

if self._shared_output_branch:
    for layer in self._shared_output_branch:
        outs = layer(outs)

exit(outs)
