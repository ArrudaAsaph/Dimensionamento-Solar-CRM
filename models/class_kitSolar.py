import json

class KitSolar:
    def __init__(self, id, idItens, quantidade, valorKit):
        self.__id = id
        self.__idItens = idItens
        self.__quantidade = quantidade
        self.__valorKit = valorKit

    # Métodos sets
    def set_id(self, id):
        if id >= 0:
            self.__id = id
        else:
            raise ValueError("ID inválido, tente outro valor positivo")

    def set_idItens(self, idItens):
        if all(type(i) == int for i in idItens):
            self.__idItens = idItens
        else:
            raise ValueError("idItens deve ser uma lista de inteiros")

    def set_quantidade(self, quantidade):
        if quantidade >= 0:
            self.__quantidade = quantidade
        else:
            raise ValueError("Quantidade inválida, tente outro valor positivo")

    def set_valorKit(self, valorKit):
        if valorKit > 0:
            self.__valorKit = valorKit
        else:
            raise ValueError("valorKit inválido, tente outro valorKit positivo")

    # Métodos gets
    def get_id(self):
        return self.__id

    def get_idItens(self):
        return self.__idItens

    def get_quantidade(self):
        return self.__quantidade

    def get_valorKit(self):
        return self.__valorKit

    def __str__(self):
        return f"Id: {self.get_id()} - idItens: {self.get_idItens()} - quantidade: {self.get_quantidade()} - valorKit: R${self.get_valorKit()}"

    def to_dict(self):
        return {
            "id": self.get_id(),
            "idItens": self.get_idItens(),
            "quantidade": self.get_quantidade(),
            "valorKit": self.get_valorKit()
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data["id"],
            idItens=data["idItens"],
            quantidade=data["quantidade"],
            valorKit=data["valorKit"]
        )


class KitsSolar:
    arquivo_json = "admin/model/KitsSolares.json"
    lista_obj = []

    @classmethod
    def abrir(cls):
        try:
            with open(cls.arquivo_json, "r") as arquivo:
                arquivo_json = json.load(arquivo)
                cls.lista_obj = [KitSolar.from_dict(obj) for obj in arquivo_json]
        except FileNotFoundError:
            cls.lista_obj = []

    @classmethod
    def salvar(cls):
        with open(cls.arquivo_json, "w") as arquivo:
            json.dump([obj.to_dict() for obj in cls.lista_obj], arquivo, indent=4)

    @classmethod
    def inserir(cls, kitSolar):
        cls.lista_obj.append(kitSolar)
        cls.salvar()

    @classmethod
    def listar(cls):
        return cls.lista_obj

    @classmethod
    def listar_id(cls, id):
        for obj in cls.lista_obj:
            if obj.get_id() == id:
                return obj
        return None

    @classmethod
    def atualizar(cls, kitSolar):
        for i, obj in enumerate(cls.lista_obj):
            if obj.get_id() == kitSolar.get_id():
                cls.lista_obj[i] = kitSolar
                cls.salvar()
                return
        raise ValueError("KitSolar não encontrado para atualização")

    @classmethod
    def excluir(cls, kitSolar):
        for obj in cls.lista_obj:
            if obj.get_id() == kitSolar.get_id():
                cls.lista_obj.remove(obj)
                cls.salvar()
                return
        raise ValueError("KitSolar não encontrado para exclusão")


# Exemplo de uso
KitsSolar.abrir()
mostrar = KitsSolar.listar()
for i in mostrar:
    print(i)