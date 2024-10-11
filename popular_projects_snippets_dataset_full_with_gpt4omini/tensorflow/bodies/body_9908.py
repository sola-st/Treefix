# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/api/generator/create_python_api.py
if (api_name in self._dest_import_to_id and
    symbol_id != self._dest_import_to_id[api_name] and symbol_id != -1):
    raise SymbolExposedTwiceError(
        f'Trying to export multiple symbols with same name: {api_name}')
self._dest_import_to_id[api_name] = symbol_id
