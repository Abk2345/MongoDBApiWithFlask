## Api creation with Flask, with MongoDB as database

# Steps to set up
1. SET UP VIRTUAL ENVIRONMENT
    1. open this folder into vscode or any other editor
    2. set up the virtual environment (eg: use "python3 -m venv server" in vs code), to name the virtual environment server
    3. activate the virtual environment: source server/bin/activate (mac/linux)
2. SET UP THE DATABASE
    1. connect to mongodb database through connection string
    2. paste the connection string in backend.py as parameter of MongoDBClient
    3. make a collection in databse named as users
3. RUN THE APPLICATION
    1. run the command "python3 backend.py" in the terminal in the project directory
4. TEST THE APPLICATION
    1. Test the application in postman using this url "http://127.0.0.1:5000" with required
    2. criteria's for post, get, edit and delete as shown in screenshot folder


