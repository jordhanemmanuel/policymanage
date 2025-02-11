# policymanage

### Execute the project

To execute the project you need:

- Install dependences from requirements.txt
```sh
pip install -r requirements.txt
```
Note: If you're using linux, some distros need pip3 command.

- Run uvicorn
Inside **/app** FOLDER, run:
```sh
cd app
uvicorn main:app
```

-- Access swagger
After the server is up, access:
127.0.0.1:8000/docs