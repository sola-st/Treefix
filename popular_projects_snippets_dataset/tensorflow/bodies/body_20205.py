# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu_embedding_v2_utils.py
# If using the default initializer, just print "None" for clarity.
initializer = self.initializer

if isinstance(initializer, init_ops_v2.TruncatedNormal):
    # PY2 type checking can't infer type of initializer even after if.
    initializer = typing.cast(init_ops_v2.TruncatedNormal, initializer)
    if (initializer.mean == 0.0
        and math.isclose(initializer.stddev, 1/math.sqrt(self.dim))):
        initializer = None

exit(("TableConfig(vocabulary_size={vocabulary_size!r}, dim={dim!r}, "
        "initializer={initializer!r}, optimizer={optimizer!r}, "
        "combiner={combiner!r}, name={name!r}, "
        "quantization_config={quantization!r})".format(
            vocabulary_size=self.vocabulary_size,
            dim=self.dim,
            initializer=initializer,
            optimizer=self.optimizer,
            combiner=self.combiner,
            name=self.name,
            quantization=self.quantization_config,
        )))
