import json
import string,random
from pymongo import MongoClient
from flask import Flask, request, redirect
from flask_mail import Mail, Message
from bson.json_util import dumps
from validators.email_validator import isEmail_valid
from validators.url_validator import isURL_valid

#creating client connection to mongoDB instance running on local machine
client = MongoClient('mongodb://my_db:27017')
db = client.URL_SortenerDB

app = Flask(__name__)
mail = Mail(app)

# configuration of mail
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'url.shortner.unh@gmail.com'
app.config['MAIL_PASSWORD'] = '#qwerty12345'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)



''' *********************** FROM APP1 *********************** '''
@app.route('/')
def HelloUser():
    return 'Hello, you are using App1'




''' *********************** Creating new user *********************** '''
@app.route('/users',methods=['POST'])
def post_user():
    try:
        data = json.loads(request.data)
        firstName = data['FirstName']
        lastName = data['LastName']
        email = data['Email']

        '''creating a new user, if user exists return message that user already exists else create new user'''
        isUser = db.links.users({"Email": email})
        if isUser:
            return "User already exists",400
        else:
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
                else: return "Email is not valid",400

    except Exception as e:
        return dumps({'error': str(e)})




''' *********************** Creating new sort_URL *********************** '''
@app.route('/links',methods = ['post'])
def post_link():
    print('I am in links route')
    print('flag-1',json.loads(request.data))
    length = 6
    try:
        data = json.loads(request.data)
        print('flag-2',data);
        longLink = data['LongLink']
        userEmail = data['Email']
        print('flag-3',longLink,userEmail)

        '''creating a new sort_link, if longLink exists return message that link already exists else create new sortLink'''
        isURL = db.links.find_one({"LongLink": longLink})

        if isURL:
            return "URL already exists and converted to sort_url",400
        else:
            if longLink and userEmail:
                # do validation checks here
                isEmail = isEmail_valid(userEmail)
                isURL = isURL_valid(longLink)
                print(isEmail,isURL)
                if isEmail and isURL:
                    sort_link = "http://localhost:8080/" + ''.join(
                        random.sample(string.ascii_letters + string.digits, length))
                    db.links.insert_one({
                        "LongLink": longLink,
                        "SortLink": sort_link,
                        "UserEmail": userEmail
                    })
                    msg = Message(
                        'Hello',
                        sender='krunalmistry119@gmail.com',
                        recipients=[userEmail]
                    )
                    msg.body = 'You have successfully created your sort link: ' + sort_link
                    mail.send(msg)

                    return dumps({'sort_link':sort_link}), 200
                else: return "Error: UserEmail or longURL is invalid",400

    except Exception as e:
        return dumps({'error': str(e)})


''' *********************** get long_URL *********************** '''
@app.route('/<sort_link>',methods = ['GET','POST'])
def get_link(sort_link):
    try:
        s_link1 = "http://localhost:8080/" + sort_link
        l_link = db.links.find_one({"SortLink": s_link1},{"LongLink": 1})

        return redirect(l_link["LongLink"], 302)

    except Exception as e:
        return dumps({'error': str(e)})



''' *************************************************************** '''
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


