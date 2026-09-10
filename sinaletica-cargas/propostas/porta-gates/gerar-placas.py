#!/usr/bin/env python3
"""
Serie de placas de gate — Fenabel, area de cargas.  Versao Poppins.

Tres hipoteses de posicionamento do descritivo (A, B, C). Todas as posicoes
sao calculadas a partir das metricas reais da Poppins lidas do ficheiro
(metricas.py), nao de valores estimados — a Poppins nao tem algarismos
tabulares e a largura do numeral varia 27% entre o 7 e o 4.

Proporcoes herdadas da placa original medida (ver
referencias/02-sinaletica-atual/placa-gate-2-retificada.png):
margem 8.1%, GATE a direita rodado 90 graus partilhando a linha de base.
"""
import sys; sys.path.insert(0, '.')
from metricas import adv, cap, xh, corpo_para_cap, corpo_para_largura

GATES = ["2","3","3a","4","5","6","7","7a","8","9"]
DESCRITIVO_MAIS_LONGO = "Acabamentos"

L        = 1000
FUNDO    = "#F1ECE1"   # RAL 9010
TINTA    = "#383E42"   # RAL 7016
FONTE    = "Poppins"

MARGEM   = 81          # 8.1%, herdado do original
G_DIR    = 892         # margem direita do GATE, 10.8%
G_CAP    = 118         # caixa alta do GATE, 11.8%
G_TRACO  = 5
G_TRACK  = 8

def _t(x, y, corpo, txt, peso=700, cor=TINTA, extra=""):
    return (f'<text x="{x:.0f}" y="{y:.0f}" font-family="{FONTE}" '
            f'font-weight="{peso}" font-size="{corpo:.0f}" fill="{cor}" {extra}>{txt}</text>')

TINTA_CLARA = "#9AA0A4"   # RAL 7016 aclarado, para papel subordinado

# Tratamento do rotulo GATE. Uma linha para mudar toda a serie.
# "solido-pequeno" | "solido-claro" | "rodape" | "nenhum" | "contorno"
GATE_ESTILO = "solido-pequeno"

def _gate_vertical(base, estilo=None):
    """Tratamentos do rotulo GATE.

    O contorno herdado da placa antiga funcionava na Helvetica. Na Poppins,
    que e monolinear, contornar deixa duas linhas finas paralelas com um vazio
    grande no meio e as letras perdem a forma — sobretudo o G circular.
    """
    estilo = estilo or GATE_ESTILO
    if estilo == "nenhum":
        return ""
    if estilo == "solido-claro":
        c = corpo_para_cap(G_CAP)
        pinta = f'fill="{TINTA_CLARA}"'
    elif estilo == "solido-pequeno":
        c = corpo_para_cap(G_CAP * 0.62)
        pinta = f'fill="{TINTA}"'
    else:  # contorno
        c = corpo_para_cap(G_CAP)
        pinta = f'fill="none" stroke="{TINTA}" stroke-width="{G_TRACO}"'
    return (f'<g transform="translate({G_DIR},{base}) rotate(-90)">'
            f'<text font-family="{FONTE}" font-weight="700" font-size="{c:.0f}" '
            f'letter-spacing="{G_TRACK}" {pinta}>GATE</text></g>')

SUFIXO_REL = 0.17   # altura-x do sufixo, em fracao da caixa alta do numeral

def _sufixo(num, corpo_num, base_num, topo_num, teto_gate=None):
    """Sufixo em expoente.

    Duas coisas sao derivadas, nao fixadas a mao: a posicao sai da largura
    real do numeral (que na Poppins muda de gate para gate) e a altura sai
    de uma fracao da caixa alta, para o sufixo manter sempre a mesma relacao
    com o numeral. Com valor absoluto, ao encolher o numeral o sufixo passou
    de 17% para 23% dele e comecou a competir com o algarismo.
    """
    altura = SUFIXO_REL * cap() * corpo_num
    c = altura / xh()
    x = MARGEM + adv(num) * corpo_num + 18
    x1 = x + adv("a") * c
    assert x1 <= L - 40, f"sufixo sai da placa: {x1:.0f}"
    if teto_gate is not None:
        assert topo_num + altura < teto_gate, (
            f"sufixo colide com o GATE: base {topo_num+altura:.0f} vs topo {teto_gate:.0f}")
    return _t(x, topo_num + altura, c, "a"), x1

