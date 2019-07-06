import pandas as pd
import numpy as np
import os


# change the start and end date

START_DATE = "2018-07-01"
END_DATE = "2018-08-01"


if "cleaned_data_uniques" not in os.listdir("."):
	os.makedirs("cleaned_data_uniques")

for filename in os.listdir("."):
	if filename.endswith(".csv"): 
		dt = pd.read_csv(filename, header=0)
		dt["location_at"] = pd.to_datetime(dt["location_at"])

		dt = dt[(dt["horizontal_accuracy"] <= 200) & 
			(dt["advertiser_id"] != None) & 
			(dt["advertiser_id"] != "00000000-0000-0000-0000-000000000000") & 
			(dt["country"] == "US") &
			(dt["location_at"] >= pd.to_datetime(START_DATE)) &
			(dt["location_at"] <= pd.to_datetime(END_DATE))]

		unique_ids = np.array(dt.sort_values("advertiser_id")["advertiser_id"].unique())

		newfilename = dt["store_name"].values[0] + "_Uniques_" + START_DATE + "_" + END_DATE

		np.savetxt("cleaned_data_uniques/" + newfilename + ".csv", unique_ids, fmt="%5s")