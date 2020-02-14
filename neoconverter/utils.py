import pandas as pd


def _read(filepath):
    """Returns DF of raw data read from a NEO CSV-for-Excel file."""
    # By not immediately specifying an index_col, we avoid a bug
    # in pandas* where it'll try to "guess" the type of an index column
    # even if you tell it not to. For numerical values this can have
    # funky side effects like converting "179.75" to "179.740000000" or
    # something along those lines.
    # I don't *think* that should be a problem here but might as well be safe.
    #
    # * see https://stackoverflow.com/a/35058538/10730311
    # TODO don't say header=None, should be avoidable
    data = pd.read_csv(filepath, sep=",", header=None, dtype=str)
    if data.at[0, 0] != "lat/lon":
        raise ValueError(
            "Looks like this file isn't formatted as expected: there isn't "
            "the text 'lat/lon' present in the top-left cell."
        )
    # now that the data is loaded in as strings (not numbers), we can set the
    # index/header correctly
    # set index from first column
    data.set_index(data.columns[0], inplace=True)
    # set column names to first row
    data.columns = data.iloc[0]
    # ... and then remove the first row
    data.drop(index=["lat/lon"], inplace=True)
    return data
