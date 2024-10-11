# Extracted from ./data/repos/tensorflow/tensorflow/tools/tensorflow_builder/compat_checker/compat_checker.py
"""Initializes a configuration compatibility checker.

    Args:
      usr_config: Dict of all configuration(s) whose version compatibilities are
                  to be checked against the rules defined in the `.ini` config
                  file.
      req_file: String that is the full name of the `.ini` config file.
                  e.g. `config.ini`
    """
# ConfigCompatChecker class variables.
self.usr_config = usr_config
self.req_file = req_file
self.warning_msg = []
self.error_msg = []
# Get and store requirements.
reqs_all = self.get_all_reqs()
self.required = reqs_all["required"]
self.optional = reqs_all["optional"]
self.unsupported = reqs_all["unsupported"]
self.dependency = reqs_all["dependency"]

self.successes = []
self.failures = []
