# GitHub Repository Analyzer

A Python tool that uses the GitHub REST API to retrieve repository information for a GitHub user, analyze the data, and export the results to a CSV file.

## Features

- Connects to the GitHub REST API
- Retrieves public repositories
- Handles API pagination
- Extracts useful repository information
- Handles missing descriptions
- Converts API data into a Pandas DataFrame
- Exports repository data to CSV

## Data Collected

- Repository name
- Primary language
- Star count
- Description
- Repository URL
- Fork count

## Technologies

- Python
- Requests
- GitHub REST API
- Pandas

## How It Works

GitHub username
       ↓
GitHub REST API
       ↓
JSON response
       ↓
Pagination
       ↓
Python processing
       ↓
Pandas DataFrame
       ↓
repositories.csv

## How to Run

Install the required packages:

pip install -r requirements.txt

Run the analyzer:

python analyzer.py

The program will retrieve the user's public repositories and create:

repositories.csv

## Project Structure

github-repo-analyzer/
├── README.md
├── analyzer.py
├── repositories.csv
└── requirements.txt
