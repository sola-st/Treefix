# Extracted from ./data/repos/pandas/pandas/io/gbq.py
pandas_gbq = _try_import()
pandas_gbq.to_gbq(
    dataframe,
    destination_table,
    project_id=project_id,
    chunksize=chunksize,
    reauth=reauth,
    if_exists=if_exists,
    auth_local_webserver=auth_local_webserver,
    table_schema=table_schema,
    location=location,
    progress_bar=progress_bar,
    credentials=credentials,
)
