# gerenciador-contatos


## Clonando o projeto e executando

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
 git clone https://github.com/sillaslima/gerenciador-contatos
 cd gerenciador-contatos
 python3 -m venv .venv
 source .venv/bin/activate
 pip install -r requirements.txt`****`
 python manage.py migrate
 python manage.py runserver
 
 
 Executando o app do Admin:
 http://localhost:8000/admin/
 
 Username:
 admin
 Password:
 admin@123
 
 
Urls API: 
api/contato/list
api/contato/update/<int:pk>
api/contato/detail/<int:pk>
api/contato/create/
api/contato/delete/<int:pk> 

 
 Link da APP http://localhost:8000/admin/gerirContatos/

Rodando os testes.
npm install -g newman
newman run Contato.postman_collection.json
 
 
```

