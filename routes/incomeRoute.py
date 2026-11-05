from typing import Annotated
from bson import ObjectId
from fastapi import Depends, FastAPI, APIRouter, HTTPException, status, Path
from database.database import income_collection
from schema.models import IncomeRequest
from utils import checkIfEmpty

router = APIRouter(prefix="/api/income", tags=["Income"])


# Method: GET
# route: /api/income/
# description: fetch all expenses
@router.get("/", status_code=status.HTTP_200_OK)
def getAll():
    data = income_collection.find({}).to_list(length=None)

    # You can print(data)
    # print(data)

    # But you cannot return data
    # The reason is because _id is stored as a ObjectId data type:
    # Example: '_id': ObjectId('6ab33df7ce7193bb086c4d7e')

    # Meaning:
    # The problem is that Python's standard JSON encoder doesn't know how to serialize an ObjectId into JSON.

    # The solution
    # FastAPI needs to convert this ObjectId into JSON
    # The solution would be to convert ObjectId into string

    checkIfEmpty(data, "No incomes available...")

    # Manually conversion
    for x in data:
        x["_id"] = str(x["_id"])

    return {"message": "Found", "data": data}


# Method: GET
# route: /api/income/{id}
# description: fetch one income by id
@router.get("/{id}", status_code=status.HTTP_200_OK)
def getOneById(id: str):

    # Needs to conert the string into a ObjectId type
    data = income_collection.find_one({"_id": ObjectId(id)})

    checkIfEmpty(data, "No income id found...")

    data["_id"] = str(data["_id"])
    return {"message": "Found", "data": data}


# Method: POST
# route: /api/income/
# description: Add a new income
@router.post("/", status_code=status.HTTP_201_CREATED)
def addIncome(theIncome: IncomeRequest):
    # MongoDB generates the _id
    income_collection.insert_one(theIncome.model_dump())

    return {"message": "Income added successfully", "data": theIncome}


# Method: PUT
# route: /api/income/
# description: Update a income by id
@router.put("/{id}", status_code=status.HTTP_200_OK)
def updateById(theIncome: IncomeRequest, id: str):
    # check if exist
    data = income_collection.find_one({"_id": ObjectId(id)})

    checkIfEmpty(data, "Income id does not exist")

    income_collection.update_one(
        {"_id": ObjectId(id)}, {"$set": theIncome.model_dump()}
    )

    return {"message": "Income updated successfully", "data": theIncome}


# Method: DELETE
# route: /api/income/{id}
# description: Delete a income by id
@router.delete("/{id}")
def deleteById(id: str):
    # find if exist
    data = income_collection.find_one({"_id": ObjectId(id)})

    checkIfEmpty(data, "Income id does not exist")

    income_collection.delete_one({"_id": ObjectId(id)})
    return {"message": "Income deleted successfully"}
