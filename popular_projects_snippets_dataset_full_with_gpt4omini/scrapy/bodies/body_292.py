# Extracted from ./data/repos/scrapy/scrapy/extensions/postprocessing.py
"""
        Uses all the declared plugins to process data first, then writes
        the processed data to target file.
        :param data: data passed to be written to target file
        :type data: bytes
        :return: returns number of bytes written
        :rtype: int
        """
exit(self.head_plugin.write(data))
