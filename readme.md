# Expense tracker V4

- This version uses FastAPI along with mongodb
- This version (V4) is the same as V3. Only difference is that insead of using a SQL approach, it does use NoSQL to store data

# Steps

## First

Clone the project
Create a virtual environment python3 -m venv
Activate the environment: source /bin/activate
Install dependencies pip install -r requirements.txt
To run: fastapi run main.py --reload

## Second

- In your root directory, create a .env file with the next credentials

```
DB_USER = Your mongodb user
DB_PSW = Your mongodb password
DB_URL= Your mongosb URL
```

# Previous models

- [v3](https://github.com/giangarof/expenseTrackerFastAPI_sql): This version implements FastAPI along with SQL (SQLAlchemy)
- [v2](https://github.com/giangarof/expenseTrackerFastAPI): This version implements FastAPI
- [V1](https://github.com/giangarof/expenseTrackerTerminalPython): This version implements vanilla python. Can be used through the terminal.
