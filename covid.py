# Pycon2020 Covid tracking tutorial by Matt Harrison

# import and save URL to file
import urllib.request as req
url = 'https://raw.githubusercontent.com/COVID19Tracking/covid-tracking-data/master/data/states_daily_4pm_et.csv'
fname = 'covid.csv'
def fetch_url(url, fname):
    """Save a URL to a local file"""
    fin = req.urlopen(url)
    data = fin.read()
    with open(fname, mode='wb') as fout:
        fout.write(data)
<<<<<<< HEAD
=======

fname =  'test.csv'
fetch_url(url, fname)

>>>>>>> b7f8a704ae0493c16b410ad19c82c2335be44ad2
