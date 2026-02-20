import requests
from ..config.usa_jobs_api_key import usa_jobs_api_key

def fetch_usajobs(keyword, location="remote", results_per_page=5):
    
    headers = {
        "Host": "data.usajobs.gov",
        "User-Agent": "shayan.hussainzardari@gmail.com",
        "Authorization-Key": usa_jobs_api_key
    }

    params = {
        "Keyword": keyword,
        "LocationName": location,
        "ResultsPerPage": results_per_page
    }

    url = f"https://data.usajobs.gov/api/search?Keyword={keyword}&LocationName={location}&ResultsPerPage={results_per_page}"
    
    response = requests.get(url,headers=headers, params=params)
    
    if response.status_code == 200:
        return {
            "success": True,
            "type": type(response),
            "data": response.json().get('SearchResult', {}).get('SearchResultItems', [])
        }
    else:
        return {
            "success": False,
            "type": type(response),
            "data": response.json()
        }

if __name__ == "__main__":
    keyword = "Software Engineer"
    jobs = fetch_usajobs(keyword=keyword)
    if jobs.get('success'):
        for job in jobs.get('data', []):
            title = job['MatchedObjectDescriptor']['PositionTitle']
            agency = job['MatchedObjectDescriptor']['OrganizationName']
            print(f"{title} at {agency}")
    else: 
        print(jobs)