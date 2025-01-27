# Extracted from ./data/repos/tensorflow/tensorflow/examples/custom_ops_doc/multiplex_4/multiplex_4_load_use.py
del argv  # not used
path = 'model_using_multiplex'
result = model_using_multiplex.load_and_use(path)
print('Result:', result)
