from flask import Flask,render_template,url_for,request,redirect
import csv
#we import render_template bcz dure to this we can use html file css file and js file also
app = Flask(__name__)  #we make a object or instance of flask class
print(__name__)

@app.route('/') 
def my_home():
    return render_template('index.html')


# @app.route('/works.html') 
# def works():
#     return render_template('works.html')

# @app.route('/work.html') 
# def work():
#     return render_template('work.html')    

# #1st for name ,2nd for int value ,3rd for string
# @app.route('/<username>/<int:post_id>/<path:subpath>')   #it gives us some extra tools for us to build a server
# #any time we hit '/' we define a func. which hello_world in our case and return from this function
# def hello_world(username=None,post_id=None,subpath=None):
#     return render_template('index_old.html',name=username,post_id=post_id,path=subpath)  #we only pass string but flask convert it into a html file as we see in developer tools


# #Note -> if debuger is off and we change Hello bro to hellooo then we have to run again our flask run command to get changes
# # but if debugger is on and we make a change then it handle it and make changes and we dont need to run our flask run command

# @app.route('/blog') 
# def my_blog():
#     return 'hey its my first blog!!'

# @app.route('/about.html') 
# def about():
#     return render_template('about.html') #it tries to look for file into a folder templates so we have to make it

# @app.route('/contact.html') 
# def contact():
#     return render_template('contact.html')

# @app.route('/about2.html') 
# def myfile2():
#     return render_template('file2.html')

# #for css and js file we have to make a new folder named static

#we can use string bcz not want to repeat myself by writing @app.route and function
@app.route('/<string:page_name>') 
def html_file(page_name):
    return render_template(page_name)

#we dont need components so we remove components line from every html file

def write_to_file(data):
    with open('database.txt',mode='a') as database:
        email= data["email"]
        subject= data["subject"]
        message= data["message"]
        file= database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv',newline='',mode='a') as database2:
        email= data["email"]
        subject= data["subject"]
        message= data["message"]
        csv_writer=csv.writer(database2, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

#for contact part
@app.route('/submit_form',methods = ['POST','GET']) 
def submit_form():
    if request.method=='POST':
        try:
            data=request.form.to_dict()  #give my contact data fill by user in a dict
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'data not saved'
    else :
        return 'something went wrong. Try again.'