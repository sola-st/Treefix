# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures_test.py
obj = autotrackable.AutoTrackable()
obj.d = {"a": 2}
json.dumps(obj.d, default=serialization.get_json_type)
