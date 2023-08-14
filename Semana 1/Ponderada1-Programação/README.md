# PONDERADA DE PROGRAMAÇÃO

## Tutorial de uso 

Para rodar o projeto é necessário primeiramente fazer um docker pull

```
docker pull felipecampos/ponderada1:1.0
```

Após isso verifica-se se a imagem foi puxada com um:

```
docker images
```

Caso a Imagem esteja lá, agora pode-se rodar ela, com o seguinte comando:

```
docker run -p 80:3000 felipecampos14/ponderada1:1.0
```
e pronto!

## Faça Você Mesmo

É isso mesmo que você leu, você professor vai aprender a fazer o que você nos ensinou a fazer!!!

Passo 1: Crie uma pasta e crie um ambiente virtual dentro dela;

```
python -m venv . 
```

Passo 2: Ative sua venv - **OBS:** se não rodar no powershell, roda no command prompt;

```
activate
```

Passo 4: Crie um arquivo python e crie um endpoint para rodar sua aplicação;

Passo 5: Crie um requirements;

```
pip freeze > requirements.txt
```

Passo 6: Crie um dockerfile para rodar seu docker -- **Cuidado:** As configurações mudam dependendo do framework web que você usa;

Passo 7: Cria uma imagem com:

```
docker build --tag [NOME DA IMAGEM] . 
```

Passo 8: Pegue o ID da sua imagem

```
docker image
```

Passo 9: Rode sua imagem com

```
docker run -p 80:5000 [ID DA IMAGEM]
```

### Extra - Subir no dockerhub

Passo 10: Cria uma conta no docker hub

Passo 11: Crie um repositório público 

Passo 12: Logue na sua máquina com sua conta do dockerhub

```
docker login
```

Passo 13: Tague seu repositório na máquina local:

```
docker tag [NOME DA IMAGEM]:[VERSÃO] [NOME DO REPOSITORIO]:[VERSÃO]
```

Passo 14: De Push para o dockerhub;

```
docker push [NOME DO USUARIO]/[NOME DO REPOSITORIO]:[VERSÃO]
```
