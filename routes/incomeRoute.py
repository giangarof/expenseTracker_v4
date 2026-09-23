from typing import Annotated
from bson import ObjectId
from fastapi import Depends, FastAPI, APIRouter, HTTPException, status, Path
from database.database import income_collection
from schema.models import IncomeRequest

router = APIRouter(prefix="/api/income", tags=["Income"])


# Method: GET
# route: /api/income/
# description: fetch all expenses
@router.get("/", status_code=status.HTTP_200_OK)
def getAll():
    data = list(income_collection.find())

    if not data:
        raise HTTPException(status_code=400, detail="No data available")

    for x in data:
        x["_id"] = str(x["_id"])

    return {"message": "Found", "data": data}


# Method: GET
# route: /api/income/{id}
# description: fetch one income by id
@router.get("/{id}", status_code=status.HTTP_200_OK)
def getOneById(id: str):
    data = income_collection.find_one({"_id": ObjectId(id)})
    if not data:
        raise HTTPException(status_code=400, detail="Id doesnt exist")

    data["_id"] = str(data["_id"])
    return {"message": "Found", "data": data}


# Method: POST
# route: /api/income/
# description: Add a new income
@router.post("/", status_code=status.HTTP_201_CREATED)
def addIncome(theIncome: IncomeRequest):
    income_collection.insert_one(theIncome.model_dump())

    return {"message": "Income added successfully", "data": theIncome}


# Method: PUT
# route: /api/income/
# description: Update a income by id
@router.put("/{id}", status_code=status.HTTP_200_OK)
def updateById(theIncome: IncomeRequest, id: str):
    # check if exist
    data = income_collection.find_one({"_id": ObjectId(id)})

    if data:
        income_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": theIncome.model_dump()}
        )

        return {"message": "Income updated successfully", "data": theIncome}

    raise HTTPException(status_code=400, detail="Id doesnt exist")


# Method: DELETE
# route: /api/income/{id}
# description: Delete a income by id
@router.delete("/{id}")
def deleteById(id: str):
    # find if exist
    data = income_collection.find_one({"_id": ObjectId(id)})

    if data:
        income_collection.delete_one({"_id": ObjectId(id)})
        return {"message": "Income deleted successfully"}

    raise HTTPException(status_code=400, detail="Id doesnt exist")
