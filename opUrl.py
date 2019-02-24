import urllib.request
import re
import shutil

def url_web(address):
    with urllib.request.urlopen(address) as resq:
        html = resq.read()
        info = re.findall(r'<a href=\"([a-zA-z0-9_\S]+/?)\">', str(html))
        info.pop(0)
        try:
            info.remove("./_unsorted")
        except ValueError as err:
            print("")
    return info

def url_download(address, filename):
    print(address+filename)
    # request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(address+filename) as response, open(filename.replace("%20", " "), 'wb') as out_file:
        shutil.copyfileobj(response, out_file)


def url_back(back):
    url = back.split("/")
    num = 0
    for a in url:
        num = num + num
        if a == "":
            url.remove("")
    newUrl = ""
    if url[len(url)-1]+"/" == "anime-ost/":
        newUrl = back
    else:
        newUrl = back.replace(url[len(url)-1]+"/", "")
    return newUrl
