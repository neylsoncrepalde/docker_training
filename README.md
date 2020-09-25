# Docker Training

Prof. Dr. Neylson Crepalde

# Comandos Docker

Para verificar o status do seu ambiente docker,

```
docker info
```

Para buscar um termo nos repositórios de imagem

```
docker search redis
```

Para baixar uma imagem, 

```
docker pull rocker/shiny:latest
```

Veja as diversas imagens disponíveis no [Docker Hub](https://hub.docker.com)

Para listar as imagens que você possui

```
docker images
```

Para executar um container, use `docker run [OPTIONS] <IMAGE>:<TAG> [ARGS...]`.  Algumas opções mais usadas:

- `-i` executa de maneira interativa
- `--rm` deleta o container logo que sua execução for interrompida
- `-p` escolhe a porta utilizada pelo host e a porta exposta dentro do container
- `-e` define alguma variável de ambiente que será interpretada no container

Como exemplo, vamos executar um container rodando o shiny-server

```
docker run -i --rm -p 3838:3838 rocker/shiny-verse:latest
```

Vamos utilizar o ainda não lançado python 3.9 usando um container

```
docker pull python:3.9.0rc2-alpine3.12
docker run -it python:3.9.0rc2-alpine3.12
```

Para parar um container use `docker ps` para identificar os containers em execução e `docker stop <NOME_DO_CONTAINER>` para dar stop.

Para remover uma imagem, use `rmi`

```
docker rmi python:3.9.0rc2-alpine3.12
```

`docker tag` cria uma tag a partir de uma imagem existente:

```
docker pull python:3.8.5-slim-buster
docker tag python:3.8.5-slim-buster python:38deb
docker run -it python:38deb
```

`docker push` empurra a sua imagem para algum repositório. Normalmente é assim que levamos a nossa solução para ser executada em algum ambiente em nuvem.

# Trabalhando com um Dockerfile

Após escrever um `Dockerfile` funcional, construa a sua imagem com

```
docker build -t minhaimagem:versao .
```

Este comando procura por um arquivo chamado `Dockerfile` no diretório de trabalho. Podemos especificar um arquivo específico usando a flag `-f`

```
docker build -f meuDockerfile -t minhaimagem:versao .
```

O ponto no final do comando indica que a imagem será "buildada" a partir do diretório de trabalho atual. Este é o caso mais comum.

Agora vamos entender as partes de um Dockerfile

```Dockerfile
#Dockerfile
FROM ubuntu:latest

MAINTAINER "Neylson Crepalde"
LABEL squad=rubik

ENV MINHAVARAMBIENTE=neylson
ENV MINHAOUTRAVAR crepalde

WORKDIR /app

COPY files/ /app/files

RUN <COMANDOS_EM_GERAL>

EXPOSE 8080 # porta

CMD <Instrução padrão do container>

ENTRYPOINT <Comando a ser executado quando o container for iniciado>
```