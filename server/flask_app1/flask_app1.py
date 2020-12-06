import json
import string,random
from pymongo import MongoClient
from flask import Flask, request, redirect
from bson.json_util import dumps
from validators.email_validator import isEmail_valid
from validators.url_validator import isURL_valid

#creating client connection to mongoDB instance running on local machine
client = MongoClient('mongodb://my_db:27017')
db = client.URL_SortenerDB

app = Flask(__name__)



# @app.route('/user')
# def get_user():
''' *********************** FROM APP1 *********************** '''
@app.route('/')
def HelloUser():
    return 'Hello, you are using App1'

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
            # do validation checks here
            isEmail = isEmail_valid(email)
            if isEmail:
                db.users.insert_one({
                    "FirstName": firstName,
                    "LastName": lastName,
                    "Email": email
                })
                return dumps({'message': 'SUCCESS'}), 200
            else: return "Email is not valid",500

    except Exception as e:
        return dumps({'error': str(e)})


''' *********************** Creating new sort_URL *********************** '''
@app.route('/links',methods = ['post'])
def post_link():
    length = 6
    try:
        data = json.loads(request.data)
        longLink = data['LongLink']
        userEmail = data['UserEmail']
        print(longLink, userEmail)

        if longLink and userEmail:
            print(longLink,userEmail)
            # do validation checks here
            isEmail = isEmail_valid(userEmail)
            isURL = isURL_valid(longLink)
            print(isEmail,isURL)
            if isEmail and isURL:
                sort_link = "http://localhost:5001/" + ''.join(
                    random.sample(string.ascii_letters + string.digits, length)) + "/"
                db.links.insert_one({
                    "LongLink": longLink,
                    "SortLink": sort_link,
                    "UserEmail": userEmail
                })
                return 'here is sort link' + sort_link, 200
            else: return "Error: UserEmail or longURL is invalid",500

    except Exception as e:
        return dumps({'error': str(e)})


''' *********************** get long_URL *********************** '''
@app.route('/<sort_link>',methods = ['GET','POST'])
def get_link(sort_link):
    try:
        s_link1 = "http://localhost:5001/" + sort_link + "/"
        s_link2 = "http://localhost:5002/" + sort_link + "/"

        try:
            l_link = db.links.find_one({"SortLink": s_link1},{"LongLink": 1})
            print("this is long_link: {}".format(l_link["LongLink"]))

        except:
            l_link = db.links.find_one({"SortLink": s_link2}, {"LongLink": 1})
            print("this is long_link: {}".format(l_link["LongLink"]))

        return redirect(l_link["LongLink"], 302)

    except Exception as e:
        return dumps({'error': str(e)})



''' *************************************************************** '''
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


