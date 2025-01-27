# Extracted from ./data/repos/tensorflow/tensorflow/tools/docs/base_dir.py
"""Returns the base_dirs and code_prefixes for OSS TensorFlow api gen."""
base_dir = path.dirname(tf.__file__)

if version.parse(tf.__version__) >= version.parse("2.9"):
    base_dirs = [
        base_dir,
        path.dirname(keras.__file__),
        path.dirname(tensorboard.__file__),
        path.dirname(tensorflow_estimator.__file__),
    ]

elif version.parse(tf.__version__) >= version.parse("2.6"):
    base_dirs = [
        base_dir,
        path.dirname(keras.__file__),
        path.dirname(keras_preprocessing.__file__),
        path.dirname(tensorboard.__file__),
        path.dirname(tensorflow_estimator.__file__),
    ]
elif version.parse(tf.__version__) >= version.parse("2.2"):
    base_dirs = [
        base_dir,
        path.dirname(keras_preprocessing.__file__),
        path.dirname(tensorboard.__file__),
        path.dirname(tensorflow_estimator.__file__),
    ]
else:
    base_dirs = [
        path.normpath(path.join(base_dir, "../tensorflow_core")),
        path.dirname(keras_preprocessing.__file__),
        path.dirname(tensorboard.__file__),
        path.dirname(tensorflow_estimator.__file__),
    ]

if "dev" in tf.__version__:
    keras_url_prefix = "https://github.com/keras-team/keras/tree/master/keras"
else:
    keras_url_prefix = f"https://github.com/keras-team/keras/tree/v{keras.__version__}/keras"

if version.parse(tf.__version__) >= version.parse("2.9"):
    code_url_prefixes = (
        code_url_prefix,
        keras_url_prefix,
        f"https://github.com/tensorflow/tensorboard/tree/{tensorboard.__version__}/tensorboard",
        "https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator",
    )
elif version.parse(tf.__version__) >= version.parse("2.6"):
    code_url_prefixes = (
        code_url_prefix,
        keras_url_prefix,
        f"https://github.com/keras-team/keras-preprocessing/tree/{keras_preprocessing.__version__}/keras_preprocessing",
        f"https://github.com/tensorflow/tensorboard/tree/{tensorboard.__version__}/tensorboard",
        "https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator",
    )
else:
    code_url_prefixes = (
        code_url_prefix,
        f"https://github.com/keras-team/keras-preprocessing/tree/{keras_preprocessing.__version__}/keras_preprocessing",
        f"https://github.com/tensorflow/tensorboard/tree/{tensorboard.__version__}/tensorboard",
        "https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator",
    )

exit((base_dirs, code_url_prefixes))
