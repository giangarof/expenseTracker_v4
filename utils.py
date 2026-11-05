from fastapi import HTTPException


def checkIfEmpty(data, msg):
    if not data:
        raise HTTPException(status_code=404, detail=msg)
