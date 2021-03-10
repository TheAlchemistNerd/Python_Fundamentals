import json
# Here the JSON data is in a big string named json_string,
# It starts and the first triple quotation marks and extends
# down to the last triple quotation marks.
json_string = """
{
"1": {
    "count": 9061,
    "lastreferrer": "https://difference-engine.com/Courses/tml-5-1118/",
    "lastvisit": "12/20/2018",
    "page": "/etg/downloadpdf.html"
},
"2": {
    "count" : 3342,
    "lastreferrer" : "https://alansimpson.me/",
    "lastvisit" : "12/19/2018",
    "page" : "/html_css/index.html"
}
}
"""

# Load the JSON data from the big json_string string.
hits_data = json.loads(json_string)

#Now you can loop through the hits_data collection.
for k, v in hits_data.items():
    print(f"{k}. {v['count']:>5} - {v['page']}")