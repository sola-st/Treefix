# Extracted from ./data/repos/tensorflow/tensorflow/python/platform/benchmark.py
# Allow TensorFlow runtime to allocate a new threadpool with different
# number of threads for each new benchmark.
os.environ[OVERRIDE_GLOBAL_THREADPOOL] = "1"
super().__init__()
