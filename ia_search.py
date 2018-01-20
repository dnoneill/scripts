import requests
import math
import unicodecsv as csv

def ia_keyword(query, delimiter):
    params = {}
    query = query.replace(" ", "+") #replaces spaces with plus signs, easier for searching
    url = 'https://archive.org/advancedsearch.php' 
    params['q'] = query
    params['fl%5B%5D'] = 'avg_rating&fl%5B%5D=backup_location&fl%5B%5D=btih&fl%5B%5D=call_number&fl%5B%5D=collection' \
    '&fl%5B%5D=contributor&fl%5B%5D=coverage&fl%5B%5D=creator&fl%5B%5D=date&fl%5B%5D=description&fl%5B%5D=downloads' \
    '&fl%5B%5D=external-identifier&fl%5B%5D=foldoutcount&fl%5B%5D=format&fl%5B%5D=genre&fl%5B%5D=headerImage' \
    '&fl%5B%5D=identifier&fl%5B%5D=imagecount&fl%5B%5D=indexflag&fl%5B%5D=language&fl%5B%5D=licenseurl&fl%5B%5D=mediatype' \
    '&fl%5B%5D=members&fl%5B%5D=month&fl%5B%5D=name&fl%5B%5D=noindex&fl%5B%5D=num_reviews&fl%5B%5D=oai_updatedate' \
    '&fl%5B%5D=publicdate&fl%5B%5D=publisher&fl%5B%5D=related-external-id&fl%5B%5D=reviewdate&fl%5B%5D=rights' \
    '&fl%5B%5D=scanningcentre&fl%5B%5D=source&fl%5B%5D=stripped_tags&fl%5B%5D=subject&fl%5B%5D=title&fl%5B%5D=type' \
    '&fl%5B%5D=volume&fl%5B%5D=week&fl%5B%5D=year'
    params['sort%5B%5D'] = '&sort%5B%5D=&sort%5B%5D=' #params['fl%5B%5D'] determines which areas to search. Dicts do not allow for multiple of the same type, which is why the long string
    params['rows'] = '1000' #number of records to return
    params['page'] = '1' #start page
    params['output'] = 'json'
    if delimiter == '' or delimiter == None:
    	delimiter = ';'
    get_data_ia(url, params, query, delimiter)

def ia_advancedsearch(title, creator, mediatype, delimiter):
    params = {}
    query_string = ''
    mediatype = mediatype.replace(" ", "+")
    title = title.replace(" ", "+")
    creator = creator.replace(" ", "+")
    if title != ''  and title != None:
    	query_string += 'title%3A%28{}%29'.format(title)
    if creator != ''  and creator != None:
    	if query_string != '':
    		query_string += '+AND+creator%3A%28{}%29'.format(creator)
    	else:
    		query_string += 'creator%3A%28{}%29'.format(creator)
    if mediatype != ''  and mediatype != None:
    	if query_string != '':
    		query_string += '+AND+mediatype%3A%28{}%29'.format(mediatype)
    	else:
    		query_string += 'mediatype%3A%28{}%29'.format(mediatype)		
    query = title +"_"+ creator +"_"+ mediatype
    url = 'https://archive.org/advancedsearch.php' 
    params['q'] = query_string
    params['fl%5B%5D'] = 'avg_rating&fl%5B%5D=backup_location&fl%5B%5D=btih&fl%5B%5D=call_number&fl%5B%5D=collection' \
    '&fl%5B%5D=contributor&fl%5B%5D=coverage&fl%5B%5D=creator&fl%5B%5D=date&fl%5B%5D=description&fl%5B%5D=downloads' \
    '&fl%5B%5D=external-identifier&fl%5B%5D=foldoutcount&fl%5B%5D=format&fl%5B%5D=genre&fl%5B%5D=headerImage' \
    '&fl%5B%5D=identifier&fl%5B%5D=imagecount&fl%5B%5D=indexflag&fl%5B%5D=language&fl%5B%5D=licenseurl&fl%5B%5D=mediatype' \
    '&fl%5B%5D=members&fl%5B%5D=month&fl%5B%5D=name&fl%5B%5D=noindex&fl%5B%5D=num_reviews&fl%5B%5D=oai_updatedate' \
    '&fl%5B%5D=publicdate&fl%5B%5D=publisher&fl%5B%5D=related-external-id&fl%5B%5D=reviewdate&fl%5B%5D=rights' \
    '&fl%5B%5D=scanningcentre&fl%5B%5D=source&fl%5B%5D=stripped_tags&fl%5B%5D=subject&fl%5B%5D=title&fl%5B%5D=type' \
    '&fl%5B%5D=volume&fl%5B%5D=week&fl%5B%5D=year'
    params['sort%5B%5D'] = '&sort%5B%5D=&sort%5B%5D=' #params['fl%5B%5D'] determines which areas to search. Dicts do not allow for multiple of the same type, which is why the long string
    params['rows'] = '1000' #number of records to return
    params['page'] = '1' #start page
    params['output'] = 'json'
    if delimiter == '' or delimiter == None:
    	delimiter = ';'
    get_data_ia(url, params, query, delimiter)
    
