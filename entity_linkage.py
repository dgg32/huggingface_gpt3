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

    #print (url)
    if "idlist" in content["esearchresult"]:
        return content["esearchresult"]["idlist"]
    else:
        return []

def efecth(db, id):
    url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db={db}&id={id}"

    content = requests.get(url).content.decode('iso8859-1').split("\n")

    for line in content:
        if len(line) != 0 and line.startswith("1:"):
            content = line.replace("1:", "").strip()
            content = re.sub(r'\[.+?\]', '', content)
            return content

def name_disambiguation(name):
    to_replace = {"&beta;":"beta", "&alpha;": "alpha", "&gamma;": "gamma", "&delta;": "delta", "&epsilon;": "epsilon", "&zeta;": "zeta", "&eta;": "eta", "&theta;": "theta", "&iota;": "iota", "&kappa;": "kappa", "&lambda;": "lambda", "&mu;": "mu"}

    for t in to_replace:
        if t in name:
            name = name.replace(t, to_replace[t])

    if name.lower() in cache:
        return cache[name.lower()]
    
    else:
        ids = esearch("mesh", name)
        #print (ids)
        content = ""
        if len(ids) == 0:
            pass
        else:
            content = efecth("mesh", ids[0])
            cache[name.lower()] = content.lower()
        with open(local_cache_file, "a", newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter='\t')
            writer.writerow([name.lower(), content.lower()])
        return content.lower()


if __name__ == "__main__":
    print(name_disambiguation("amorphous cellulose"))