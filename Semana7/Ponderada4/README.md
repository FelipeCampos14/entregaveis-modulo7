<h1>Ponderada 5</h1>

Para esse projeto utilizei fastapi e segui basicamente a documentação dele inteira(inclusive top1 documentações do planeta terra). Para estruturar o db foram feitos 3 arquivos python, sendo o o 'models' para configurar o db, 'schemes' para validar as operações de crud e entregar melhores feedbacks de erro e 'crud' para realizar, surpreendemente, operações de crud.

Há cinco rotas no backend, uma que serve de pagina principal, uma para logar, outra para levar para a pagina de criação de usuario, uma para criar o usuário de fato e a última para retornar a pagina de login.

Não consegui implementar JWT então fica por isso.

Quanto ao streamlit, basicamente reutilizei o codigo da api da ultima ponderada, utilizando o modelo ja pronto para prever os dados de acordo com o input do usuario.

O streamlit fica acessivel por meio de um iframe, um elemento HTML que permite rodar outra página html naquele espaço.

<h2>Como rodar</h2>

<h3>Local</h3>
Necessário rodar o streamlit primeiramente:

```
streamlit run streamlit/streamlit.py
```

Depois é só entrar na pasta src e rodar o main.py com uvicorn.
```
cd src
uvicorn main:app --reload
```

Finalmente é possivel criar um usuario e entra com ele. Já tem um usuário de teste com username 'teste' e senha 'admin123'.

<h3>AWS</h3>

Na implementação na AWS utilizei nginx para rodar o fastapi, porém tive problemas para rodar o streamlit. Até tentei criar duas instâncias para ver se conseguia rodar o streamlit em uma e o fastapi na outra mas não consegui, apesar de ter conseguido executar o arquivo. Em geral tentei mostrar o fluxo da aplicação evidenciando o que funcionou e o que não funcionou.

<video src="demo.mp4" width="640" height="360" controls>
  Your browser does not support the video tag.
</video>