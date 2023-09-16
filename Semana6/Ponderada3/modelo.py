import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.ensemble import IsolationForest
from sklearn.metrics import r2_score
from datetime import date, datetime
from sklearn.model_selection import cross_val_score
import joblib

# pegando o dataset e subindo no notebook
df = pd.read_csv('Global YouTube Statistics.csv', encoding='unicode_escape')

# Transformando os dados de data em datetime e depois usando a diferença entre a data de criação e o dia de hoje
df['created_month'] = df['created_month'].replace({'Jan':1,
                                                  'Feb':2,
                                                  'Mar':3,
                                                  'Apr':4,
                                                  'May':5,
                                                  'Jun':6,
                                                  'Jul':7,
                                                  'Aug':8,
                                                  'Sep':9,
                                                  'Oct':10,
                                                  'Nov':11,
                                                  'Dec':12})
df = df.sort_values(by=['created_year','created_month','created_date'])

df['created_year'] = df['created_year'].fillna(method='ffill')
df['created_month'] = df['created_month'].fillna(method='ffill')
df['created_date'] = df['created_date'].fillna(method='ffill')

year = df['created_year']
month = df['created_month']
date = df['created_date']

lista = list()
dici = dict()
for i,j,k in zip(date,month,year):
  dia = pd.to_datetime(f'{int(i)}/{int(j)}/{int(k)}', format='%d/%m/%Y')
  dici['creation'] = int((datetime.now() - dia).days)
  lista.append(dici.copy())

data = pd.DataFrame(lista)

# join do dataframe de data feito
df = df.join(data)

# removendo as colunas de data nao mais necessárias de data
df = df.drop(columns={'created_year','created_month','created_date'})

# Substituindo valores incoerentes(como uploads em zero ou lucro = 0, mesmo não sendo um canal Nonprofit) e aplicando valores médios(mediana) no lugar de NaN
df['uploads'] = df['uploads'].replace({0:df['uploads'].median()})

colunas_incoerentes = ['lowest_monthly_earnings','highest_monthly_earnings','lowest_yearly_earnings','highest_yearly_earnings','video_views_for_the_last_30_days','subscribers_for_last_30_days']
for i in colunas_incoerentes:
  df[i] = df[i].loc[(df['channel_type'] != 'Nonprofit')].replace({0:df[i].median()})
  df[i] = df[i].fillna(df[i].median())

# Substituindo dados NaN categóricos por valores médios(moda)
df['Country'] = df['Country'].fillna(df['Country'].mode()[0])
df['channel_type'] = df['channel_type'].fillna(df['channel_type'].mode()[0])

# dropando colunas com alta correlação
pre_modelo = df.drop(columns={'country_rank','channel_type_rank','highest_monthly_earnings','lowest_monthly_earnings','lowest_yearly_earnings','highest_yearly_earnings','subscribers_for_last_30_days'})

# drop de colunas desnecessárias
modelo = pre_modelo.drop(columns={'Youtuber','Longitude','Latitude','Population','Unemployment rate','Urban_population','Gross tertiary education enrollment (%)','Title','Abbreviation','category','uploads','video_views_rank'})

## Modelo
# aplicando one-hot enconding
pais = pd.get_dummies(modelo.Country)
cat = pd.get_dummies(modelo.channel_type)
join_all = modelo.join([pais,cat])
join_all = join_all.drop(columns={'Country','channel_type'})

# Isolation Forest para achar outliers
model=IsolationForest(n_estimators=50, max_samples='auto', contamination=float(0.05),max_features=1.0)
model.fit(join_all)
# marcando os outliers
join_all['anomaly']=model.predict(join_all)
outliers = join_all['anomaly'].loc[join_all['anomaly'] == -1]

# removendo os outliers com threshold de 5%
join_all = join_all.drop(columns={'anomaly'})
join_all.drop(outliers.index)

# divide a coluna target das features
y = join_all['rank']
x = join_all.drop(columns={y.name})

# separa em treino e teste
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

# treinando o modelo
clf = linear_model.Lasso(alpha=0.1)
clf.fit(X_train, y_train)

# testa se está com overfitting
scores = cross_val_score(clf, x, y, cv=5)

# faz a predição
y_pred = clf.predict(X_test)

# teste de r2 para testar a acurácia
r2 = r2_score(y_test, y_pred)

# sobe o modelo para os arquivos
joblib.dump(clf, 'modelo.pkl')