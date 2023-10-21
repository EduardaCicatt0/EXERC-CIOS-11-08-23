class Estudante:
    def __init__(self, nome): 
         
        """""
        # init é um construtor. Ele é chamado automaticamente quando criamos um 
        # novo objeto na classe. Que tem um parâmetro
        self.nome = nome

        """
class Turma:
    def __init__(self, nome) :
        self.nome = nome
        self.estudantes = []

    def adicionar_estudantes(self, estudantes):
        self.estudantes.append(estudantes)        


joao = Estudante("joaoh")
maria = Estudante("maria")

turmaA = Turma("Turma A")
turmaA.adicionar_estudantes(joao)
turmaA.adicionar_estudantes(maria)