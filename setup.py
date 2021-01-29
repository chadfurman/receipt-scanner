from setuptools import setup

setup(name='receipt-scanner',
      version='0.1',
      description='Takes pictures of receipts, orients them, sends them to Google\'s OCR API, parses the output into names and prices, adds categories, creates a CSV, and sends the CSV to Sheets',
      url='http://github.com/chadfurman/receipt-scanner',
      author='Chad Furman',
      author_email='chad@chadfurman.com',
      license='MIT',
      install_requires=[
          'pillow',
          'google-cloud-vision'
      ],
      zip_safe=False)
