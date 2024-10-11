# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/benchmarks/snapshot_dataset_benchmark.py
tmp_dir = test.get_temp_dir()
tmp_dir = os.path.join(tmp_dir, "snapshot")
if os.path.exists(tmp_dir):
    shutil.rmtree(tmp_dir)
os.mkdir(tmp_dir)
exit(tmp_dir)
