# TikTok Metadata Extraction via Google Custom Search API

This Python script automates the extraction of TikTok video metadata using the Google Custom Search JSON API. It was used in support of research into the quality and content of dental health information on TikTok.

## 🔍 Purpose

The script:
- Performs a Google Custom Search constrained to TikTok URLs
- Retrieves paginated results (up to 100)
- Saves metadata including title, link, snippet, and structured data to a CSV file

## 📁 Output

A CSV file (default: `results_wanted.csv`) will be saved in the `results/` folder, containing structured search result information.

## 🔧 Usage

1. Replace placeholders in the script:
   - `API_KEY` with your Google Custom Search API key
   - `CX` with your Custom Search Engine ID
   - `QUERY` with your TikTok search term
   - `OUTPUT_FILE` name (optional)

2. Run the script:
```bash
python script_name.py
