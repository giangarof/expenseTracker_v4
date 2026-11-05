from typing import Annotated
from bson import ObjectId
from fastapi import Depends, FastAPI, APIRouter, HTTPException, status, Path
from database.database import expenses_collection, income_collection
from schema.models import ExpenseRequest
from utils import checkIfEmpty

router = APIRouter(prefix="/api/analysis", tags=["Analysis"])


# Method: GET
# route: /api/analysis/
# description: retrieve a report
@router.get("/", status_code=status.HTTP_200_OK)
def analysis():

    pipeline_expenses = [
        {"$group": {"_id": None, "total_expenses": {"$sum": "$ammount"}}}
    ]
    pipeline_incomes = [
        {"$group": {"_id": None, "total_incomes": {"$sum": "$ammount"}}}
    ]

    result_expenses = expenses_collection.aggregate(pipeline_expenses).to_list(length=1)
    result_income = income_collection.aggregate(pipeline_incomes).to_list(length=1)

    totalExpenses = result_expenses[0]["total_expenses"]
    totalIncomes = result_income[0]["total_incomes"]

    # remaining
    remaining = totalIncomes - totalExpenses

    # percentage used - income
    # percentage used = (total spent / total income) * 100
    percentage_used = (totalExpenses / totalIncomes) * 100

    # percentage remaining - income
    # percentage remaining = 100 - percentage used
    percentage_remaining = 100 - percentage_used

    return {
        "message": "your report",
        "data": {
            "total_expenses": totalExpenses,
            "total_income": totalIncomes,
            "remaining": remaining,
            "percentage_used": percentage_used,
            "percentage_remaining": percentage_remaining,
        },
    }
