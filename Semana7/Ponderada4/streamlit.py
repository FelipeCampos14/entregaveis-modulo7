import pandas as pd
import streamlit as st
import joblib
from datetime import datetime, date


model = joblib.load("modelo.pkl")
st.title('Ponderada 4')
video_views_for_the_last_30_days = st.number_input("Quantidade de views nos ultimos 30 dias")
creation_date = st.date_input("Data de criação")
subscribers = st.number_input("Quantidade de inscritos totais")
video_views = st.number_input("Quantidade de views totais")
country = st.selectbox(
    'País do canal',
    ('Afghanistan','Andorra', 'Argentina', 'Australia', 'Bangladesh', 'Barbados', 'Brazil',
       'Canada', 'Chile', 'China', 'Colombia', 'Cuba', 'Ecuador', 'Egypt',
       'El Salvador', 'Finland', 'France', 'Germany', 'India', 'Indonesia',
       'Iraq', 'Italy', 'Japan', 'Jordan', 'Kuwait', 'Latvia', 'Malaysia',
       'Mexico', 'Morocco', 'Netherlands', 'Pakistan', 'Peru', 'Philippines',
       'Russia', 'Samoa', 'Saudi Arabia', 'Singapore', 'South Korea', 'Spain',
       'Sweden', 'Switzerland', 'Thailand', 'Turkey', 'Ukraine',
       'United Arab Emirates', 'United Kingdom', 'United States', 'Venezuela',
       'Vietnam'))
channel_type = st.selectbox(
    'Tipo do canal',
    ('Animals', 'Autos', 'Comedy', 'Education', 'Entertainment',
       'Film', 'Games', 'Howto', 'Music', 'News', 'Nonprofit', 'People',
       'Sports', 'Tech'))

creation = int((datetime.date(datetime.now()) - creation_date).days)


data_colunas = ['video_views_for_the_last_30_days','creation','subscribers','video views','Country','channel_type']
data = pd.DataFrame([[video_views_for_the_last_30_days, creation, subscribers, video_views, country, channel_type]])
data.columns = data_colunas
visual_data = data
df = data
st.write(visual_data)

df['subscribers'] = subscribers*(-1)
df['video views'] = video_views*(-1)


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

df[df['Country']] = 1
df[df['channel_type']] = 1

# Criação dos dataframe com os outros dados do one hot encoding
columns = list(set(join_all_columns) - set(df.columns))
zero_array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
data2 = pd.DataFrame([zero_array])
data2.columns = columns

# Join dos dois dataframes
data_prediction = df.join(data2)

# tirando o y e colunas do one-hot
columns_to_drop = ['Country','channel_type','rank']
data_prediction = data_prediction.drop(columns=columns_to_drop)
data_prediction = data_prediction[x_columns]
predictions = model.predict(data_prediction)
if predictions < 1:
    predictions = 1
st.write('Posição no ranking    : ',int(predictions))