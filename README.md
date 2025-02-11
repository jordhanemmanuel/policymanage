# policymanage

### Executar o Projeto

Para executar o projeto, existem as seguintes formas:

- Docker
```sh
docker compose run capitalgains
```
- Input redirection:
```sh
docker compose run -T capitalgains < [diretorio]/input.txt
```

Caso estiver executando da pasta raíz do projeto onde o **docker-compose.yaml** está localizado, pode usar o arquivo com inputs padrões:
```sh
docker compose run -T capitalgains < input.txt
```

### Executar Testes

-Testes unitários
Para executar a suíte de testes unitários:
```sh
docker compose run capitalgains_test
```

-Testes de integração
Para executar a suíte de testes de integração:
```sh
docker compose run capitalgains_test_integration
```
