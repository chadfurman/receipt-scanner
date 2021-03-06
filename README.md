# Receipt Scanner

Using Google Vision API, process some images into a CSV for use in cataloging your grocery purchases

## Requirements

Note some of the dependencies require python development libraries and C++, in Fedora you can install these as follows (note the # implies root prompt or sudo):

```
# dnf install libjpeg-dev gcc-c++ kernel-devel python3-devel
```

Then install the Python package dependencies with the following command (note the $ implies "user prompt" rather than root or sudo)
```
$ pip3 install . 
```

also install the google sdk: https://cloud.google.com/sdk/docs/install

 

## See Also

* Google Vision API: https://github.com/googleapis/python-vision
* Google client library quickstart: https://cloud.google.com/vision/docs/quickstart-client-libraries

## TODO

* Parse product name and prices from OCR output
  * The OCR text doesn't spit out product name in a single line, and sometimes the price is on the first line but the name is split across two lines which makes this slightly challenging
