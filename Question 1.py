import requests
from bs4 import BeautifulSoup
import pandas as pd

def crawl_dell_jobs(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        job_listings = []
        
        job_cards = soup.find_all('li', class_='GWTCKCABBG')
        
        for card in job_cards:
            job_title_elem = card.find('span', class_='GWTCKCABAF GWTCKCABMF')
            job_title = job_title_elem.text.strip() if job_title_elem else 'Not available'
            
            location_elem = card.find('span', class_='GWTCKCABPF')
            location = location_elem.text.strip() if location_elem else 'Not available'
            
            req_id_elem = card.find('span', class_='GWTCKCABRF')
            req_id = req_id_elem.text.strip() if req_id_elem else 'Not available'
            
            job_link_elem = card.find('a', href=True)
            job_link = 'https://dell.wd1.myworkdayjobs.com' + job_link_elem['href'] if job_link_elem else 'Not available'
            
            job_data = {
                'Job Title': job_title,
                'Location': location,
                'Req Id': req_id,
                'Job Link': job_link
            }
            
            job_listings.append(job_data)
        
        return job_listings
    
    else:
        print(f"Failed to retrieve page, status code: {response.status_code}")
        return None

def export_to_excel(job_listings, filename):
    df = pd.DataFrame(job_listings)
    df.to_excel(filename, index=False)
    print(f"Data exported to {filename} successfully.")

# URL of the Dell job portal
url = 'https://dell.wd1.myworkdayjobs.com/en-US/External?Location_Country=c4f78be1a8f14da0ab49ce1162348a5e'

# Crawling the jobs
job_listings = crawl_dell_jobs(url)

# Exporting to Excel
if job_listings:
    export_to_excel(job_listings, 'dell_job_listings.xlsx')