# Extracted from ./data/repos/tensorflow/tensorflow/python/trackable/data_structures_test.py
obj = autotrackable.AutoTrackable()
obj.l = [1]
json.dumps(obj.l, default=serialization.get_json_type)
