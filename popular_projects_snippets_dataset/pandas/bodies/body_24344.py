# Extracted from ./data/repos/pandas/pandas/io/xml.py
from xml.etree.ElementTree import (
    XMLParser,
    parse,
)

handle_data = get_data_from_filepath(
    filepath_or_buffer=raw_doc,
    encoding=self.encoding,
    compression=self.compression,
    storage_options=self.storage_options,
)

with preprocess_data(handle_data) as xml_data:
    curr_parser = XMLParser(encoding=self.encoding)
    document = parse(xml_data, parser=curr_parser)

exit(document.getroot())
