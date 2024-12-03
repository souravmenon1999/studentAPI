
# Student API with FastAPI and MongoDB

this is a project that provide some endpoints that is build in Fast API to manage Student details using a backend

## Setup Instructions

### 1. Clone the repository
First, clone the repository to your local machine:

```bash
git clone https://github.com/souravmenon1999/studentAPI_Flask.git
cd studentAPI_Flask
```

### 2. Create and activate a virtual environment
To manage dependencies, create a virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install dependencies
Once the virtual environment is activated, install the required dependencies:

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
Create a `.env` file in the root directory of the project and add your MongoDB URI. Replace the placeholders with your actual MongoDB credentials.

```bash
MONGO_URI=mongodb+srv://<username>:<password>@cluster.mongodb.net/<database_name>
PORT=3600
```

### 5. Run the Application
You can start the FastAPI server by running:

```bash
python main.py
```

This will start the API at `http://localhost:3600`.

### 6. If you use  Docker then use the follwing command to run start the dockurized file.

```bash

docker build -t my-fastapi-app .

```

    then Once the image is built, you can run the container using the following command:
    make sure port number in .env file and internal port mentioned docker command should be same and I you can access the docurized server running on port 8080 and it will be mapped to internal port 3600

```bash 
docker run --env-file .env -p 8080:3600 my-fastapi-app

```




