# Expense tracker

- Fourth model of my expense tracker series
- This version stores data in MongoDB
- The idea of this project is to store data in a NoSQL database
- Implemented using FastAPI + MongoDB

## What this version does?

- Each version progressively introduces new features and improvements, showcasing the technologies and capabilities used throughout development.
- In this version, data is stored persistently using SQLite, ensuring that information is retained between program executions.
  - Add/edit your income and expenses
  - Get the total of your expenses/income
  - The program can analyse your expenses to know how much you do save/spend

## Steps

- Clone the project
- Create a virtual environment: python3 -m venv <venv name>
- Activate the environment: source <venv name>/bin/activate
- Install dependencies: pip install -r requirements.txt
- To run: fastapi run app.py --reload

## Database setup

- You must create you cluster instance in mongo atlas.
- In your root directory, create a .env file with the next credentials

```
DB_USER = Your mongodb user
DB_PSW = Your mongodb password
DB_URL= Your mongodb URL
```

## All versions

- [v6](https://github.com/giangarof/expenseTracker_v6): Extension of v4. Implements user authentication and verification
- [v5](https://github.com/giangarof/expenseTracker_v5): Extension of v3. Implements user authentication and verification
- [v4](https://github.com/giangarof/expenseTracker_v4): This version implements FastAPI along with NoSQL (MongoDB)
- [v3](https://github.com/giangarof/expenseTracker_v3): This version implements FastAPI along with SQL (SQLAlchemy)
- [v2](https://github.com/giangarof/expenseTracker_v2): This version implements FastAPI
- [V1](https://github.com/giangarof/expenseTracker_v1): This version implements vanilla python. Can be used through the terminal.

## Important note

- This version, and the upcoming FastAPI + mongoDB version, will use pipeline implementations.
  - A pipeline in MongoDB is a sequence of stages that documents pass through, one after another, to produce a final result.
  - MongoDB Aggregation is conceptually similar to SQL queries. Both allow you to filter, group, calculate, sort, and combine data.

- The routes that perform id lookup are stored as ObjectId in MongoDB. Keep in mind that plain id in string formart won't work
  - The solution is to convert plain string into ObjectId format
  - Same idea when retrieving a document from MongoDB, the `_id` needs to be converted in string so python can successfully retrieve the data.
