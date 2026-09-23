from typing import Annotated
from bson import ObjectId
from fastapi import Depends, FastAPI, APIRouter, HTTPException, status, Path
from database.database import income_collection
from schema.models import IncomeRequest

router = APIRouter(prefix="/api/income", tags=["Income"])


# Method: GET
# route: /api/income/
# description: fetch all expenses
@router.get("/")
def getAll():
    income = list(income_collection.find())

    if not income:
        return "nothing found"

    for x in income:
        x["_id"] = str(x["_id"])

    return income


# Method: GET
# route: /api/income/{id}
# description: fetch one income by id
@router.get("/{id}")
def getOneById(id: str):
    income = income_collection.find_one({"_id": ObjectId(id)})
    if not income:
        return "Nothing found"

    income["_id"] = str(income["_id"])
    return income


# Method: POST
# route: /api/income/
# description: Add a new income
@router.post("/")
def addIncome(theIncome: IncomeRequest):
    newincome = income_collection.insert_one(theIncome.model_dump())
    return "added"


# Method: PUT
# route: /api/income/
# description: Update a income by id
@router.put("/{id}")
def updateById(theIncome: IncomeRequest, id: str):
    # check if exist
    income = income_collection.find_one({"_id": ObjectId(id)})

    if income:
        income_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": theIncome.model_dump()}
        )

        return "updated successfully"

    return "nothing found"


# Method: DELETE
# route: /api/income/{id}
# description: Delete a income by id
@router.delete("/{id}")
def deleteById(id: str):
    # find if exist
    income = income_collection.find_one({"_id": ObjectId(id)})

    if income:
        income_collection.delete_one({"_id": ObjectId(id)})
        return "deleted successfully"

    return "it doesnt exist"
