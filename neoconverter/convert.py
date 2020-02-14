#! /usr/bin/env python3
import pandas as pd
import click

def _convert_one_file(filepath):
    """Returns a DataFrame modified as expected."""

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
    # now that the data is loaded in as strings (not numbers), we can set the
    # index/header correctly
    # set index from first column
    data.set_index(data.columns[0], inplace=True)
    # set column names to first row
    data.columns = data.iloc[0]
    # ... and then remove the first row
    data.drop(index=["lat/lon"], inplace=True)
  
    lat_lon = []
    value = []
    # Go through the rows (each representing a latitude)
    for lat, row in data.iterrows():
      # Go through the cols (each representing a longitude)
      for lon, val in row.iteritems():
        lat_lon.append("{},{}".format(lat, lon))
        value.append(val)
  
    new_data = pd.Series(value, index=lat_lon)
    new_df = pd.DataFrame(data=new_data, columns=["Values"])
    new_df.index.name = "lat_lon"
    return new_df
  
    # As a sanity check, the MY1DMM_CHLORA_2016-01-01_rgb_3600x1800.SS.CSV file
    # from NOAA has a value of "0.0393" at row 1125, column RN (or latitude
    # ~ -22.35000000, longitude -131.95). From testing this code on that file,
    # this value is set in the output data correctly.

@click.command()
@click.option(
    "-i",
    "--input-csv-for-excel-file",
    required=True,
    help="Input 'CSV for Excel' filepath.",
    type=str,
)
@click.option(
    "-o",
    "--output-tsv-file",
    required=True,
    help="Output TSV filepath.",
    type=str,
)
def convert(input_csv_for_excel_file, output_tsv_file) -> None:
    """Converts a geographically formatted CSV file to a two-column format.

       In particular, this assumes that the rows correspond to "chunks" of
       latitudes and the columns correspond to "chunks" of longitudes, and that
       the cell values correspond to some variable of interest within that
       latitude/longitude area.

       The output file produced from this is in a much simpler two-column
       format (each row has a lat/lon coordinate and the value in that "chunk")
       which may be easier to analyze.
       
       NOTE THAT this assumes that the rows and columns are labelled with the
       latitude/longitude values -- this requires selecting the "CSV for Excel"
       download option from NEO's website, not the plain "CSV" option.
    """

    converted_df = _convert_one_file(input_csv_for_excel_file)
    converted_df.to_csv(
        output_file_name, header=True, index=True, sep="\t"
    )

if __name__ == "__main__":
    convert()
