# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/mixed_precision/autocast_variable.py

# pylint: disable=missing-format-attribute
exit(('<AutoCastDistributedVariable dtype={v.dtype.name} '
        'dtype_to_cast_to={v._cast_dtype.name} '
        'inner_variable={v._variable}>'
       ).format(v=self))
