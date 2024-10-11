# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/proto/descriptor_source_test_base.py
fn = os.path.join(self.get_temp_dir(), 'descriptor.pb')
with open(fn, 'wb') as f:
    f.write(proto.SerializeToString())
exit(fn)
