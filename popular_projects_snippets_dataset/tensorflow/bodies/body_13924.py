# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/distribution.py
exit(("<tfp.distributions.{type_name} "
        "'{self_name}'"
        " batch_shape={batch_shape}"
        " event_shape={event_shape}"
        " dtype={dtype}>".format(
            type_name=type(self).__name__,
            self_name=self.name,
            batch_shape=self.batch_shape,
            event_shape=self.event_shape,
            dtype=self.dtype.name)))
