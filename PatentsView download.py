import requests
import json
import math
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest'
}

def query(code):
    output = {
        "_and": [
            {"assignee_country": code}        
        ]
    }
    return output

def queryBuilder(country):
    # Valid if are less that 100,000 results
    page = 1            # Default
    total_pages = 1     # Default
    per_page = 5000     # Divide the results in 5,000 per page
    
    data = {}

    # Customize this query
    data["q"] = query(country["code"])
    
    # Connect with PatentsView
    response = session.post(
        url = 'http://www.patentsview.org/api/patents/query',
        data = json.dumps(data),
        headers = headers
    )
    
    total_patent_count = float(response.json()['total_patent_count'])

    if(total_patent_count > per_page):
        total_pages = int(math.ceil(total_patent_count/per_page))

    # Verify n# of results
    if int(total_patent_count) < 100000:
        download(country, page, headers, total_pages, per_page)
    return True

def download(country, page, headers, total_pages, per_page):
    if(page <= total_pages):
        data = {}
        data["q"] = query(country["code"])
        # Cols to download
        data["f"] = [
            "assignee_country", 
            "cpc_group_id", 
            "patent_number", 
            "patent_year"
        ]
        data["o"] = {"per_page" : per_page, "page" : page}
        data["format"] = 'json'     # Format: json or xml

        # Connect with PatentsView
        response = session.post(
            url = 'http://www.patentsview.org/api/patents/query',
            data = json.dumps(data),
            headers = headers
        )

        # Create in folder directory "Data"
        directory = 'Data/' + country["name"]
        if not os.path.exists(directory):
            os.makedirs(directory)
        file = open(directory + '/' + country["code"] + " (" + str(page) + ").json", "w")
        file.write(response.text)
        file.close()

        print ("Sheet " + str(page) + " complete")
        page = page + 1
        download(country, page, headers, total_pages, per_page)

# Download data from USPTO
country = {
    "name": "Chile",
    "code": "CL"
}
queryBuilder(country)

    