# ── A · rodape com filete ────────────────────────────────────────────
def layout_A(num, letra, desc, gate=None):
    RODAPE = 232                      # altura da banda inferior
    zona   = L - RODAPE               # zona do numeral
    base   = zona - 46
    # o numeral e limitado pela coluna do GATE, nao pela altura
    largura_util = (G_DIR - G_CAP - 22) - MARGEM
    corpo = min(corpo_para_cap(zona - 108),
                corpo_para_largura("4", largura_util))
    topo  = base - cap() * corpo
    teto_g = base - (adv("GATE") * corpo_para_cap(G_CAP) + 3*G_TRACK)
    suf = _sufixo(num, corpo, base, topo, teto_g)[0] if letra else ""
    c_desc = min(corpo_para_largura(DESCRITIVO_MAIS_LONGO, L - 2*MARGEM, 500), 132)
    gate = gate or GATE_ESTILO
    if gate == "rodape":
        c_k = corpo_para_cap(38)
        kicker = _t(MARGEM, L - 78 - cap(500)*c_desc - 34, c_k, "GATE",
                    cor=TINTA_CLARA, extra='letter-spacing="9"')
        return (_t(MARGEM, base, corpo, num) + suf +
                f'<line x1="{MARGEM}" y1="{zona}" x2="{L-MARGEM}" y2="{zona}" '
                f'stroke="{TINTA}" stroke-width="3" opacity=".55"/>' +
                kicker + _t(MARGEM, L - 78, c_desc, desc, peso=500))
    return (_t(MARGEM, base, corpo, num) + suf + _gate_vertical(base, gate) +
            f'<line x1="{MARGEM}" y1="{zona}" x2="{L-MARGEM}" y2="{zona}" '
            f'stroke="{TINTA}" stroke-width="3" opacity=".55"/>' +
            _t(MARGEM, L - 78, c_desc, desc, peso=500))

# ── B · rodape solido, GATE dentro do rodape ─────────────────────────
def layout_B(num, letra, desc):
    RODAPE = 210
    topo_r = L - RODAPE
    base   = topo_r - 74
    corpo  = min(corpo_para_cap(topo_r - 130),
                 corpo_para_largura("4", L - 2*MARGEM))
    topo   = base - cap() * corpo
    suf = _sufixo(num, corpo, base, topo)[0] if letra else ""
    c_g  = corpo_para_cap(52)
    c_d  = min(corpo_para_largura(DESCRITIVO_MAIS_LONGO,
                                  L - 2*MARGEM - adv("GATE")*c_g - 60, 500), 112)
    y = topo_r + RODAPE/2 + cap(500)*c_d/2
    return (_t(MARGEM, base, corpo, num) + suf +
            f'<rect x="0" y="{topo_r}" width="{L}" height="{RODAPE}" fill="{TINTA}"/>' +
            _t(MARGEM, y, c_g, "GATE", cor=FUNDO,
               extra=f'letter-spacing="6" opacity=".75"') +
            _t(MARGEM + adv("GATE")*c_g + 60, y, c_d, desc, peso=500, cor=FUNDO))

# ── C · descritivo vertical, na coluna do GATE ───────────────────────
def layout_C(num, letra, desc):
    base = L - 48
    largura_util = (G_DIR - G_CAP - 22) - MARGEM
    corpo = min(corpo_para_cap(base - 88),
                corpo_para_largura("4", largura_util))
    topo  = base - cap() * corpo
    suf = _sufixo(num, corpo, base, topo)[0] if letra else ""
    c_g  = corpo_para_cap(G_CAP)
    comp_g = adv("GATE") * c_g + 3*G_TRACK
    # o descritivo vertical tem de comecar abaixo do sufixo, senao passa
    # por cima dele nas placas com letra (3a, 7a)
    teto = (topo + 150 + 40) if letra else 60
    espaco = (base - comp_g - 46) - teto
    c_d  = min(corpo_para_largura(DESCRITIVO_MAIS_LONGO, espaco, 500), 104)
    return (_t(MARGEM, base, corpo, num) + suf + _gate_vertical(base) +
            f'<g transform="translate({G_DIR - G_CAP*0.32:.0f},'
            f'{base - comp_g - 46:.0f}) rotate(-90)">' +
            _t(0, 0, c_d, desc, peso=500) + '</g>')

LAYOUTS = {"A": layout_A, "B": layout_B, "C": layout_C}

def placa(rotulo, desc, layout="A"):
    num, letra = rotulo[0], rotulo[1:]
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {L} {L}" '
            f'width="{L}" height="{L}"><title>Gate {rotulo} — {desc}</title>'
            f'<rect width="{L}" height="{L}" fill="{FUNDO}"/>'
            f'{LAYOUTS[layout](num, letra, desc)}</svg>\n')

def descritivos():
    """Le descritivos.json. Por preencher -> marcador visivel, nunca inventado."""
    import json, pathlib
    d = json.loads(pathlib.Path("descritivos.json").read_text())
    return {g: (d.get(g) or "[descritivo]") for g in GATES}


if __name__ == "__main__":
    import sys
    lay = sys.argv[1] if len(sys.argv) > 1 else "A"
    desc = descritivos()
    for g in GATES:
        open(f"gate-{g}.svg", "w").write(placa(g, desc[g], lay))
    for l in LAYOUTS:                       # comparacao das hipoteses
        for g in ("3a", "5"):
            open(f"opcao-{l}-gate-{g}.svg", "w").write(
                placa(g, DESCRITIVO_MAIS_LONGO, l))
    porPreencher = [g for g in GATES if desc[g] == "[descritivo]"]
    print(f"{len(GATES)} placas no layout {lay}")
    if porPreencher:
        print(f"  por preencher em descritivos.json: {', '.join(porPreencher)}")
