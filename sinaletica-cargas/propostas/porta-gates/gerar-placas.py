#!/usr/bin/env python3
"""
Serie de placas de gate — Fenabel, area de cargas.

As proporcoes nao sao inventadas: foram medidas na placa original, depois de
retificada a perspetiva da fotografia (ver
referencias/02-sinaletica-atual/placa-gate-2-retificada.png).

    numeral   altura 88.3% da placa · largura 63.8% · margem esquerda 8.1%
    linha de base   4.8% acima do fundo
    GATE      caixa alta 11.8% · margem direita 10.8%
    GATE e numeral partilham a MESMA linha de base (medido: 0.0% de desvio)

Fonte de desenho: Nimbus Sans Bold, clone metrico da Helvetica, a substituir
a Neue Haas Grotesk Display Bold enquanto nao ha licenca.
"""
GATES = ["2", "3", "3a", "4", "5", "6", "7", "7a", "8", "9"]

L       = 1000
FUNDO   = "#F1ECE1"   # RAL 9010
TINTA   = "#383E42"   # RAL 7016
FONTE   = "Nimbus Sans"

CAP_EM, XH_EM = 0.717, 0.523      # metricas da Helvetica

MARGEM_E = 81                      # 8.1%
BASE     = 952                     # 4.8% do fundo
CAP      = 883                     # 88.3%
CORPO    = CAP / CAP_EM

G_CAP    = 118                     # 11.8%
G_CORPO  = G_CAP / CAP_EM
G_DIR    = 892                     # margem direita 10.8%
G_TRACO  = 5
G_TRACK  = 8

LIMITE   = G_DIR - G_CAP - 16      # onde a coluna do GATE comeca a estorvar
AVANCO   = 0.556                   # avanco dos algarismos na Helvetica, em ems
G_COMP   = 376                     # comprimento do GATE (37.6% medido)

def _gate():
    return (f'<g transform="translate({G_DIR},{BASE}) rotate(-90)">'
            f'<text x="0" y="0" font-family="{FONTE}" font-weight="bold" '
            f'font-size="{G_CORPO:.0f}" letter-spacing="{G_TRACK}" fill="none" '
            f'stroke="{TINTA}" stroke-width="{G_TRACO}">GATE</text></g>')

def _txt(x, y, corpo, s):
    return (f'<text x="{x:.0f}" y="{y:.0f}" font-family="{FONTE}" '
            f'font-weight="bold" font-size="{corpo:.0f}" fill="{TINTA}">{s}</text>')

def placa(rotulo, variante="A"):
    num, letra = rotulo[0], rotulo[1:]
    corpo_extra = ""

    if not letra:
        corpo = _txt(MARGEM_E, BASE, CORPO, num)

    elif variante == "A":
        # sufixo em expoente, no canto superior direito.
        # Espelha a construcao do logotipo, onde a marca circular assenta
        # em expoente sobre o canto superior direito da palavra.
        #
        # A posicao e derivada da largura real do numeral, nao fixada a mao:
        # com uma coordenada fixa o 'a' encostava a barra superior do 7.
        # Na vertical cruza a coluna do GATE, mas sem se tocarem — o GATE
        # so ocupa a metade de baixo.
        corpo = _txt(MARGEM_E, BASE, CORPO, num)
        xh = 150
        ca = xh / XH_EM
        x_a = MARGEM_E + AVANCO * CORPO + 14
        assert x_a + AVANCO*ca <= L - 55, "sufixo sai da placa"
        assert (BASE - CAP) + xh < BASE - G_COMP, "sufixo colide com o GATE"
        corpo_extra = _txt(x_a, (BASE - CAP) + xh, ca, letra)

    elif variante == "B":
        # par a mesma altura, reduzido para caber na largura util.
        # Centrado na vertical: mantido na linha de base ficava com metade
        # da placa vazia por cima, o que julgava a variante pelo defeito errado.
        cb = (LIMITE - MARGEM_E) / (0.556 * 2)
        alt = CAP_EM * cb
        corpo = _txt(MARGEM_E, (L + alt) / 2, cb, num + letra)

    else:  # "C"
        # sufixo sobre a linha de base. O numeral tem de encolher bastante:
        # a largura util ate a coluna do GATE nao chega para os dois a corpo
        # cheio — e exatamente o custo desta variante.
        cc = CORPO * 0.62
        corpo = _txt(MARGEM_E, BASE, cc, num)
        corpo_extra = _txt(MARGEM_E + 0.556*cc + 16, BASE, cc*0.45, letra)

    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {L} {L}" '
            f'width="{L}" height="{L}"><title>Gate {rotulo}</title>'
            f'<rect width="{L}" height="{L}" fill="{FUNDO}"/>'
            f'{corpo}{corpo_extra}{_gate()}</svg>\n')

if __name__ == "__main__":
    for g in GATES:
        open(f"gate-{g}.svg", "w").write(placa(g))
    for v in "ABC":
        for g in ("3a", "7a"):
            open(f"variante-{v}-gate-{g}.svg", "w").write(placa(g, v))
    print("geradas", len(GATES), "placas +", 6, "variantes")
