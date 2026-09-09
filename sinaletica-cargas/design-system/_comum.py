import re, pathlib

LOGO_SVG_PATH = pathlib.Path('../referencias/03-identidade-marca/Logo.svg')

def logo(altura=42):
    s = LOGO_SVG_PATH.read_text()
    corpo = re.findall(r'<path class="(cls-\d)" d="([^"]+)"/>', s)
    ps = "".join(
        f'<path fill="{"#E42313" if c=="cls-1" else "#4D4C4C"}" d="{d}"/>'
        for c, d in corpo)
    w = 128.79 / 36.65 * altura
    return (f'<svg viewBox="0 0 128.79 36.65" width="{w:.0f}" height="{altura}" '
            f'role="img" aria-label="fenabel">{ps}</svg>')

# paleta do documento
PAPEL, TINTA, CINZA = "#F7F6F3", "#2E2E2C", "#4D4C4C"
MUDO, FILETE, VERM  = "#8A8781", "#DAD7D0", "#E42313"
RAL9010, RAL7016    = "#F1ECE1", "#383E42"

PILHA = ('"Neue Haas Grotesk Display Pro","Neue Haas Grotesk Text Pro",'
         '"Helvetica Neue",Helvetica,Arial,sans-serif')

# geometria medida na placa original, em milesimos do lado
CAP, MARG_E, BASE = 883, 81, 952
G_CAP, G_COMP, G_DIR = 118, 376, 892
AVANCO, CAP_EM, XH_EM = 0.556, 0.717, 0.523
CORPO = CAP / CAP_EM

def plate_svg(num, letra="", lado=1000, ral=RAL9010, tinta=RAL7016, grelha=False,
              encher=False):
    """A placa como SVG embutido — mesmos numeros do gerador de producao.

    encher=True faz a placa preencher a largura do contentor. A altura tem de
    vir do CSS: height="auto" como ATRIBUTO de SVG e invalido e o browser
    estica a placa ate uma altura absurda (ja aconteceu — 2263px numa moldura
    de 760).
    """
    g = ""
    if grelha:
        g = (f'<g stroke="{VERM}" stroke-width="2" stroke-dasharray="7 7" fill="none">'
             f'<line x1="{MARG_E}" y1="0" x2="{MARG_E}" y2="1000"/>'
             f'<line x1="0" y1="{BASE}" x2="1000" y2="{BASE}"/>'
             f'<line x1="0" y1="{BASE-CAP}" x2="1000" y2="{BASE-CAP}"/>'
             f'<line x1="{G_DIR}" y1="0" x2="{G_DIR}" y2="1000"/></g>')
    suf = ""
    if letra:
        xh = 150
        suf = (f'<text x="{MARG_E + AVANCO*CORPO + 14:.0f}" y="{BASE-CAP+xh:.0f}" '
               f'font-size="{xh/XH_EM:.0f}" font-weight="700" fill="{tinta}">{letra}</text>')
    pilha = PILHA.replace(chr(34), chr(39))
    dim = ('style="display:block;width:100%;height:auto;font-family:' + pilha + '"'
           if encher else
           f'width="{lado}" height="{lado}" style="font-family:{pilha}"')
    return (f'<svg viewBox="0 0 1000 1000" {dim}>'
            f'<rect width="1000" height="1000" fill="{ral}"/>'
            f'<text x="{MARG_E}" y="{BASE}" font-size="{CORPO:.0f}" font-weight="700" '
            f'fill="{tinta}">{num}</text>{suf}'
            f'<g transform="translate({G_DIR},{BASE}) rotate(-90)">'
            f'<text x="0" y="0" font-size="{G_CAP/CAP_EM:.0f}" font-weight="700" '
            f'letter-spacing="8" fill="none" stroke="{tinta}" stroke-width="5">GATE</text></g>'
            f'{g}</svg>')

CABECA = '''<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
  <style>
    body {{ margin:0; background:{papel}; color:{cinza};
      font-family:{pilha}; -webkit-font-smoothing:antialiased; }}
    a {{ color:{verm}; }} a:hover {{ color:#b31b0f; }}
    .folha {{ padding:64px 64px 56px; box-sizing:border-box; height:100%;
      display:flex; flex-direction:column; }}
    .rot {{ writing-mode:vertical-rl; transform:rotate(180deg);
      letter-spacing:.34em; font-size:11px; text-transform:uppercase;
      color:{mudo}; }}
    .tit {{ font-size:38px; font-weight:700; color:{tinta}; letter-spacing:-.02em;
      line-height:1.05; margin:0; }}
    .sub {{ font-size:13px; color:{mudo}; letter-spacing:.02em; margin:10px 0 0; }}
    .rule {{ height:1px; background:{filete}; border:0; margin:0; }}
    .lbl {{ font-size:10px; letter-spacing:.28em; text-transform:uppercase;
      color:{mudo}; }}
  </style>
</helmet>
'''.format(papel=PAPEL, cinza=CINZA, pilha=PILHA, verm=VERM,
           mudo=MUDO, tinta=TINTA, filete=FILETE)

RABO = "</x-dc>\n</body>\n</html>\n"

def escrever(nome, corpo, script=""):
    pathlib.Path(nome).write_text(CABECA + corpo + "\n" + script + RABO)
    print("escrito", nome)
