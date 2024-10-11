# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/legacy_tf_layers/core.py
super(Dense, self).__init__(units=units,
                            activation=activation,
                            use_bias=use_bias,
                            kernel_initializer=kernel_initializer,
                            bias_initializer=bias_initializer,
                            kernel_regularizer=kernel_regularizer,
                            bias_regularizer=bias_regularizer,
                            activity_regularizer=activity_regularizer,
                            kernel_constraint=kernel_constraint,
                            bias_constraint=bias_constraint,
                            trainable=trainable,
                            name=name,
                            **kwargs)
