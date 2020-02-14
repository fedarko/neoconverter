#!/usr/bin/env python3
import pandas as pd
import os

# os.chdir("/home/c1carpen/bin/coral/metadata/noaa_chlorophylla/")

files=pd.read_csv('noaa_chlorophylla_list.txt', header=None, sep='\t', index_col = 0)

for file in files.index:
  raw_file_name = file + '.CSV'
  output_file_name = file + '_READABLE.csv'
  # The use of header=None and not specifying an index_col avoids a shitty bug
  # in pandas* where it'll try to "guess" the type of a column/row even if you
  # tell it not to. For numerical values this can have funky side effects like
  # converting "179.75" to "179.740000000" or something along those lines.
  # I don't *think* that should be a problem here but might as well be safe.
  #
  # * see https://stackoverflow.com/a/35058538/10730311
  data = pd.read_csv(raw_file_name, sep=',', header=None, dtype=str)

  # now that the data is loaded in as strings (not numbers), we can set the
  # index/header correctly
  data.set_index(data.columns[0], inplace=True) # set index from first column
  data.columns = data.iloc[0]                   # set column names to first row
  data.drop(index=["lat/lon"], inplace=True)    # ...and remove that first row

  lat_lon = []
  value = []
  # Go through the rows (each representing a latitude)
  for lat, row in data.iterrows():
    # Go through the cols (each representing a longitude)
    for lon, val in row.iteritems():
      lat_lon.append("{},{}".format(lat, lon))
      value.append(val)

  new_data = pd.Series(value, index=lat_lon)
  new_df = pd.DataFrame(data=new_data, columns = ["Values"])
  new_df.index.name = 'lat_long'
  new_df.to_csv(output_file_name, header=True, index=True, sep="\t")

  # As a sanity check, the MY1DMM_CHLORA_2016-01-01_rgb_3600x1800.SS.CSV file
  # from NOAA has a value of "0.0393" at row 1125, column RN (or latitude
  # ~ -22.35000000, longitude -131.95). From testing this code on that file,
  # this value is set in the output data correctly.
