from distutils.core import setup
import py2exe
import sys

# sys.argv.append('stock2csv')

setup(#name='stock2csv',
      # version='1.0.0',
      # description='Takes in a list of stock tickers along with a start date, end date, and file path from the user then'
      #             'creates .csv files for each stock containing data between the specified times.',
      # author='Adam Siwiec',
      # author_email='adam2.siwiec@gmail.com',
      # url='https://github.com/adamsiwiec1/stocktocsv',
      # # package_dir={'Lib': 'Z:\\test'},
      # # options={'py2exe': {'includes': ['lxml._elementpath']}},
      console=['stock2csv.py']
      )