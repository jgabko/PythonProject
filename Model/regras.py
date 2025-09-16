# FlaskDD/model/regras.py
import random

def rolar_dado(lados=6, qtd=1):
    """Rola uma quantidade específica de dados e retorna uma lista com os resultados."""
    return [random.randint(1, lados) for _ in range(qtd)]

def gerar_atributos_classico():
    """Gera 6 atributos rolando 3d6 para cada um."""
    atributos = {}
    nomes = ["Força", "Destreza", "Constituição", "Inteligência", "Sabedoria", "Carisma"]
    for nome in nomes:
        rolagem = rolar_dado(lados=6, qtd=3)
        atributos[nome] = sum(rolagem)
    return atributos

def gerar_atributos_heroico():
    """Gera 6 atributos rolando 4d6 e descartando o menor resultado."""
    atributos = {}
    nomes = ["Força", "Destreza", "Constituição", "Inteligência", "Sabedoria", "Carisma"]
    for nome in nomes:
        rolagem = rolar_dado(lados=6, qtd=4)
        rolagem.sort()
        atributos[nome] = sum(rolagem[1:]) # Soma os 3 maiores
    return atributos

def gerar_atributos_aventureiro():
    """Gera 6 atributos rolando 2d6+6 para cada um."""
    atributos = {}
    nomes = ["Força", "Destreza", "Constituição", "Inteligência", "Sabedoria", "Carisma"]
    for nome in nomes:
        rolagem = rolar_dado(lados=6, qtd=2)
        atributos[nome] = sum(rolagem) + 6
    return atributos

def obter_racas():
    """Retorna uma lista de raças disponíveis."""
    return ["Humano", "Elfo", "Anão"]

def obter_classes():
    """Retorna uma lista de classes disponíveis."""
    return ["Guerreiro", "Mago", "Ladino"]

def obter_habilidades_por_classe(classe):
    """Retorna uma lista de habilidades para uma classe específica."""
    habilidades = {
        "Guerreiro": ["Ataque Poderoso", "Defesa com Escudo", "Frenesi de Batalha"],
        "Mago": ["Bola de Fogo", "Mísseis Mágicos", "Invisibilidade"],
        "Ladino": ["Ataque Furtivo", "Desarmar Armadilhas", "Mãos Leves"]
    }
    return habilidades.get(classe, [])