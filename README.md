# VA Ethics Scraper

A scraper for the [Virginia Conflict of Interest and Ethics Advisory Council](http://ethicssearch.dls.virginia.gov/) website. It creates a CSV file with all results and downloads the linked PDF forms.

## Running

First, set up and activate a Python virtual environment by following [these excellent instructions](http://docs.python-guide.org/en/latest/dev/virtualenvs/) from *The Hitchhiker's Guide to Python*.

With your virtual environment activated, install the dependencies for this software:

```
pip install -r requirements.txt
```

With the dependencies installed, you can run the scraper using the `scrapy` command line tool:

```
scrapy crawl -o output.csv -t csv lobbyist
```

This runs the `lobbyist` spider and outputs its data in a CSV called `output.csv`. To adjust where the PDFs are downloaded, change the `FILES_STORE` setting in `va_ethics_scraper/settings.py`.
