from typing import Annotated
from bson import ObjectId
from fastapi import Depends, FastAPI, APIRouter, HTTPException, status, Path
from database.database import expenses_collection
from schema.models import ExpenseRequest

router = APIRouter(prefix="/api/expenses", tags=["Expenses"])


# Method: GET
# route: /api/expenses/
# description: fetch all expenses
@router.get("/")
def getAll():
    expenses = list(expenses_collection.find())

    if not expenses:
        return "No expenses, add some"

    for x in expenses:
        x["_id"] = str(x["_id"])

    return expenses


# Method: GET
# route: /api/expenses/{id}
# description: fetch one by id
@router.get("/{id}")
def getOneById(id: str):
    expense = expenses_collection.find_one({"_id": ObjectId(id)})
    expense["_id"] = str(expense["_id"])

    return expense


# Method: POST
# route: /api/expenses/
# description: add a new expenses
@router.post("/")
def addExpense(theExpense: ExpenseRequest):
    newExpense = expenses_collection.insert_one(theExpense.model_dump())

    return "added"

    # to check the properties of newExpense
    # dir(newExpense)


# Method: PUT
# route: /api/expenses/{id}
# description: Update expense by id
@router.put("/{id}")
def updateById(theExpense: ExpenseRequest, id: str):
    # find if exist
    expense = expenses_collection.find_one({"_id": ObjectId(id)})

    if expense:
        expenses_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": theExpense.model_dump()}
        )

        return "updated successfully"

    return "it doesnt exist"


# Method: DELETE
# route: /api/expenses/{id}
# description: Delete expense by id
@router.delete("/{id}")
def deleteExpense(id: str):
    # find if exist
    expense = expenses_collection.find_one({"_id": ObjectId(id)})

    if expense:
        expenses_collection.delete_one({"_id": ObjectId(id)})
        return "deleted successfully"

    return "it doesnt exist"
