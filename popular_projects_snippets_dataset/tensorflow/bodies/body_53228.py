# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/extension_type.py
fields = [(k, _convert_anonymous_fields(v))
          for (k, v) in self.__dict__.items()
          if not extension_type_field.ExtensionTypeField.is_reserved_name(k)
         ]
self.__dict__.update(fields)
