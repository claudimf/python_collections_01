# Python Collections parte 1: Listas e tuplas

👋 Olá, Seja Bem-vindo(a) ao 'Python Collections parte 1: Listas e tuplas'.

# Projeto ['Python Collections parte 1: Listas e tuplas'](https://cursos.alura.com.br/course/python-collections-listas-e-tuplas):

### Aulas

<details>
    <summary>Listas e operações</summary>
    <ul>
        <li>Introdução</li>
        <li>Introdução as coleções e lista</li>
        <li>Mais operações em listas e list comprehension</li>
        <li>Problemas da mutabilidade da lista</li>
        <li>Removendo dados duplicados</li>
        <li>Faça como eu fiz na aula</li>
        <li>O que aprendemos?</li>
    </ul>
</details>

<details>
    <summary>Tuplas</summary>
    <ul>
        <li>Projeto da aula anterior</li>
        <li>Listas com objetos de classes nossas</li>
        <li>Tuplas, objetos e anemia</li>
        <li>Tupla de objetos e lista de tuplas</li>
        <li>Diferenciando tupla e lista</li>
        <li>Faça como eu fiz na aula</li>
        <li>O que aprendemos?</li>
    </ul>
</details>

<details>
    <summary>Polimorfismo e arrays</summary>
    <ul>
        <li>Projeto da aula anterior</li>
        <li>Listas e polimorfismo</li>
        <li>Arrays e Numpy</li>
        <li>Método abstrato</li>
        <li>Criação do array</li>
        <li>Faça como eu fiz na aula</li>
        <li>O que aprendemos?</li>
    </ul>
</details>

<details>
    <summary>Igualdade</summary>
    <ul>
        <li>Projeto da aula anterior</li>
        <li>Igualdade e o __eq__</li>
        <li>Igualdade</li>
        <li>Faça como eu fiz na aula</li>
        <li>O que aprendemos?</li>
    </ul>
</details>

<details>
    <summary>Outros builtins</summary>
    <ul>
        <li>Projeto da aula anterior</li>
        <li>Builtins como enumerated, range e desempacotamento automatico de tuplas</li>
        <li>Numerando</li>
        <li>Faça como eu fiz na aula</li>
        <li>O que aprendemos?</li>
    </ul>
</details>

<details>
    <summary>Ordem natural</summary>
    <ul>
        <li>Projeto da aula anterior</li>
        <li>Ordenação básica</li>
        <li>Organizando a lista</li>
        <li>Faça como eu fiz na aula</li>
        <li>O que aprendemos?</li>
    </ul>
</details>

<details>
    <summary>Ordenação customizada</summary>
    <ul>
        <li>Projeto da aula anterior</li>
        <li>Ordenação de objetos sem ordem natural</li>
        <li>Implementando o __lt__</li>
        <li>Boas práticas</li>
        <li>Faça como eu fiz na aula</li>
        <li>O que aprendemos?</li>
    </ul>
</details>

<details>
    <summary>Ordenação total</summary>
    <ul>
        <li>Projeto da aula anterior</li>
        <li>Ordenação completa e functools</li>
        <li>Conclusão</li>
        <li>Única escolha sobre o conteúdo da aula</li>
        <li>Faça como eu fiz na aula</li>
        <li>Projeto final</li>
        <li>O que aprendemos?</li>
    </ul>
</details>

# Notas das aulas:

Para executar um script python, faça conforme o exemplo abaixo:
```sh
docker-compose run --rm app python aulas/01.py
```

## Sobre o projeto:

### Permissões de arquivos:

Ao se criar migrações, adicionar libs ou qualquer outro comando que crie arquivos dentro do contâiner Docker o proprietário para edição se torna o contâiner, sendo assim você precisará rodar o comando abaixo para alterar essas permissões e você poder editar:

```sh
sudo chown -R $USER:$USER .
```

# Exigências

**:warning: Atenção:** É necessário que os desenvolvedores usem o Docker no seu ambiente de desenvolvimento.

- **🛠 Modo Desenvolvimento Docker**
    - :computer: [Linux Ubuntu LTS](https://ubuntu.com/download/desktop)
    - 🐳 [Docker](https://docs.docker.com/engine/installation/) Deve estar instalado.
    - 🐳 [Docker Compose](https://docs.docker.com/compose/) Deve estar instalado.
    - **💡 Dica:** [Documentação do Docker](https://docs.docker.com/)

# Instalando

## 🐳 Modo Desenvolvimento com Docker

Após instalar o docker e docker-compose, estando na pasta raiz do projeto, execute:

```sh
docker-compose up
```

Para se certificar que os seus containers subiram corretamente, todos os containers deve estar com o status `UP`, execute:

```sh
docker-compose ps -a
```

Para acessar o container da aplicação, execute:

```sh
docker-compose run --rm app bash
```

Para derrubar e subir a instância do docker novamente, execute:

```sh
docker-compose down && docker-compose up
```

# Referências utilizadas

[1° Conteinerização de scripts em Python](https://github.com/claudimf/containerized_python)

[2° Data Structures](https://docs.python.org/3/tutorial/datastructures.html)

[3° Enumerate](https://docs.python.org/3/library/functions.html#enumerate)