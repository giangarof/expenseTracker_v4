import database.database
from fastapi import FastAPI
from routes import expensesRoutes, incomeRoute, analysisRoute

app = FastAPI()

app.include_router(expensesRoutes.router)
app.include_router(incomeRoute.router)
app.include_router(analysisRoute.router)
