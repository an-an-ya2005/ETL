# ETL
ETL Pipeline
About
-----
This project is a simple ETL (Extract, Transform, Load) pipeline built using Python.

The pipeline:
-------------
Extracts data from a public API

Transforms and cleans the data

Loads the processed data into a local JSON file

This simulates how real companies automate data collection and preparation for analytics and AI systems.

Tech Stack:
----------
Python

Requests library

How to Run
----------
python -m pip install -r requirements.txt
python src/etl/pipeline.py

Output
------
Processed data is saved in:

data/processed/products.json
