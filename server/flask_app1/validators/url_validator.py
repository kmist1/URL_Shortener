from urllib.parse import urlparse

def isURL_valid(url):
    try:
        parsedURL = urlparse(url)
        if parsedURL.scheme:
            print("URL is Valid")
            return True
        else:
            print("URL is not valid")
            return False
    except Exception as e:
        print("Error: ",e)