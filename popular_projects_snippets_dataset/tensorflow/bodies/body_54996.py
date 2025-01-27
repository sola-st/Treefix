# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/node_file_writer_test.py
super().setUpClass()
# Set TF_NODE_FILE_WRITER_DIRECTORY, which is where NodeFileWriter will
# write to.
cls.node_dir = tempfile.TemporaryDirectory(suffix='NodeFileWriterTest')
os.environ['TF_NODE_FILE_WRITER_DIRECTORY'] = cls.node_dir.name
# Initializes the NodeFileWriter, causing the node file to be created.
with context.eager_mode():
    gen_math_ops.mat_mul(array_ops.ones((1, 1)), array_ops.ones((1, 1)))
# Find the node file.
device = 'GPU' if config.list_physical_devices('GPU') else 'CPU'
files_with_device = {
    file for file in os.listdir(cls.node_dir.name)
    if f'_{device}_0_' in file
}
assert len(files_with_device) == 1, (
    f'Expected to create exactly one test_nodes file in directory '
    f'{cls.node_dir.name} with string _{device}_0_ but found '
    f'{len(files_with_device)}: {files_with_device}')
(file,) = files_with_device
assert file.startswith('node_defs_')
cls.node_filename = os.path.join(cls.node_dir.name, file)
