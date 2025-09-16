# FlaskDD/model/personagem.py
class Personagem:
    def __init__(self, nome, raca, classe, atributos):
        self.nome = nome
        self.raca = raca
        self.classe = classe
        self.atributos = atributos
        self.modificadores = self._calcular_modificadores()
        self.habilidades = self._definir_habilidades()

    def _calcular_modificadores(self):
        """Calcula o modificador para cada atributo."""
        modificadores = {}
        for atributo, valor in self.atributos.items():
            mod = (valor - 10) // 2
            modificadores[atributo] = f"+{mod}" if mod >= 0 else str(mod)
        return modificadores

    def _definir_habilidades(self):
        """Define as habilidades com base na classe."""
        from .regras import obter_habilidades_por_classe # Importação local
        return obter_habilidades_por_classe(self.classe)

    def resumo(self):
        """Retorna um dicionário com o resumo do personagem."""
        return {
            "Nome": self.nome,
            "Raça": self.raca,
            "Classe": self.classe,
            "Atributos": self.atributos,
            "Modificadores": self.modificadores,
            "Habilidades": self.habilidades
        }