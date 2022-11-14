import bentoml

from bentoml.io import JSON
#from bentoml.io import NumpyNdarray

from pydantic import BaseModel

#validation schema
class CreditApplication(BaseModel):
    seniority: int
    home: str
    time: int
    age: int
    marital: str
    records: str
    job: str
    expenses: int
    income: float
    assets: float
    debt: float
    amount: int
    price: int




model_ref = bentoml.xgboost.get("credit_risk_model:swwzc2cshozbnool")

dv = model_ref.custom_objects["dictVectorizer"]

model_runner = model_ref.to_runner()

svc = bentoml.Service("credit_risk_classifier", runners = [model_runner])

@svc.api(input=JSON(pydantic_model=CreditApplication), output=JSON())
async def classify(credit_application):
    application_data = credit_application.dict()
    vector = dv.transform(application_data)
    prediction = await model_runner.predict.async_run(vector)
    print(prediction)
    result = prediction[0]

    if result > 0.5:
        return {
            "status": "DECLINED"
        }
    elif result > 0.23:
        return {
            "status": "MAYBE"
        }
    else:
        return {
            "status": "APPROVED"
        }
