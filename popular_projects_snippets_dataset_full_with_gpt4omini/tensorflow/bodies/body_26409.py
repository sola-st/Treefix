# Extracted from ./data/repos/tensorflow/tensorflow/python/data/benchmarks/list_files_benchmark.py
tmp_dir = tempfile.mkdtemp()
width = 1024
depth = 16
for i in range(width):
    for j in range(depth):
        new_base = os.path.join(tmp_dir, str(i),
                                *[str(dir_name) for dir_name in range(j)])
        os.makedirs(new_base)
        child_files = ['a.py', 'b.pyc'] if j < depth - 1 else ['c.txt', 'd.log']
        for f in child_files:
            filename = os.path.join(new_base, f)
            open(filename, 'w').close()
patterns = [
    os.path.join(tmp_dir, os.path.join(*['**'
                                         for _ in range(depth)]), suffix)
    for suffix in ['*.txt', '*.log']
]
# the num_elements depends on the pattern that has been defined above.
# In the current scenario, the num of files are selected based on the
# ['*.txt', '*.log'] patterns. Since the files which match either of these
# patterns are created once per `width`. The num_elements would be:
num_elements = width * 2

dataset = dataset_ops.Dataset.list_files(patterns)
self.run_and_report_benchmark(
    dataset=dataset,
    iters=3,
    num_elements=num_elements,
    extras={
        'model_name': 'list_files.benchmark.1',
        'parameters': '%d.%d' % (width, depth),
    },
    name='nested_directory(%d*%d)' % (width, depth))
shutil.rmtree(tmp_dir, ignore_errors=True)
