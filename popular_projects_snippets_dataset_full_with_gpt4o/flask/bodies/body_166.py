# Extracted from ./data/repos/flask/src/flask/config.py
"""Update the values in the config from a file that is loaded
        using the ``load`` parameter. The loaded data is passed to the
        :meth:`from_mapping` method.

        .. code-block:: python

            import json
            app.config.from_file("config.json", load=json.load)

            import toml
            app.config.from_file("config.toml", load=toml.load)

        :param filename: The path to the data file. This can be an
            absolute path or relative to the config root path.
        :param load: A callable that takes a file handle and returns a
            mapping of loaded data from the file.
        :type load: ``Callable[[Reader], Mapping]`` where ``Reader``
            implements a ``read`` method.
        :param silent: Ignore the file if it doesn't exist.
        :return: ``True`` if the file was loaded successfully.

        .. versionadded:: 2.0
        """
filename = os.path.join(self.root_path, filename)

try:
    with open(filename) as f:
        obj = load(f)
except OSError as e:
    if silent and e.errno in (errno.ENOENT, errno.EISDIR):
        exit(False)

    e.strerror = f"Unable to load configuration file ({e.strerror})"
    raise

exit(self.from_mapping(obj))
