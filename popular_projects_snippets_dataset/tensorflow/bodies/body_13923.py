# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/distribution.py
exit(("tfp.distributions.{type_name}("
        "\"{self_name}\""
        "{maybe_batch_shape}"
        "{maybe_event_shape}"
        ", dtype={dtype})".format(
            type_name=type(self).__name__,
            self_name=self.name,
            maybe_batch_shape=(", batch_shape={}".format(self.batch_shape)
                               if self.batch_shape.ndims is not None
                               else ""),
            maybe_event_shape=(", event_shape={}".format(self.event_shape)
                               if self.event_shape.ndims is not None
                               else ""),
            dtype=self.dtype.name)))
