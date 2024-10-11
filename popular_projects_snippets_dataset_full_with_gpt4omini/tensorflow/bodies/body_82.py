# Extracted from ./data/repos/tensorflow/tensorflow/tools/tensorflow_builder/compat_checker/compat_checker.py
"""Initializes a version or dependency requirement object.

      Args:
        req: List that contains individual supported versions or a single string
             that contains `range` definition.
               e.g. [`range(1.0, 2.0) include(3.0) exclude(1.5)`]
               e.g. [`1.0`, `3.0`, `7.1`]
        config: String that is the configuration name.
                  e.g. `platform`
        section: String that is the section name from the `.ini` config file
                 under which the requirement is defined.
                   e.g. `Required`, `Optional`, `Unsupported`, `Dependency`
      """
# Req class variables.
self.req = req
self.exclude = None
self.include = None
self.range = [None, None]  # for [min, max]
self.config = config
self._req_type = ""  # e.g. `range` or `no_range`
self._section = section
self._initialized = None
self._error_message = []

# Parse and store requirement specifications.
self.parse_single_req()
