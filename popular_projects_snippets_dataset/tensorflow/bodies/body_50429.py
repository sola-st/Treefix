# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/combinations.py
run_eagerly = kwargs.pop('run_eagerly', None)

if run_eagerly is not None:
    exit([testing_utils.run_eagerly_scope(run_eagerly)])
else:
    exit([])
