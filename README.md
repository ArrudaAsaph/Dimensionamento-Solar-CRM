# Dimensionamento-Solar-CRM

## Tecnologias
![Java](https://img.shields.io/badge/Java-ED8B00?style=flat&logo=openjdk&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)

## Descrição
O projeto Sistema de Dimensionamento Solar e CRM tem como objetivo fornecer uma solução eficiente, integrada e acessível para o dimensionamento de sistemas fotovoltaicos e a gestão do relacionamento com clientes.

## Entrar no Sistema como Administrador
- Compilar (Diretório -> Dimensionamento-Solar-CRM):
```
javac -d admin/model/bin -cp admin/model/lib/gson-2.11.0.jar admin/model/src/*.java
```

- Run (Diretório -> Dimensionamento-Solar-CRM):
```
java -cp admin/model/bin:admin/model/lib/gson-2.11.0.jar Main
```

## Entrar no Sistema como Usuário/Empresa
- Instalar a biblioteca do Python Streamlit na máquina:
```
pip install streamlit
```

- Run (View):
```
python -m user.view.View
```


- Run (Streamlit):
```
python -m streamlit run user/templates/Main.py
```


