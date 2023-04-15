## HOW TO TEST THE ASSIGNMENT

## STEP 1: SET UP VIRTUAL ENVIRONMENT
open this folder into vscode or any other editor
set up the virtual environment (eg: use "python3 -m venv server" in vs code), to name the virtual environment server
activate the virtual environment: source server/bin/activate (mac/linux)


## STEP 2: SET UP THE DATABASE
connect to mongodb database through connection string
paste the connection string in backend.py as parameter of MongoDBClient
make a collection in databse named as users

## STEP 3: RUN THE APPLICATION
run the command "python3 backend.py" in the terminal in the project directory


## STEP 4: TEST THE APPLICATION
Test the application in postman using this url "http://127.0.0.1:5000" with required
criteria's for post, get, edit and delete as shown in screenshot folder


