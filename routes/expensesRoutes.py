from typing import Annotated
from bson import ObjectId
from fastapi import Depends, FastAPI, APIRouter, HTTPException, status, Path
from database.database import expenses_collection
from schema.models import ExpenseRequest

router = APIRouter(prefix="/api/expenses", tags=["Expenses"])


# Method: GET
# route: /api/expenses/
# description: fetch all expenses
@router.get("/", status_code=status.HTTP_200_OK)
def getAll():
    data = list(expenses_collection.find())

    if not data:
        raise HTTPException(status_code=404, detail="No expenses, add some")

    for x in data:
        x["_id"] = str(x["_id"])

    return {"message": "Found", "data": data}


# Method: GET
# route: /api/expenses/{id}
# description: fetch one by id
@router.get("/{id}", status_code=status.HTTP_200_OK)
def getOneById(id: str):
    data = expenses_collection.find_one({"_id": ObjectId(id)})
    if not data:
        raise HTTPException(status_code=404, detail="Id doesnt exist")

    data["_id"] = str(data["_id"])

    return {"message": "Found", "data": data}


# Method: POST
# route: /api/expenses/
# description: add a new expenses
@router.post("/", status_code=status.HTTP_201_CREATED)
def addExpense(theExpense: ExpenseRequest):

    # Pydantic handles validation
    # if not theExpense:
    #     raise HTTPException(status_code=404, detail="error while adding new expense")

    expenses_collection.insert_one(theExpense.model_dump())

    return {"message": "Expense added successfully", "data": theExpense}

    # to check the properties of newExpense
    # dir(newExpense)


# Method: PUT
# route: /api/expenses/{id}
# description: Update expense by id
@router.put("/{id}", status_code=status.HTTP_200_OK)
def updateById(theExpense: ExpenseRequest, id: str):
    # find if exist
    data = expenses_collection.find_one({"_id": ObjectId(id)})

    if data:
        expenses_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": theExpense.model_dump()}
        )

        return {"message": "Expense updated successfully", "data": theExpense}

    raise HTTPException(status_code=404, detail="Unable to update")


# Method: DELETE
# route: /api/expenses/{id}
# description: Delete expense by id
@router.delete("/{id}", status_code=status.HTTP_200_OK)
def deleteExpense(id: str):
    # find if exist
    data = expenses_collection.find_one({"_id": ObjectId(id)})

    if data:
        expenses_collection.delete_one({"_id": ObjectId(id)})
        return {"message": "Deleted successfully"}

    raise HTTPException(status_code=404, detail="Id doesnt exist")
