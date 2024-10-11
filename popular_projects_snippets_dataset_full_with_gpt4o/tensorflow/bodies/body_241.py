# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/ast_edits.py
"""Handle bare Attributes i.e. [tf.foo, tf.bar]."""
full_name = self._get_full_name(node)
if full_name:
    detection = self._api_analysis_spec.symbols_to_detect.get(full_name, None)
    if detection:
        self.add_result(detection)
        self.add_log(
            detection.log_level, node.lineno, node.col_offset,
            detection.log_message)

self.generic_visit(node)
