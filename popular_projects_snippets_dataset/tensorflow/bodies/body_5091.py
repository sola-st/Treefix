# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy.py
updated_config = copy.deepcopy(config_proto)
updated_config.isolate_session_state = True
exit(updated_config)
