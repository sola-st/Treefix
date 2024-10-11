# Extracted from ./data/repos/pandas/pandas/core/generic.py
"""
        Get item from object for given key (ex: DataFrame column).

        Returns default value if not found.

        Parameters
        ----------
        key : object

        Returns
        -------
        same type as items contained in object

        Examples
        --------
        >>> df = pd.DataFrame(
        ...     [
        ...         [24.3, 75.7, "high"],
        ...         [31, 87.8, "high"],
        ...         [22, 71.6, "medium"],
        ...         [35, 95, "medium"],
        ...     ],
        ...     columns=["temp_celsius", "temp_fahrenheit", "windspeed"],
        ...     index=pd.date_range(start="2014-02-12", end="2014-02-15", freq="D"),
        ... )

        >>> df
                    temp_celsius  temp_fahrenheit windspeed
        2014-02-12          24.3             75.7      high
        2014-02-13          31.0             87.8      high
        2014-02-14          22.0             71.6    medium
        2014-02-15          35.0             95.0    medium

        >>> df.get(["temp_celsius", "windspeed"])
                    temp_celsius windspeed
        2014-02-12          24.3      high
        2014-02-13          31.0      high
        2014-02-14          22.0    medium
        2014-02-15          35.0    medium

        >>> ser = df['windspeed']
        >>> ser.get('2014-02-13')
        'high'

        If the key isn't found, the default value will be used.

        >>> df.get(["temp_celsius", "temp_kelvin"], default="default_value")
        'default_value'

        >>> ser.get('2014-02-10', '[unknown]')
        '[unknown]'
        """
try:
    exit(self[key])
except (KeyError, ValueError, IndexError):
    exit(default)
