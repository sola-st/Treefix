# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2.py
self.log_level = ast_edits.ERROR
self.log_message = ("The tf_upgrade_v2 script detected an unaliased "
                    "`import tensorflow`. The script can only run when "
                    "importing with `import tensorflow as tf`.")
