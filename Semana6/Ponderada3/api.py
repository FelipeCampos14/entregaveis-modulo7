import pandas as pd
from sklearn import linear_model
from fastapi import FastAPI
import uvicorn
import joblib
from modelo import join_all, x

# Create the app
app = FastAPI()

# Load trained Pipeline
model = joblib.load("modelo.pkl")

# Prepara uma entrada para predição
data = pd.DataFrame([['10000000', '6275', '10000000', '5000000','United States','Games']])
data.columns = ['video_views_for_the_last_30_days','creation','subscribers','video views','Country','channel_type']
data[data['Country']] = 1
data[data['channel_type']] = 1

# Criação dos dataframe com os outros dados do one hot encoding
columns = list(set(join_all.columns) - set(data.columns))
zero_array = []
for i in range(len(columns)):
  zero_array.append(0)
data2 = pd.DataFrame([zero_array])
data2.columns = columns

# Join dos dois dataframes
data_prediction = data.join(data2)

# tirando o y e colunas do one-hot
columns_to_drop = ['Country','channel_type','rank']
data_prediction = data_prediction.drop(columns=columns_to_drop)
data_prediction = data_prediction[x.columns]

# Define predict function
@app.post("/predict")
def predict(data = data_prediction):
    predictions = model.predict(data)
    return predictions

# Define predict function
@app.get("/")
def ola_mundo():
    return "hello world"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
