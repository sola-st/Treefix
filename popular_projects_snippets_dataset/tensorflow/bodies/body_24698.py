# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/debug_data.py
json_metadata = json.loads(event.log_message.message)
exit(_CoreMetadata(json_metadata["global_step"],
                     json_metadata["session_run_index"],
                     json_metadata["executor_step_index"],
                     json_metadata["input_names"],
                     json_metadata["output_names"],
                     json_metadata["target_nodes"]))
