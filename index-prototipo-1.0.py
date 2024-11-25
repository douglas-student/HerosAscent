import random

# Lista de ranks
ranks = ["ferro", "bronze", "prata", "ouro", "platina", "ascendente", "imortal", "radiante"]

# Lista de nomes de monstros para cada rank
rank_monsters = {
    "ferro": ["Iron Golem", "Rust Beast", "Scrap Gargoyle", "Metallic Spider", "Corroded Hulk"],
    "bronze": ["Bronze Minotaur", "Copper Serpent", "Burnished Harpy", "Gleaming Wight", "Polished Fiend"],
    "prata": ["Silver Knight", "Platinum Wraith", "Moonlit Specter", "Shimmering Wyvern", "Celestial Djinn"],
    "ouro": ["Golden Dragon", "Auric Chimera", "Gilded Lich", "Radiant Behemoth", "Solar Hydra"],
    "platina": ["Platinum Leviathan", "Shining Archon", "Chrome Kraken", "Blazing Sentinel", "Crystal Drake"],
    "ascendente": ["Ascended Phantom", "Ethereal Watcher", "Spectral Guardian", "Void Stalker", "Stellar Beast"],
    "imortal": ["Immortal Titan", "Eternal Reaper", "Timeless Leviathan", "Unyielding Warden", "Boundless Fiend"],
    "radiante": ["Radiant Phoenix", "Divine Seraph", "Luminous Leviathan", "Celestial Titan", "Eclipse Dragon"]
}

# Classe base para os personagens
class Personagem:
    def __init__(self, nome, tipo, vida, xp, ataque, nivel):
        self.nome = nome
        self.tipo = tipo  # Pode ser 'heroi' ou 'inimigo'
        self.vida = vida
        self.max_vida = vida
        self.xp = xp
        self.ataque = ataque
        self.nivel = nivel  # Indica o rank atual do personagem

# Subclasse para o herói
class Heroi(Personagem):
    def __init__(self, nome):
        super().__init__(nome, "heroi", vida=100, xp=0, ataque=15, nivel="ferro")

    # Método para aumentar os atributos ao subir de nível
    def subir_nivel(self, xp_ganho):
        up_nivel = 1 + (xp_ganho / 1000)
        self.xp += xp_ganho
        self.vida = self.max_vida  # Restaura a vida ao máximo
        self.max_vida *= up_nivel
        self.ataque *= up_nivel
        
        # Poção de vida ao derrotar inimigo
        pocao = random.randint(10, 100)
        self.vida = min(self.vida + pocao, self.max_vida)
        print(
            f"Herói {self.nome} subiu de nível! Vida: {self.vida:.1f}/{self.max_vida:.1f}, "
            f"Ataque: {self.ataque:.1f}, XP: {self.xp:.1f}"
        )
        print(f"{self.nome} recebeu uma poção e sua vida foi restaurada para {self.vida:.1f}")


# Função para gerar um inimigo aleatório com base no nível do herói
def gerar_inimigo(nivel):
    nome_inimigo = random.choice(rank_monsters[nivel])
    vida = random.randint(50, 100)
    ataque = random.randint(10, 20)
    return Personagem(nome_inimigo, "inimigo", vida, 0, ataque, nivel)

# Função de ataque
def realizar_ataque(atacante, defensor):
    dano = round(random.uniform(0.1, 1) * atacante.ataque)
    defensor.vida -= dano
    print(f"{atacante.nome} afligiu um ataque, reduzindo {defensor.nome} em {dano} pontos de vida!")
    if defensor.vida <= 0:
        print(f"{defensor.nome} foi derrotado!")

# Função para calcular o nível do herói com base no XP
def atualizar_nivel_heroi(heroi):
    xp = heroi.xp
    if xp < 1000:
        heroi.nivel = "ferro"
    elif 1000 <= xp < 2000:
        heroi.nivel = "bronze"
    elif 2000 <= xp < 5000:
        heroi.nivel = "prata"
    elif 5000 <= xp < 7000:
        heroi.nivel = "ouro"
    elif 7000 <= xp < 8000:
        heroi.nivel = "platina"
    elif 8000 <= xp < 9000:
        heroi.nivel = "ascendente"
    elif 9000 <= xp < 10000:
        heroi.nivel = "imortal"
    else:
        heroi.nivel = "radiante"

# Ciclo de combate
def combate(heroi):
    while heroi.nivel != "radiante" and heroi.vida > 0:
        # Gerar inimigo com base no nível do herói
        inimigo = gerar_inimigo(heroi.nivel)
        print(f"Um inimigo surgiu: {inimigo.nome} ({inimigo.nivel}) com {inimigo.vida} pontos de vida!")

        # Combate até a derrota de um dos personagens
        while heroi.vida > 0 and inimigo.vida > 0:
            realizar_ataque(heroi, inimigo)
            if inimigo.vida > 0:
                realizar_ataque(inimigo, heroi)

        # Se o herói venceu o inimigo
        if heroi.vida > 0:
            xp_ganho = random.randint(500, 1000)
            print(f"{heroi.nome} derrotou {inimigo.nome} e ganhou {xp_ganho} pontos de experiência!")
            heroi.subir_nivel(xp_ganho)
            atualizar_nivel_heroi(heroi)
            print(f"{heroi.nome} agora é do rank {heroi.nivel}.")
        else:
            print(f"{heroi.nome} foi derrotado na dungeon! Fim de jogo.")
            return

    if heroi.nivel == "radiante":
        print(f"O herói {heroi.nome} atingiu o rank Radiante! Vencendo a dungeon!")

# Configuração do herói com input do usuário
nome_heroi = input("Digite o nome do seu herói: ")
heroi = Heroi(nome_heroi)

# Introdução
introducao = (
    f"Bem-vindo, {heroi.nome}! Você adentra a dungeon sombria, cheia de perigos. "
    "Seu destino será determinado por sua coragem e habilidade!"
)

print(introducao)

# Inicia o combate
combate(heroi)
