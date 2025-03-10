# Dimensionamento-Solar-CRM

## Tecnologias
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Java](https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=openjdk&logoColor=white) 

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


