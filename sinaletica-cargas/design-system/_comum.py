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

PILHA = 'Poppins,"Century Gothic",Futura,system-ui,sans-serif'
GFONTS = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2'
          '?family=Poppins:wght@400;500;600;700&display=swap">')

# geometria medida na placa original, em milesimos do lado
CAP, MARG_E, BASE = 883, 81, 952
G_CAP, G_COMP, G_DIR = 118, 376, 892
AVANCO, CAP_EM, XH_EM = 0.556, 0.717, 0.523
CORPO = CAP / CAP_EM

import sys as _sys, pathlib as _pl
_sys.path.insert(0, str(_pl.Path(__file__).parent / '..' / 'propostas' / 'porta-gates'))
import importlib.util as _iu
_spec = _iu.spec_from_file_location(
    "gerador", _pl.Path(__file__).parent / '..' / 'propostas' / 'porta-gates' / 'gerar-placas.py')
_ger = _iu.module_from_spec(_spec); _spec.loader.exec_module(_ger)

def plate_svg(num, letra="", desc="[descritivo]", lado=1000, encher=False, layout="A"):
    """A placa, vinda do gerador de producao — uma so fonte de verdade.

    encher=True: a altura tem de vir do CSS. height="auto" como ATRIBUTO de
    SVG e invalido e o browser estica a placa (ja aconteceu: 2263px numa
    moldura de 760).
    """
    corpo = _ger.LAYOUTS[layout](num, letra, desc)
    dim = ('style="display:block;width:100%;height:auto"' if encher
           else f'width="{lado}" height="{lado}"')
    return (f'<svg viewBox="0 0 1000 1000" {dim}>'
            f'<rect width="1000" height="1000" fill="{_ger.FUNDO}"/>{corpo}</svg>')

CABECA = '''<!doctype html>
<html>
<head>
  <meta charset="utf-8">
  <script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
  {gfonts}
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
'''.format(gfonts=GFONTS, papel=PAPEL, cinza=CINZA, pilha=PILHA, verm=VERM,
           mudo=MUDO, tinta=TINTA, filete=FILETE)

RABO = "</x-dc>\n</body>\n</html>\n"

def escrever(nome, corpo, script=""):
    pathlib.Path(nome).write_text(CABECA + corpo + "\n" + script + RABO)
    print("escrito", nome)
