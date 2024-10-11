# Extracted from ./data/repos/pandas/pandas/core/frame.py
"""
        Render a DataFrame to an XML document.

        .. versionadded:: 1.3.0

        Parameters
        ----------
        path_or_buffer : str, path object, file-like object, or None, default None
            String, path object (implementing ``os.PathLike[str]``), or file-like
            object implementing a ``write()`` function. If None, the result is returned
            as a string.
        index : bool, default True
            Whether to include index in XML document.
        root_name : str, default 'data'
            The name of root element in XML document.
        row_name : str, default 'row'
            The name of row element in XML document.
        na_rep : str, optional
            Missing data representation.
        attr_cols : list-like, optional
            List of columns to write as attributes in row element.
            Hierarchical columns will be flattened with underscore
            delimiting the different levels.
        elem_cols : list-like, optional
            List of columns to write as children in row element. By default,
            all columns output as children of row element. Hierarchical
            columns will be flattened with underscore delimiting the
            different levels.
        namespaces : dict, optional
            All namespaces to be defined in root element. Keys of dict
            should be prefix names and values of dict corresponding URIs.
            Default namespaces should be given empty string key. For
            example, ::

                namespaces = {{"": "https://example.com"}}

        prefix : str, optional
            Namespace prefix to be used for every element and/or attribute
            in document. This should be one of the keys in ``namespaces``
            dict.
        encoding : str, default 'utf-8'
            Encoding of the resulting document.
        xml_declaration : bool, default True
            Whether to include the XML declaration at start of document.
        pretty_print : bool, default True
            Whether output should be pretty printed with indentation and
            line breaks.
        parser : {{'lxml','etree'}}, default 'lxml'
            Parser module to use for building of tree. Only 'lxml' and
            'etree' are supported. With 'lxml', the ability to use XSLT
            stylesheet is supported.
        stylesheet : str, path object or file-like object, optional
            A URL, file-like object, or a raw string containing an XSLT
            script used to transform the raw XML output. Script should use
            layout of elements and attributes from original output. This
            argument requires ``lxml`` to be installed. Only XSLT 1.0
            scripts and not later versions is currently supported.
        {compression_options}

            .. versionchanged:: 1.4.0 Zstandard support.

        {storage_options}

        Returns
        -------
        None or str
            If ``io`` is None, returns the resulting XML format as a
            string. Otherwise returns None.

        See Also
        --------
        to_json : Convert the pandas object to a JSON string.
        to_html : Convert DataFrame to a html.

        Examples
        --------
        >>> df = pd.DataFrame({{'shape': ['square', 'circle', 'triangle'],
        ...                    'degrees': [360, 360, 180],
        ...                    'sides': [4, np.nan, 3]}})

        >>> df.to_xml()  # doctest: +SKIP
        <?xml version='1.0' encoding='utf-8'?>
        <data>
          <row>
            <index>0</index>
            <shape>square</shape>
            <degrees>360</degrees>
            <sides>4.0</sides>
          </row>
          <row>
            <index>1</index>
            <shape>circle</shape>
            <degrees>360</degrees>
            <sides/>
          </row>
          <row>
            <index>2</index>
            <shape>triangle</shape>
            <degrees>180</degrees>
            <sides>3.0</sides>
          </row>
        </data>

        >>> df.to_xml(attr_cols=[
        ...           'index', 'shape', 'degrees', 'sides'
        ...           ])  # doctest: +SKIP
        <?xml version='1.0' encoding='utf-8'?>
        <data>
          <row index="0" shape="square" degrees="360" sides="4.0"/>
          <row index="1" shape="circle" degrees="360"/>
          <row index="2" shape="triangle" degrees="180" sides="3.0"/>
        </data>

        >>> df.to_xml(namespaces={{"doc": "https://example.com"}},
        ...           prefix="doc")  # doctest: +SKIP
        <?xml version='1.0' encoding='utf-8'?>
        <doc:data xmlns:doc="https://example.com">
          <doc:row>
            <doc:index>0</doc:index>
            <doc:shape>square</doc:shape>
            <doc:degrees>360</doc:degrees>
            <doc:sides>4.0</doc:sides>
          </doc:row>
          <doc:row>
            <doc:index>1</doc:index>
            <doc:shape>circle</doc:shape>
            <doc:degrees>360</doc:degrees>
            <doc:sides/>
          </doc:row>
          <doc:row>
            <doc:index>2</doc:index>
            <doc:shape>triangle</doc:shape>
            <doc:degrees>180</doc:degrees>
            <doc:sides>3.0</doc:sides>
          </doc:row>
        </doc:data>
        """

from pandas.io.formats.xml import (
    EtreeXMLFormatter,
    LxmlXMLFormatter,
)

lxml = import_optional_dependency("lxml.etree", errors="ignore")

TreeBuilder: type[EtreeXMLFormatter] | type[LxmlXMLFormatter]

if parser == "lxml":
    if lxml is not None:
        TreeBuilder = LxmlXMLFormatter
    else:
        raise ImportError(
            "lxml not found, please install or use the etree parser."
        )

elif parser == "etree":
    TreeBuilder = EtreeXMLFormatter

else:
    raise ValueError("Values for parser can only be lxml or etree.")

xml_formatter = TreeBuilder(
    self,
    path_or_buffer=path_or_buffer,
    index=index,
    root_name=root_name,
    row_name=row_name,
    na_rep=na_rep,
    attr_cols=attr_cols,
    elem_cols=elem_cols,
    namespaces=namespaces,
    prefix=prefix,
    encoding=encoding,
    xml_declaration=xml_declaration,
    pretty_print=pretty_print,
    stylesheet=stylesheet,
    compression=compression,
    storage_options=storage_options,
)

exit(xml_formatter.write_output())
