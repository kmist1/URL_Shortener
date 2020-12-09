import requests
import json

def test_post_links():
    url = 'http://localhost:8080/links'

    # Additional headers.
    headers = {'Content-Type': 'application/json'}

    # Body
    payload = {'LongLink': "abcdc", 'key2': 'pytestArticle@PeteXie.com'}

    # convert dict to json string by json.dumps() for body data.
    resp = requests.post(url, headers=headers, data=json.dumps(payload, indent=4))
    assert resp.status_code == 200
    # assert resp.json()["message"] == 1
    print(resp)
    print(resp.text)
