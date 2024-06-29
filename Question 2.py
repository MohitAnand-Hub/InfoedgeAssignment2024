import requests
from bs4 import BeautifulSoup
import re
import csv

def scrape_bentley_jobs():
    base_url = "https://jobs.bentley.com/search"
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    job_listings = []

    job_cards = soup.find_all('div', class_='job-tile')
    for job_card in job_cards:
        job_title = job_card.find('a', class_='job-link').text.strip()
        job_location = job_card.find('span', class_='job-location').text.strip()
        job_link = job_card.find('a', class_='job-link')['href']
        
        # Extract job date using regex if it's not available
        job_date_tag = job_card.find('span', class_='job-date')
        if job_date_tag:
            job_date = job_date_tag.text.strip()
        else:
            job_date_pattern = re.compile(r'\b\d{2}-\w{3}-\d{2}\b')
            job_date_match = job_date_pattern.search(response.text)
            job_date = job_date_match.group(0) if job_date_match else 'N/A'

        job_listings.append({
            'jobTitle': job_title,
            'jobLocation': job_location,
            'jobLink': f"https://jobs.bentley.com{job_link}",
            'jobDate': job_date
        })

    # Save to CSV
    csv_output = 'bentley_jobs.csv'
    with open(csv_output, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['jobTitle', 'jobLocation', 'jobLink', 'jobDate'])
        writer.writeheader()
        for job in job_listings:
            writer.writerow(job)
    
    return csv_output

# Run the scraper function
csv_file = scrape_bentley_jobs()
print(f"Job listings have been saved to {csv_file}")
