import json
import string,random
from pymongo import MongoClient
from flask import Flask, request, redirect
from bson.json_util import dumps

#creating client connection to mongoDB instance running on local machine
client = MongoClient('mongodb://my_db:27017')
db = client.URL_SortenerDB

app = Flask(__name__)



# @app.route('/user')
# def get_user():
''' *********************** FROM APP2 *********************** '''
@app.route('/')
def HelloUser():
    return 'Hello, you are using App2'

''' *********************** Creating new user *********************** '''
@app.route('/users',methods=['POST'])
def post_user():
    print('Im in users route')
    try:
        '''creating a new user, if user exists return error message else create user'''
        data = json.loads(request.data)
        firstName = data['FirstName']
        lastName = data['LastName']
        email = data['Email']

        if firstName and lastName and email:
            db.users.insert_one({
                "FirstName": firstName,
                "LastName": lastName,
                "Email": email
            })

        return dumps({'message': 'SUCCESS'}), 200

    except Exception as e:
        return dumps({'error': str(e)})


''' *********************** Creating new sort_URL *********************** '''
@app.route('/links',methods = ['post'])
def post_link():
    """
    function to create new link
    """
    length = 6
    # create new link
    try:
        data = json.loads(request.data)
        longLink = data['LongLink']
        userEmail = data['UserEmail']

        if longLink and userEmail:
            sort_link = "http://localhost:5002/" + ''.join(random.sample(string.ascii_letters + string.digits, length)) + "/"
            db.links.insert_one({
                "LongLink": longLink,
                "SortLink": sort_link,
                "UserEmail": userEmail
            })

            return 'here is sort link' + sort_link, 200

    except Exception as e:
        return dumps({'error': str(e)})



''' *********************** get long_URL *********************** '''
@app.route('/<sort_link>',methods = ['GET','POST'])
def get_link(sort_link):
    """
    function to get long link
    """

    # create new link
    try:
        '''Do Something'''

    except:
        '''why you giving error?'''



''' *************************************************************** '''
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

