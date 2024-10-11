# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/matching_files_dataset_test.py
tmp_dir = tempfile.mkdtemp()
width = 16
depth = 8
for i in range(width):
    for j in range(depth):
        new_base = os.path.join(tmp_dir, str(i),
                                *[str(dir_name) for dir_name in range(j)])
        if not os.path.exists(new_base):
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

num_outputs = width * len(patterns)
verify_fn(self, lambda: self._build_iterator_graph(patterns), num_outputs)

shutil.rmtree(tmp_dir, ignore_errors=True)
