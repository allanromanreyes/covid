# Pycon2020 Covid tracking tutorial by Matt Harrison
import urllib.request as req

url = 'https://raw.githubusercontent.com/COVID19Tracking/covid-tracking-data/master/data/states_daily_4pm_et.csv'

def get_url(url, filename):
    """Save a URL to a local file"""
    fin = req.urlopen(url)
    data = fin.read()
    with open(filename, mode='wb') as fout:
        fout.write(data)

