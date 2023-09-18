# Documentação 

## Pipeline e Modelagem
Inicialemnte foi feito no Colab todo o processamento de dados e escolha do modelo uma vez que lá é possível utilizar o Pycaret. Portanto há dois notebooks, um com AutoML chamado Colab e outro utilizando a biblioteca scikit-learn, chamado vscode. Há também um arquivo vscode.py que serve apenas para poder exportar algumas variáveis do notebook para a api.

Ambos notebooks são praticamente iguais nas partes de pré-processamento, exploração dos dados e feature engineering. A pipeline que se seguiu foi basicamente de repor dados NaN por dado médios — mediana para valores contínuos e moda para dados categóricos, localizar e corrigir dados inconsistentes, remover colunas com baixa correlação com a variável target e colunas com alta correlação com a variável target, mas com alta correlação entre si.

Já em relação a parte de modelo, os dois notebooks se diferem. O notebook do colab, como dito antes, foi feito utilizando AutoML, obtendo diversos resultados com overfitting, com 0,999 de r2 score. Consequentemente, foi escolhido o primeiro algpritmo que não tivesse um grau de overfitting tão alto. Portanto o modelo usado foi de Lasso.

A coluna target selecionada foi 'rank', com o objetivo de inputar as informações do canal e descobrir em que lugar ele ficaria no ranking.

No notebook vscode.ipynb, utilzou-se o modelo previamente escolhido, utilizando a biblioteca scikit-learn. Além disso, o modelo de AutoML do Colab continha uma remoção de 5% dos outliers utilizando o modelo de Isolation Forest, que também foi replicado no notebook vscode. Também aplicou-se um teste de validação cruzada para testar se o algoritmo não estava com sobreajuste, o que não aparentou ter. Ao final o modelo é salvo em um arquivo pkl para ser usado pela API.

Em relação à API, é carregado o modelo e importadas algumas variáveis para contruir uma dataframe que possa ser lido pelo modelo. Essa informações são processadas na rota post 'predict', que pode ser acessada pelo endereço das aplicação + '/docs' na guia.

## Executando os containers
passo 1:
```
docker pull felipecampos14/ponderada3:latest
```

passo 2:
```
docker run 8080:80 felipecampos14/ponderada3:latest
```