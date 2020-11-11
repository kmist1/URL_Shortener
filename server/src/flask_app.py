import sys
import pymongo

from src import Models
from src.Models import User
from src.Models import Link
import string,random
from flask import Flask, request, redirect


connection = pymongo.MongoClient()
c_db = connection["users"]



sys.path.append('..')



app = Flask(__name__)



app.config['MONGODB_SETTINGS'] = {
    'host':'mongodb://localhost/users'
}

db = Models.db.intialize_db(app)

# @app.route('/user')
# def get_user():


''' *********************** Creating new user *********************** '''
@app.route('/users',methods=['POST'])
def post_user():
    """
    creating a new user, if user exists return error message else create user
    """
    body = request.get_json()
    user = User(**body).save()
    id = user.id
    return {'id':str(id)},200

''' *********************** Creating new sort_URL *********************** '''
@app.route('/links',methods = ['post'])
def post_link():
    """
    function to create new link
    """

    # create new link
    try:
        length = 6
        body = request.get_json()
        long_link = body["long_link"]
        user_email = body["user_email"]
        if (long_link):
            sort_link = "http://127.0.0.1:5000/" + ''.join(random.sample(string.ascii_letters + string.digits, length)) + "/"
            obj_dict = {
                "long_link":long_link,
                "sort_link":sort_link,
                "user_email":user_email
            }
            Link(**obj_dict).save()
            return "Link created, your sort_link: {}.".format(sort_link),200



    except:
        # Error while trying to create the resource
        # Add message for debugging purpose
        return "Error", 500

''' *********************** get long_URL *********************** '''

@app.route('/<sort_link>',methods = ['GET','POST'])
def get_link(sort_link):
    """
    function to get long link
    """

    # create new link
    try:

        s_link = "http://127.0.0.1:5000/"+sort_link+"/"
        l_link = c_db.link.find_one({"sort_link":s_link},{"long_link":1})
        print("this is long_link: {}".format(l_link["long_link"]))
        return redirect(l_link["long_link"],302)


    except:
        # Error while trying to create the resource
        # Add message for debugging purpose
        return "Error", 500



''' *************************************************************** '''
if __name__ == '__main__':
    app.run()

# length = 6
#
#     #body = request.get_json()
#     long_link = request.args.get("long_link")
#     user_email = request.args.get("user_email")
#     if (long_link):
#         #then create sort link
#         sort_link = "http://linkit/"+''.join(random.sample(string.ascii_letters+string.digits,length))+"/"
#         link = Link((long_link,sort_link,user_email)).save()
#         id = link.id
#         return {'id':str(id)},200