def get_data_ia(url, params, query, delimiter):
    params_str = "&".join("%s=%s" % (k,v) for k,v in params.items())
    iadata = requests.get(url, params=params_str)
    iadata = iadata.json()
    pages = math.ceil(iadata['response']['numFound']/int(params['rows']))
    x = 0
    start = 2
    data = []
    while True:
        for iarecord in iadata['response']['docs']:
            data.append(iarecord)
            x += 1
        params['page'] = str(start)
        params_str = "&".join("%s=%s" % (k,v) for k,v in params.items())
        start += 1
        if int(params['page']) <= pages:
            iadata = requests.get(url, params=params_str)
            iadata = iadata.json()
        else:
            break
    print("%s records retrieved"%x)
    fieldnames = ['title', 'creator']
    delimiter = delimiter + ' '
    for row in data:
        for key, value in row.items(): #goes through all dictionary keys, adds keys if not already in fieldnames list
            if key not in fieldnames:
                fieldnames.append(key)
            if type(value) == list: #replaces list values in data with strings with items seperated by commas
                value = delimiter.join(value)
                row[key] = value  

    try: #mac 
        with open("%s.csv"%query, "w") as f: #opens csv with title from earlier in script
            writer = csv.DictWriter(f, fieldnames=fieldnames) #opens unicodecsv
            writer.writeheader() #writes header row
            for row in data: #for dictionary in data
                writer.writerow(row) #write row with row data
    except: #windows
        with open("%s.csv"%query, "wb") as f: #opens csv with title from earlier in script
            writer = csv.DictWriter(f, fieldnames=fieldnames) #opens unicodecsv
            writer.writeheader() #writes header row
            for row in data: #for dictionary in data
                writer.writerow(row) #write row with row data

            
def main():
    try:
        type = raw_input("Keyword or Advanced (Title, Creator, Mediatype) Search (K/A): ") #python2
    except:
        type = input("Keyword or Advanced (Title, Creator, Mediatype) Search (K/A): ") #python3
    if "K" in type or "k" in type:
        try:
            query = raw_input("Enter Query: ") #python2
        except:
            query = input("Enter Query: ") #python3
        try:
            delimiter = raw_input("Enter Delimiter, leave blank for semi-colon: ") #python2
        except:
            delimiter = input("Enter Delimiter, leave blank for semi-colon: ") #python3
        ia_keyword(query, delimiter)
    if "A" in type or "a" in type:
        try:
            title = raw_input("Enter Title: ") #python2
        except:
            title = input("Enter Title: ") #python3
        try:
            creator = raw_input("Enter Creator: ") #python2
        except:
            creator = input("Enter Creator: ") #python3
        try:
            mediatype = raw_input("Enter Mediatype (audio, collection, data, image, movies, texts, web): ") #python2
        except:
            mediatype = input("Enter Mediatype (audio, collection, data, image, movies, texts, web): ") #python3
        try:
            delimiter = raw_input("Enter Delimiter, leave blank for semi-colon: ") #python2
        except:
            delimiter = input("Enter Delimiter, leave blank for semi-colon: ") #python3
        ia_advancedsearch(title, creator, mediatype, delimiter)
    else:
    	print("{} Entered\nNot Valid Option".format(type))
    	main()
        
if __name__ == "__main__":
    main()