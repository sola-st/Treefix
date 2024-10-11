# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner_test.py
config_task = json.loads(os.environ['TF_CONFIG'])['task']
exit(config_task['index'])
