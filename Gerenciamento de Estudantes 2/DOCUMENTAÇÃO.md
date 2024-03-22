# Sistema de Gerenciamento de Estudantes

Este é um sistema de gerenciamento de estudantes construído usando Django 4, HTML 5, CSS 3 e Bootstrap 5 com um tema Bootswatch.

![plot](https://github.com/BobsProgrammingAcademy/Student-Management-System/blob/master/students/static/images/homepage.png?raw=true)



### Pré-requisitos

Instale os seguintes pré-requisitos:

1. [Python 3.8-3.11](https://www.python.org/downloads/)
<br> Este projeto usa Django v4.2.4. Para o Django funcionar, você deve instalar uma versão correta do Python em sua máquina. Mais informações  [aqui](https://django.readthedocs.io/en/stable/faq/install.html).
2. [Visual Studio Code](https://code.visualstudio.com/download)


### Instalação

#### 1. Criar um ambiente virtual

A partir do diretório raiz, execute:


```bash
python -m venv venv
```

#### 2. Ativar o ambiente virtual

Ativar o ambiente virtual
No macOS:

```bash
source venv/bin/activate
```

No Windows:

```bash
venv\scripts\activate
```

#### 3. Instale os programas necessários para a produção

A partir do diretório raiz, execute:

```bash
pip install -r requirements.txt
```

#### 4. Executar as migrações

A partir do diretório raiz, execute:


```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```

#### 5. Criar um usuário administrador para acessar a interface de administração do Django

A partir do diretório raiz, execute:


```bash
python manage.py createsuperuser
```

Quando solicitado, informe um nome de usuário, email e senha.


### Executar a aplicação


A partir do diretório raiz, execute:


```bash
python manage.py runserver
```

### Visualizar a aplicação

Vá para http://127.0.0.1:8000/ para visualizar a aplicação.


### Copyright and License

Copyright © 2024 Universidade Para Todos. 
