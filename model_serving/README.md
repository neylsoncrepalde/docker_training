# Implementando uma API para servir modelo de ML

Para executar o projeto, instale ou atualize `hermione-ml`

```
pip install -U hermione-ml
```

Abra um novo projeto implementado

```bash
hermione new a3docker -imp y
```

Entre no projeto, ative o virtualenv e instale as dependências

```bash
cd a3docker
conda activate a3docker_env
pip install -r requirements.txt
```

vá até a pasta src e execute o train para ter o modelo treinado

```bash
cd src
hermione train
```

Substitua o Dockerfile do projeto por este aqui do repositório e coloque os arquivos `app.py` e `request.py` na pasta `api`

Depois disso, faça o *build* da imagem com o novo Dockerfile. Lembre-se de estar na pasta correta, a pasta root do projeto

```bash
cd ~/a3docker
docker build -f src/Dockerfile -t modelapp:latest .
```

Depois de buildar a imagem, execute o container com

```bash
docker run -p 5000:5000 modelapp:latest
```

Agora, use o arquivo `request.py` para fazer uma chamada para a API do seu modelo! :)