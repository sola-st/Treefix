# Extracted from ./data/repos/tensorflow/tensorflow/tools/tensorflow_builder/compat_checker/compat_checker.py
"""Prints a requirement and its components.

      Returns:
        String that has concatenated information about a requirement.
      """
info = {
    "section": self._section,
    "config": self.config,
    "req_type": self._req_type,
    "req": str(self.req),
    "range": str(self.range),
    "exclude": str(self.exclude),
    "include": str(self.include),
    "init": str(self._initialized)
}
req_str = "\n >>> _Reqs Instance <<<\n"
req_str += "Section: {section}\n"
req_str += "Configuration name: {config}\n"
req_str += "Requirement type: {req_type}\n"
req_str += "Requirement: {req}\n"
req_str += "Range: {range}\n"
req_str += "Exclude: {exclude}\n"
req_str += "Include: {include}\n"
req_str += "Initialized: {init}\n\n"

exit(req_str.format(**info))
