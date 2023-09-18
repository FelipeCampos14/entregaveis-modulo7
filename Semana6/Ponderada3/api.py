import pandas as pd
from sklearn import linear_model
from fastapi import FastAPI
import uvicorn
import joblib
from typing import List


join_all_columns = ['rank', 'subscribers', 'video views','video_views_for_the_last_30_days', 'creation', 'Afghanistan',
       'Andorra', 'Argentina', 'Australia', 'Bangladesh', 'Barbados', 'Brazil',
       'Canada', 'Chile', 'China', 'Colombia', 'Cuba', 'Ecuador', 'Egypt',
       'El Salvador', 'Finland', 'France', 'Germany', 'India', 'Indonesia',
       'Iraq', 'Italy', 'Japan', 'Jordan', 'Kuwait', 'Latvia', 'Malaysia',
       'Mexico', 'Morocco', 'Netherlands', 'Pakistan', 'Peru', 'Philippines',
       'Russia', 'Samoa', 'Saudi Arabia', 'Singapore', 'South Korea', 'Spain',
       'Sweden', 'Switzerland', 'Thailand', 'Turkey', 'Ukraine',
       'United Arab Emirates', 'United Kingdom', 'United States', 'Venezuela',
       'Vietnam', 'Animals', 'Autos', 'Comedy', 'Education', 'Entertainment',
       'Film', 'Games', 'Howto', 'Music', 'News', 'Nonprofit', 'People',
       'Sports', 'Tech']

x_columns = ['subscribers', 'video views','video_views_for_the_last_30_days', 'creation', 'Afghanistan',
       'Andorra', 'Argentina', 'Australia', 'Bangladesh', 'Barbados', 'Brazil',
       'Canada', 'Chile', 'China', 'Colombia', 'Cuba', 'Ecuador', 'Egypt',
       'El Salvador', 'Finland', 'France', 'Germany', 'India', 'Indonesia',
       'Iraq', 'Italy', 'Japan', 'Jordan', 'Kuwait', 'Latvia', 'Malaysia',
       'Mexico', 'Morocco', 'Netherlands', 'Pakistan', 'Peru', 'Philippines',
       'Russia', 'Samoa', 'Saudi Arabia', 'Singapore', 'South Korea', 'Spain',
       'Sweden', 'Switzerland', 'Thailand', 'Turkey', 'Ukraine',
       'United Arab Emirates', 'United Kingdom', 'United States', 'Venezuela',
       'Vietnam', 'Animals', 'Autos', 'Comedy', 'Education', 'Entertainment',
       'Film', 'Games', 'Howto', 'Music', 'News', 'Nonprofit', 'People',
       'Sports', 'Tech']

# Create the app
app = FastAPI()

# Load trained Pipeline
model = joblib.load("modelo.pkl")


# Define predict function
@app.get("/predict", response_model=List[float])
def predict():
    # Prepara uma entrada para predição
    data = pd.DataFrame([['10000000', '6175', '10000000', '5000000','United States','Games']])
    data_colunas = ['video_views_for_the_last_30_days','creation','subscribers','video views','Country','channel_type']
    data.columns = data_colunas
    data[data['Country']] = 1
    data[data['channel_type']] = 1

    # Criação dos dataframe com os outros dados do one hot encoding
    columns = list(set(join_all_columns) - set(data.columns))
    zero_array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    data2 = pd.DataFrame([zero_array])
    data2.columns = columns

    # Join dos dois dataframes
    data_prediction = data.join(data2)

    # tirando o y e colunas do one-hot
    columns_to_drop = ['Country','channel_type','rank']
    data_prediction = data_prediction.drop(columns=columns_to_drop)
    data_prediction = data_prediction[x_columns]
    predictions = model.predict(data_prediction)
    return predictions.tolist()

# Define predict function
@app.get("/")
def ola_mundo():
    return 'hi'

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
