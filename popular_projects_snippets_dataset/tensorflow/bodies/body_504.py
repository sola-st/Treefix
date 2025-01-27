# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2.py
self.log_level = ast_edits.INFO
self.log_message = ("Not upgrading symbols because `tensorflow." + version +
                    "` was directly imported as `tf`.")
