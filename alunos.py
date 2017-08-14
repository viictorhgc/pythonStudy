#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Aluno:
    __doc__ = """
        Classe de estudo
    """
    # Todos os atributos são privados...
    __Nome = ''
    __Serie = 0
    __Notas = [0,0,0,0]

    def __init__(self, Nome, Serie):
        __doc__ = """
            Instancia da classe Aluno
            Parâmetros
            Nome: String com o nome do aluno
            Serie: Integer com a classe do aluno (1 a 9)
        """
        self.__Nome = Nome
        self.__Serie = Serie

    def pega_nome(self):
        __doc__ = """
            Esta função retorna uma string com o nome do aluno
        """
        return self.__Nome

    def define_nota(self, Semestre, Nota):
        __doc__ = """
            Esta função serve para definir uma nota para um aluno
            Parâmetros
            Semestre: Integer de 1 a 4
            Nota: Float de 0 a 10
        """
        self.__Notas[Semestre] = Nota

    def define_nome(self, Nome):
        __doc__ = """
            Função para "renomear" o aluno
        """
        self.__Nome = Nome

    def fecha_media(self):
        __doc__ = """
            Esta função função tira a média do aluno
            e returna um float
        """
        Notas = 0
        Media = 0
        i = 0
        while (i < 4):
            Notas += self.__Notas[i]
            i += 1
        Media = Notas / 4
        return Media

# Iniciando o programa
nome = str(raw_input("Nome do aluno: "))
serie = int(raw_input("Serie: "))
aluno = Aluno(nome, serie)
# A linha abaixo não vai alterar mais o nome do aluno
aluno.__Nome = "José Nascimento"
# Mas a linha abaixo altera
aluno.define_nome("João da Silva")
i = 0
while (i < 4):
    nota = float(raw_input("Digite a %sª nota: " % str(i+1)))
    aluno.define_nota(Semestre=i, Nota=nota)
    i += 1
print("O aluno %s terminou o ano com média %f" % (aluno.pega_nome(),aluno.fecha_media()))
