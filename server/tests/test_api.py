import requests
import json

url = 'http://localhost:8080/links'

# Additional headers.
headers = {'Content-Type': 'application/json'}

def test_post_links():

    # Body
    payload = {'LongLink': "https://peter-jp-xie.medium.com/rest-api-testing-using-python-751022c364b8", 'Email': 'pytestarticle@aeteXie.com'}

    # convert dict to json string by json.dumps() for body data.
    resp = requests.post(url, headers=headers, data=json.dumps(payload, indent=4))

    # test to create new short_link using new long_link
    assert resp.status_code == 200




def test_same_post_links():

    # Body
    payload = {'LongLink': "https://peter-jp-xie.medium.com/rest-api-testing-using-python-751022c364b8",
               'Email': 'pytestarticle@aeteXie.com'}

    # convert dict to json string by json.dumps() for body data.
    resp = requests.post(url, headers=headers, data=json.dumps(payload, indent=4))

    # test to fail creating new sort_url if using same long_url, should return 400
    resp = requests.post(url, headers=headers, data=json.dumps(payload, indent=4))
    assert resp.status_code == 400

def test_invalid_post_links():

    # Body
    payload = {'LongLink': "Invalid",
               'Email': 'INVALID@aeteXie.com'}

    # convert dict to json string by json.dumps() for body data.
    resp = requests.post(url, headers=headers, data=json.dumps(payload, indent=4))

    # test for invalid longLink or userEmail, should return 400
    resp = requests.post(url, headers=headers, data=json.dumps(payload, indent=4))
    assert resp.status_code == 400


