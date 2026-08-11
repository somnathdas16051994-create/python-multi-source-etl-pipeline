# Multi-Source ETL Data Pipeline

A Python-based ETL (Extract, Transform, Load) pipeline that extracts data from multiple sources such as Excel, JSON, and SharePoint, processes the data using Pandas, and loads the cleaned data into MySQL.

## Project Flow

Excel ───────┐
             │
JSON ────────┼──> Pandas DataFrame ──> Transform ──> MySQL
             │
SharePoint ──┘

## Project Overview

The pipeline follows a simple ETL architecture:

```text
                 ┌─────────────────┐
                 │  Excel File     │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │                 │
                 │  Data Extraction│
                 │                 │
                 └────────┬────────┘
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
        ▼                 ▼                 ▼
   Excel Data        JSON Data       SharePoint Data
        │                 │                 │
        └─────────────────┼─────────────────┘
                          ▼
                 ┌─────────────────┐
                 │     Pandas      │
                 │  DataFrame      │
                 └────────┬────────┘
                          ▼
                 ┌─────────────────┐
                 │   Transform &   │
                 │   Clean Data    │
                 └────────┬────────┘
                          ▼
                 ┌─────────────────┐
                 │      MySQL      │
                 │    Database     │
                 └─────────────────┘

## Features

- Extract data from Excel files
- Extract data from JSON files
- Extract data from SharePoint using Microsoft Graph API
- Authenticate with Microsoft Graph using MSAL
- Combine multiple data sources using Pandas
- Remove duplicate records
- Handle missing values
- Load processed data into MySQL
- Use SQLAlchemy for database connectivity
- Use environment variables for configuration and credentials
- MySQL UPSERT using `ON DUPLICATE KEY UPDATE`

## Technology Stack

- Python
- Pandas
- Microsoft Graph API
- MSAL
- Requests
- SQLAlchemy
- PyMySQL
- MySQL
- python-dotenv

## Project Structure

```text
python-multi-source-etl-pipeline/
│
├── app/
│   ├── config/
│   │   └── settings.py
│   │
│   ├── database/
│   │   └── mysql_service.py
│   │
│   ├── extract/
│   │   ├── excel_extractor.py
│   │   ├── json_extractor.py
│   │   └── sharepoint_extractor.py
│   │
│   ├── transform/
│   │   └── data_transform.py
│   │
│   └── utils/
│       └── logger.py
│
├── data/
│   ├── mock/
│   └── raw/
│
├── tests/
├── main.py
├── requirements.txt
├── .gitignore
└── README.md