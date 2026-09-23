from pydantic import BaseModel, Field

# Note:
# MongoDB generates the id
# No need to specify id in the request model


class ExpenseRequest(BaseModel):
    name: str = Field(min_length=2, max_length=25)
    ammount: int = Field(gt=0, lt=10000)
    model_config = {
        "json_schema_extra": {"example": {"name": "expense name", "ammount": 1}}
    }


class IncomeRequest(BaseModel):
    name: str = Field(min_length=2, max_length=25)
    ammount: int = Field(gt=0, lt=10000)
    model_config = {
        "json_schema_extra": {"example": {"name": "expense name", "ammount": 1}}
    }
