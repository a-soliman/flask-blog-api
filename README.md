# Tech Blog
## Flask RESTful APP

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

1. Client Side
    - KnockOut.js
    - jQuery
    - Sass
    - Bootstrap4
    - Gulp
    - Babel
    - Font-Awesome

----
### Installation:
1. Install [Python 3.6](https://www.python.org/downloads/)
1. Install [Node](https://nodejs.org/en/)
1. Install Gulp CLI
    ```bash
    npm install gulp-cli -g
    npm install gulp -D
    ```
1. Clone this REPO
    ```bash
    git clone https://github.com/a-soliman/python-restful-blog.git
    ```
    ```bash
    cd python-restful-blog/
    ```
1. Install and activate [Python virtualenv](https://virtualenv.pypa.io/en/stable/), (recomended).
1. Install the requirments for SERVER-SIDE
    ```bash
    pip install Flask==1.0.2
    pip install Flask-RESTful==0.3.6
    pip install Flask-JWT==0.3.2
    pip install Flask-SQLAlchemy==2.3.2
    pip install httplib2==0.11.3
    pip install oauth2client==4.1.2
    pip install requests==2.18.4
    pip install SQLAlchemy==1.2.7
    pip install datetime
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
### Run Application:
1. from the root '/ ' Navigate to server/
    ```bash
    cd server/
    ```
1. Run app.py
    ```bash
    python app.py
    ```
1. With the server runing, open a new bash terminal and navigate to client from the root '/ '
    ```bash
    cd client/
    ```

1. Run 'gulp server' to complile the application.

    ```bash
    npm start
    ```

1. open your browser at port 3000 => [http://localhost:3000](http://localhost:3000)

----
### Directions:
1. Root page: http://localhost:3000/ 
    - is where you can view the movies and run the trailers.

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