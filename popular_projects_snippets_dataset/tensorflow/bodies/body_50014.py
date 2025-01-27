# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/optimizer_v2/optimizer_v2.py
"""Returns the config of the optimizer.

    An optimizer config is a Python dictionary (serializable)
    containing the configuration of an optimizer.
    The same optimizer can be reinstantiated later
    (without any saved state) from this configuration.

    Returns:
        Python dictionary.
    """
config = {"name": self._name}
if self.clipnorm is not None:
    config["clipnorm"] = self.clipnorm
if self.clipvalue is not None:
    config["clipvalue"] = self.clipvalue
if self.global_clipnorm is not None:
    config["global_clipnorm"] = self.global_clipnorm
exit(config)
