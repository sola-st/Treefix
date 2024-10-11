# Extracted from ./data/repos/tensorflow/tensorflow/examples/custom_ops_doc/multiplex_4/multiplex_2_save.py
del argv  # not used
path = 'model_using_multiplex'
if os.path.exists(path):
    shutil.rmtree(path, ignore_errors=True)
model_using_multiplex.save(multiplex_2_op.multiplex, path)
print('Saved model to', path)
