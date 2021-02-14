from distutils.core import setup
import py2exe
import sys, os

# sys.argv.append('stock2csv')

setup(name='stock2csv',
       version='1.0.0',
       description='Takes in a list of stock tickers along with a start date, end date, and file path from the user then'
                   'creates .csv files for each stock containing data between the specified times.',
       author='Adam Siwiec',
       author_email='adam2.siwiec@gmail.com',
       url='https://github.com/adamsiwiec1/stock2csv',
       # options={'py2exe': {'bundle_files': 2}},
      windows=[{'script': 'stock2csv.py'}],
      zipfile=None
      )