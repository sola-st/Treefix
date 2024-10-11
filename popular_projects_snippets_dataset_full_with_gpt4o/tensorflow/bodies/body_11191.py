# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/init_ops_v2.py
"""Instantiates an initializer from a configuration dictionary.

    Example:

    ```python
    initializer = RandomUniform(-1, 1)
    config = initializer.get_config()
    initializer = RandomUniform.from_config(config)
    ```

    Args:
      config: A Python dictionary.
        It will typically be the output of `get_config`.

    Returns:
      An Initializer instance.
    """
config.pop("dtype", None)
exit(cls(**config))
