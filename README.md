# Tech Blog
## Flask RESTful APP

### Server Details: 
- #### IP ADDRESS: 18.221.127.237
- #### SSH port: 2200 
- #### URL: http://ec2-18-221-127-237.us-east-2.compute.amazonaws.com/  #NOTE BELOW#
The url will display 404, because there is no content at the home page of the rest API, Add /categories at the end of the url and the categories will be displayed.
- for connecting use, the follwoing after correcting the location for /.ssh/
    ```bash
    ssh grader@18.221.127.237 -p 2200 -i ~/.ssh/awsServer
    ```


### Technologies:
1. Server Side
    - Python 3.6
    - Flask
    - Flask-RESTful
    - SQLLite3
    - Flask-SQLAlchemy
    - OAuth2
    - JWT
    - werkzeug.security (for hashing passwords).
    - AWS

1. Client Side
    - KnockOut.js
    - jQuery
    - Sass
    - Bootstrap4
    - Gulp
    - Babel
    - Font-Awesome

----
### Installation (CLIENT SIDE ONLY):
1. Install [Node](https://nodejs.org/en/)
1. Install Gulp CLI
    ```bash
    npm install gulp-cli -g
    npm install gulp -D
    ```
1. Clone this REPO
    ```bash
    git clone https://github.com/a-soliman/flask-blog-api.git
    ```
    ```bash
    cd python-restful-blog/
    ```


1. Install the requirments for CLIENT-SIDE
    1. From the root '/ ' Navigate to client/
    ```bash
    cd client/
    ```

    1. Run 'npm install' or 'npm i' to install the needed packages.
    ```bash
    npm install
    ```
----
### Running the client side code:
1. Navigate to client from the root '/ '
    ```bash
    cd client/
    ```

1. Run 'gulp server' to complile the application.

    ```bash
    gulp server
    ```

1. open your browser at port 3000 => [http://localhost:3000](http://localhost:3000)

----
### TESTING THE APP: EITHER USE THE BROWSER OR POSTMAN
1. BROWSER Root page: http://localhost:3000/ 
2. IF POSTMAN, PLEASE SEE END-POINTS BELOW 

----
# API END-POINTS:
## USER
- ### GET /users
- ### GET /user/<string:email>
- ### GET /user_id/<string:id>
- ### POST /user/register
- ### DEL /user/<string:email>
## POST
- ### GET /posts
- ### GET /post/<string:id>
- ### POST /post/add
- ### DEL /post/<string:id>

## Category
- ### GET /categories
- ### GET /category/<string:name>
- ### POST /category/<string:name>
- ### DEL /category/<string:name>

## Login & Authentication
- ### POST /login
- ### GET /auth

---
## SERVER CONFIGURATION SUMMERY:
- Updated and upgraded the software packages.
- Added a new User, with sudo access.
- Activated SSH login.
- Disabled remote login to root.
- Ativated the firewall for specific ports and services.
- Installed and configured Nginx.
- Hosted the SSh on a non-default port.
- Installed and configured POSTGRESQL database.
- Configured the webServer with uwsgi protocol.
- Install pip Virtualenv, and installed all the required packages within.

---

## THIRD PART RESOURCES USED TO COMPLETE THE PROJECT: 
- AWS Articles.
- Udacity Videos.
- YouTube Toturials.
- StackOverFlow Answers.
- various other courses.