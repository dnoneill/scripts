#written by Niqui O'Neill October 18, 2017
#This script allows users to download metadata from LOC digital collections and writes it to a csv named for the collection
#It allows for users to either download a collection using that collection's URL with collection()
#Or allows users to search loc.gov with query()
#get_data() grabs all the results from a search, adds the contents to a list and writes the list to a csv file. 
#This can easily be dumped to a json file by writing "data" to a json object instead of a csv
#install requests and unicodecsv before running (pip install requests)(pip install unicodecsv)
#to run $python loc_get_data.py
import requests
import unicodecsv as csv
data = []
def collection():
    try:
        collection_url = raw_input("Enter LOC url for collection: ") #python2
    except:
        collection_url = input("Enter LOC url for collection: ")#python3
    params = {} #lines 11-13 set the parameters for the urls
    params['fo'] = "json"
    params['c'] = '150'
    collections_json = requests.get(collection_url, params=params).json()
    get_data(collections_json)

def query():
    try:
        query = raw_input("Enter Query String or URL: ") #python2
    except:
        query = input("Enter Query String or URL: ") #python3
    if 'http' in query:
	    params = {}
	    params['fo'] = 'json'
	    params['c'] = '150'
	    collections_json = requests.get(query, params=params).json()
	    get_data(collections_json)
    else:
	    query = query.replace(" ", "+")
	    url = "https://www.loc.gov/search/"
	    params = {}
	    params['fo'] = 'json'
	    params['q'] = query
	    params['all'] = 'true'
	    params['c'] = '150'
	    collections_json = requests.get(url, params=params).json()
	    get_data(collections_json)
    
def get_data(collections_json):
    x = 0
    #lines 48-58 based on code from https://github.com/LibraryOfCongress/data-exploration/blob/master/LOC.gov%20JSON%20API.ipynb
    #Under heading "Why does it stop after 40?"
    while True: #As long as we have a next page, go and fetch it
        for collection in collections_json["results"]:
            data.append(collection)
            x += 1
        next_page = collections_json["pagination"]["next"] #get the next page url
        if next_page is not None: #make sure we haven't hit the end of the pages
            collections_json = requests.get(next_page).json()
        else:
            break #we are done and can stop looping
    title=collections_json['facet_trail'][0]['value'].replace(" ", "_").replace("'", "").replace(".", "").replace(",", "").replace("+","_") #creates title for csv file created at end of script
    title = title+".csv" #adds extension
    total_records = collections_json['pagination']['of']
    print("%s records collected" % total_records)
    fieldnames = ['title', 'other_title'] #ensures that first two rows are title and other_title
    
    for row in data:
        for key, value in row.items():
            if type(value) == list and key != 'segments': #replaces list values in data with strings with items seperated by commas
                value = '; '.join(value)
                row[key] = value         

    for row in data:
        for key, value in row.items(): #goes through all dictionary keys, adds keys if not already in fieldnames list
            if key not in fieldnames:
                fieldnames.append(key)
    try: #mac 
        with open(title, "w") as f: #opens csv with title from earlier in script
            writer = csv.DictWriter(f, fieldnames=fieldnames) #opens unicodecsv
            writer.writeheader() #writes header row
            for row in data: #for dictionary in data
                writer.writerow(row) #write row with row data
    except: #windows
        with open(title, "wb") as f: #opens csv with title from earlier in script
            writer = csv.DictWriter(f, fieldnames=fieldnames) #opens unicodecsv
            writer.writeheader() #writes header row
            for row in data: #for dictionary in data
                writer.writerow(row) #write row with row data
def main():
    try:
        type = raw_input("Query or Collection download? (Q/C): ") #python2
    except:
        type = input("Query or Collection download? (Q/C): ") #python3
    if "Q" in type or "q" in type:
        query()
    elif "C" in type or "c" in type:
        collection()
    else:
    	print("{} Entered\nNot Valid Option".format(type))
    	main()
    	  
if __name__ == "__main__":
    main()
