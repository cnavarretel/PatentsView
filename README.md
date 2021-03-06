# PyUSPTO 
Download granted data from USPTO by countries with Python

## Example
For download granted patents to assignees in Chile, you must use the two-digits ISO 3166-2 code.

    def query(code):
        output = {
            "_and": [
                {"assignee_country": "CL"}        
            ]
        }
        return output

If you want customize the query, for more information visit http://www.patentsview.org/api/patent.html, where you can choose the most indicated field.

Hence, if you want download granted patents to assignees in Chile at 2015, the query is:

    def query(code):
        output = {
            "_and": [
                {"assignee_country": "CL",
                "patent_year": 2015}        
            ]
        }
        return output

## Advanced Options
This code include four fields: _assignee_country, cpc_group_id, patent_number, patent_year_
If you need add and/or remove fields, only you must edit _data["f"]_ in download() function.

    data["f"] = [
        "assignee_country", 
        "cpc_group_id", 
        "patent_number", 
        "patent_year",
        "inventor_country",
        "assignee_city",
        ...
        "assignee_lastknown_longitude"
    ]

More information about Public API in http://www.patentsview.org/api/query-language.html
