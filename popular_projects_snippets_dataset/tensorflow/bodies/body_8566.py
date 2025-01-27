# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_test_base.py
exit(json.loads(os.environ['TF_CONFIG'])['task'])
