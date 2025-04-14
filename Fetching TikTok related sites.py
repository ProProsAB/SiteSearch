import requests
import csv 
from datetime import datetime, timedelta
import sys
import os

# Replace with your actual API Key and CX
API_KEY = "Code for api"
CX = "required"


# Query parameters
QUERY = "Your search" #enter your google search term
NUM_RESULTS = 10
SITE_SEARCH = "tiktok.com"
START_DATE = "2021-01-01"  # Start date in YYYY-MM-DD format
OUTPUT_FILE = "results_wanted.csv" # enter your requested file
OUTPUT_DIR = "results/"  # Directory to save output files

BASE_URL = "https://customsearch.googleapis.com/customsearch/v1"

def fetch_results(start, start_date):
    """Fetch results using Google Custom Search API with a start date."""
    params = {
        "key": API_KEY,
        "cx": CX,
        "q": QUERY,
        "start": start,
        "num": NUM_RESULTS,
        "siteSearch": SITE_SEARCH,
        "sort": f"date:r:{start_date}:"
    }
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    return response.json()

def save_to_csv(results, file_name, append=False):
    """Save results to a CSV file."""
    mode = "a" if append else "w"
    with open(file_name, mode, newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)
        
        # Write header only once
        if not append:
            writer.writerow(["Title", "Link", "Snippet", "Formatted URL", "Display Link", "Other Metadata"])

        for result in results:
            writer.writerow([
                result.get("title", "N/A"),
                result.get("link", "N/A"),
                result.get("snippet", "N/A"),
                result.get("formattedUrl", "N/A"),
                result.get("displayLink", "N/A"),
                str(result.get("pagemap", {}))
            ])

def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    for page in range(1, 11):  # Max 10 pages per iteration
        start_index = (page - 1) * NUM_RESULTS + 1
        print(f"Fetching results for page {page} (start index: {start_index})...")

        try:
            results = fetch_results(start_index, START_DATE)
            items = results.get("items", [])
            
            # Save results incrementally
            save_to_csv(items, f"{OUTPUT_DIR}{OUTPUT_FILE}", append=True)

            if len(items) < NUM_RESULTS:
                print(f"Fewer than {NUM_RESULTS} results on page {page}, stopping...")
                break

        except requests.exceptions.RequestException as e:
            print(f"Error fetching results on page {page}: {e}")
            break

    print(f"Finished fetching results. Total results saved to {OUTPUT_FILE}.")

if __name__ == "__main__":
    main()
