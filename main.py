import database.database
from fastapi import FastAPI
from routes import expensesRoutes, incomeRoute

app = FastAPI()

app.include_router(expensesRoutes.router)
app.include_router(incomeRoute.router)
