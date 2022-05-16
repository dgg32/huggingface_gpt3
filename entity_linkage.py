import requests
import json
import csv
import re

local_cache_file = "./cache.tsv"
cache = {}
with open(local_cache_file, newline='') as csvfile:
    name_mapping = csv.reader(csvfile, delimiter='\t')
    for row in name_mapping:
        if len(row) == 2:
            cache[row[0]] = row[1]

def esearch(db, term):
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db={db}&term={term}&sort=relevance&format=json"

    content = json.loads(requests.get(url).content.decode('iso8859-1'))

    
    return content["esearchresult"]["idlist"]

def efecth(db, id):
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db={db}&id={id}"

    content = requests.get(url).content.decode('iso8859-1').split("\n")

    for line in content:
        if len(line) != 0 and line.startswith("1:"):
            content = line.replace("1:", "").strip()
            content = re.sub(r'\[.+?\]', '', content)
            return content

def name_disambiguation(name):
    if name.lower() in cache:
        return cache[name.lower()]
    
    else:
        ids = esearch("mesh", name)
        #print (ids)
        if len(ids) == 0:
            return None
        else:
            content = efecth("mesh", ids[0])
            cache[name.lower()] = content
            with open(local_cache_file, "a", newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter='\t')
                writer.writerow([name.lower(), content])
            return content


if __name__ == "__main__":
    print(name_disambiguation("xyloglucan"))