from model.livro import LivroModel

class LivroController:
    def __init__(self):
        self.model = LivroModel()

    def listar_livros(self):
        return self.model.listar_livros()