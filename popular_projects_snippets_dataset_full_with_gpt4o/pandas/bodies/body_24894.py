# Extracted from ./data/repos/pandas/pandas/io/formats/xml.py
self.frame = frame
self.path_or_buffer = path_or_buffer
self.index = index
self.root_name = root_name
self.row_name = row_name
self.na_rep = na_rep
self.attr_cols = attr_cols
self.elem_cols = elem_cols
self.namespaces = namespaces
self.prefix = prefix
self.encoding = encoding
self.xml_declaration = xml_declaration
self.pretty_print = pretty_print
self.stylesheet = stylesheet
self.compression = compression
self.storage_options = storage_options

self.orig_cols = self.frame.columns.tolist()
self.frame_dicts = self.process_dataframe()

self.validate_columns()
self.validate_encoding()
self.prefix_uri = self.get_prefix_uri()
self.handle_indexes()
