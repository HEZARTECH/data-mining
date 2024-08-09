# Data Mining / Scraping ~ HEZARTECH.AI

A data mining / scraping repository for our TDDI Model. (HEZARTECH.AI)
This files used for data mining/scraping scripts for preparing and synthesizing dataset.

## Table of Concepts

* Installation
* Websites that we scraped data
* Synthesizing dataset.
* Folder Structure

## Installation

```bash
$ pip3 install -r requirements.txt
```

---

## Websites that we scraped data

* X (formerly Twitter): For getting customer service conversations etc.
* Amazon: 1, 4 and 5 star comments of best seller products to analyze sentiments.
* ŞikayetVar: articles
* Synthesizing Dataset: via Generative AI.

## Synthesizing dataset

We synthesis dataset with manually labelled

## Folder Structure

```bash
.
|   .gitignore
|   LICENSE.md
|   README.md
|   requirements.txt
|
+---Amazon
|   |   b0.txt
|   |   fetchAmazonData.py
|   |   pattern_finder.py
|   |   url_otomation.py
|   |   urunid.txt
|   |
|   \---results
|           amazon_dataset.txt
|           besyildizurl.txt
|           biryildizurl.txt
|           dortyildizurl.txt
|
+---Dataset Optimization
|       csv_validator.py
|       dataset_cleaner.py
|       Data_Visulator.ipynb
|       delete_dup.py
|       delete_short_sentences.py
|       json_to_csv.py
|
+---SikayetVar
|       sikayetvar.py
|
\---X
        headers.json
        twitter_search_engine.py
```
