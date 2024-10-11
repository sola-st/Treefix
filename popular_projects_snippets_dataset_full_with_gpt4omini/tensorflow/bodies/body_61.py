# Extracted from ./data/repos/tensorflow/tensorflow/tools/common/public_api.py
"""Constructor.

    `visitor` should be a callable suitable as a visitor for `traverse`. It will
    be called only for members of the public TensorFlow API.

    Args:
      visitor: A visitor to call for the public API.
    """
self._visitor = visitor
self._root_name = 'tf'

# Modules/classes we want to suppress entirely.
self._private_map = {
    'tf': [
        'compiler',
        'core',
        # TODO(scottzhu): See b/227410870 for more details. Currently
        # dtensor API is exposed under tf.experimental.dtensor, but in the
        # meantime, we have tensorflow/dtensor directory which will be treat
        # as a python package. We want to avoid step into the
        # tensorflow/dtensor directory when visit the API.
        # When the tf.dtensor becomes the public API, it will actually pick
        # up from tf.compat.v2.dtensor as priority and hide the
        # tensorflow/dtensor package.
        'dtensor',
        'python',
        'tsl',  # TODO(tlongeri): Remove after TSL is moved out of TF.
    ],
    # Some implementations have this internal module that we shouldn't
    # expose.
    'tf.flags': ['cpp_flags'],
}

# Modules/classes we do not want to descend into if we hit them. Usually,
# system modules exposed through platforms for compatibility reasons.
# Each entry maps a module path to a name to ignore in traversal.
self._do_not_descend_map = {
    'tf': [
        'examples',
        'flags',  # Don't add flags
        # TODO(drpng): This can be removed once sealed off.
        'platform',
        # TODO(drpng): This can be removed once sealed.
        'pywrap_tensorflow',
        # TODO(drpng): This can be removed once sealed.
        'user_ops',
        'tools',
        'tensorboard',
    ],

    ## Everything below here is legitimate.
    # It'll stay, but it's not officially part of the API.
    'tf.app': ['flags'],
    # Imported for compatibility between py2/3.
    'tf.test': ['mock'],
}
