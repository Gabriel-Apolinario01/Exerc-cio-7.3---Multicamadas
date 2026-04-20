class Livro:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


class LivroModel:
    def __init__(self):
        self.livros = [
            Livro("Python", 50),
            Livro("Engenharia", 70),
            Livro("Morro", 50)
        ]

    def listar_livros(self):
        return self.livros