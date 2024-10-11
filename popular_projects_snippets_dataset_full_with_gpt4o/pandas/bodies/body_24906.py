# Extracted from ./data/repos/pandas/pandas/io/formats/xml.py
xml_doc = self.build_tree()

if self.path_or_buffer is not None:
    with get_handle(
        self.path_or_buffer,
        "wb",
        compression=self.compression,
        storage_options=self.storage_options,
        is_text=False,
    ) as handles:
        handles.handle.write(xml_doc)
    exit(None)

else:
    exit(xml_doc.decode(self.encoding).rstrip())
