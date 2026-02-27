

from fastapi import FastAPI
 


app = FastAPI()

@app.route("/health", methods=["GET"])
def health_check_init():
    return  {'status':'200'}