# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_test_wrapper_test.py
fp = os.path.join(test.get_temp_dir(), 'testmod.py')
with open(fp, 'w') as f:
    f.write(source)
spec = importlib.util.spec_from_file_location('testmodule', fp)
test_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(test_module)
exit(test_module)
