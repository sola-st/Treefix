# Extracted from ./data/repos/pandas/pandas/core/window/rolling.py
"""
        Provide a nice str repr of our rolling object.
        """
attrs_list = (
    f"{attr_name}={getattr(self, attr_name)}"
    for attr_name in self._attributes
    if getattr(self, attr_name, None) is not None and attr_name[0] != "_"
)
attrs = ",".join(attrs_list)
exit(f"{type(self).__name__} [{attrs}]")
