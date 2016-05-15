# pyArt - WikiArt SVM Predictor and Webcrawler
###### [Wikiart](http://www.wikiart.org/) web crawler and SVM art genere predictor

This project is made of three parts:  
1. Wikiart scraper using [scrapy](http://scrapy.org/)  
2. Robust image descriptor extractor using [scikit image](http://scikit-image.org/)  
3. Support vector machine the relies on data scraped from wikiart to recognize images it is given  
##### Please feel free to contact me for help, i'd be glad to support (:

###Usage:
To install run:
```
python setup.py
```

And to use the predictor run:
```python
from image_predictor.multiclass_svm import MultiClassSVM

predictor = MultiClassSVM('data_set_file_path')
predictor.predict('image.jpg')
```
>
*you can find a built dataset in the data folder  
and you could also build yours using the image vectorizer (more below..)*

To use the vectorizer run:
```python
from image_vectorizer.vectorizer import get_descriptor

descriptor = get_descriptor([numpy format image, b/w or rgb])
```
>
*you can save this data to a json file or pass it directly to   
the SVM using the SVM's 'fit' function*

To run the scraper run:
```
scrapy crawl wikiart_global
```
>
*note that the scraper already saved the new scraped data to a data log  
so no fuss about it*

###Project Structure:
```
├── __init__.py
├── data --> logging and scraped data location
│   ├── scrapy_log.log
│   └── wikiart_data.json
├── image_predictor --> SVM art predictor machine
│   ├── __init__.py
│   └── multiclass_svm.py
├── image_vectorizer --> image descriptor extractor
│   ├── __init__.py
│   └── vectorizer.py
├── scrapinghub.yml
├── scrapy.cfg
├── setup.py
└── webcrawler --> wikiart web crawler
    ├── __init__.py
    ├── items.py --> art piece item scraping schema
    ├── pipelines.py --> data processing pipelines
    ├── settings.py
    └── spiders
        ├── __init__.py
        └── wikiart_crawler.py --> the webcrawled used to scrape wikiart
```
###MIT License

Copyright (c) 2016 Shaked Lokits

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
