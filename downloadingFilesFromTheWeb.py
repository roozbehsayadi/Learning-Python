from urllib import request

csv_url = "https://www.stats.govt.nz/assets/Uploads/Household-living-costs-price-indexes/Household-living-costs-price-indexes-June-2019-quarter/Download-data/household-living-costs-price-indexes-june-2019-quarter-expenditure-weights.csv"


def download_data(csv_url):
	response = request.urlopen(csv_url)
	csv = response.read()
	csv_str = str(csv)
	lines = csv_str.split("\\r\\n")
	dest_url = r'test.csv'
	fx = open(dest_url, 'w')
	for line in lines:
		fx.write(line + '\n')
	fx.close()


download_data(csv_url)

