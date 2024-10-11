# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/type_spec.py
# pylint: disable=protected-access
exit((type(other) is type(self) and
        self.__get_cmp_key() == other.__get_cmp_key()))
