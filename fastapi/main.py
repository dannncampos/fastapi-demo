"""FastAPI Entrypoint"""
import uvicorn
from fastapi import FastAPI, HTTPException

import houses


app = FastAPI()

ID = {"01": {"teste"}} # Connect to DB looking for process


@app.get("/process/{id}")
async def read_process(id: str):
    """Get process ID from BD

    Args:
        id (str): The ID of the searching

    Raises:
        HTTPException: An exception ocurred. Something went wrong!

    Returns:
        dict: The JSON dict with the search details
    """
    if id not in ID:
        raise HTTPException(
            status_code=404,
            detail="Process ID not found"
            )
    return {"process": ID[id]}


@app.get("/enumexample")
async def enum_async_example(number_of_results: int):
    """ Enumerable asyncronous example

    Returns:
        enum: Houses for sale
    """
    return houses.houses_on_sale(number_of_results)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)