import sys; sys.path.insert(0, '.')
from _comum import *

GATES = ["2","3","3a","4","5","6","7","7a","8","9"]

# ─────────────────────────────────────────────── capa
escrever("Main.dc.html", f'''
<div class="folha" style="gap:0">
  <div style="display:flex; justify-content:space-between; align-items:flex-start">
    <div>{logo(40)}</div>
    <div class="lbl" style="text-align:right; line-height:1.9">Rebordosa · Porto<br>Setembro 2026</div>
  </div>
  <div style="display:flex; gap:36px; flex-grow:1; margin-top:96px">
    <div class="rot">Sistema de Sinalética</div>
    <div style="flex-grow:1; display:flex; flex-direction:column">
      <h1 class="tit" style="font-size:56px">Sinalética<br>Área de Cargas</h1>
      <p class="sub" style="max-width:44ch; line-height:1.65; margin-top:22px">
        Sistema para a zona de cargas e descargas: identificação das portas de
        cais e totem direcional de entrada. As proporções das placas não são
        novas — foram medidas na sinalética existente e mantidas.</p>
      <div style="flex-grow:1"></div>
      <div style="display:flex; flex-direction:column; gap:0">
        <hr class="rule">
        {"".join(f"""<div style="display:flex; gap:20px; padding:15px 0; align-items:baseline">
          <span class="lbl" style="width:26px; color:{VERM}">{i:02d}</span>
          <span style="font-size:16px; color:{TINTA}; flex-grow:1">{t}</span>
          <span style="font-size:12px; color:{MUDO}">{d}</span></div><hr class="rule">"""
        for i,(t,d) in enumerate([
          ("Cor","RAL, contraste e limites de uso"),
          ("Tipografia","Neue Haas Grotesk · Display e Text"),
          ("Placa de gate — construção","Grelha medida no original"),
          ("Série de gates","10 placas: 2 a 9, com 3a e 7a"),
          ("Totem de entrada","Estrutura em lamelas"),
        ], start=1))}
      </div>
    </div>
  </div>
</div>''')

# ─────────────────────────────────────────────── cor
def amostra(nome, hexa, cod, nota, escuro=True):
    return f'''<div style="flex-grow:1; display:flex; flex-direction:column; gap:12px">
      <div style="height:150px; background:{hexa}; border:1px solid {FILETE}"></div>
      <div style="display:flex; flex-direction:column; gap:5px">
        <span style="font-size:15px; color:{TINTA}; font-weight:700">{cod}</span>
        <span style="font-size:12px; color:{MUDO}">{nome}</span>
        <span style="font-size:12px; color:{CINZA}; font-family:ui-monospace,Menlo,monospace">{hexa}</span>
        <span style="font-size:11px; color:{MUDO}; line-height:1.5; margin-top:4px">{nota}</span>
      </div></div>'''

linhas = [("Cinza da marca #4D4C4C","7,26:1","Legível, fraco à distância"),
          ("RAL 7016 antracite","9,21:1","Escolhido para o numeral"),
          ("RAL 9004 preto sinal","11,25:1","Alternativa de maior presença"),
          ("Vermelho #E42313","3,92:1","Só elementos grandes")]
escrever("Cor.dc.html", f'''
<div class="folha">
  <div style="display:flex; gap:36px; flex-grow:1">
    <div class="rot">Cor</div>
    <div style="flex-grow:1; display:flex; flex-direction:column">
      <h1 class="tit">Cor</h1>
      <p class="sub" style="max-width:46ch; line-height:1.6">
        Dois tons fazem a sinalética. O vermelho da marca entra só como acento —
        nunca preenche superfície, nunca faz texto.</p>
      <div style="display:flex; gap:22px; margin-top:44px">
        {amostra("Fundo das placas","#F1ECE1","RAL 9010","Branco puro. Substitui o marfim da placa antiga, que se camuflava na fachada.")}
        {amostra("Numeral e texto","#383E42","RAL 7016","Cinza antracite. Aguenta a distância de leitura melhor que o cinza da marca.")}
        {amostra("Cinza da marca","#4D4C4C","LOGÓTIPO","Reservado ao logótipo e a texto secundário. Não serve para numeral.")}
        {amostra("Acento","#E42313","MARCA","Setas do totem e pouco mais. Sem correspondência RAL boa — pedir Pantone.")}
      </div>
      <div style="margin-top:52px">
        <div class="lbl" style="margin-bottom:14px">Contraste sobre RAL 9010</div>
        <hr class="rule">
        {"".join(f"""<div style="display:flex; padding:13px 0; align-items:baseline; gap:16px">
          <span style="flex-grow:1; font-size:14px; color:{TINTA}">{a}</span>
          <span style="font-size:15px; font-weight:700; width:74px; text-align:right;
            color:{VERM if b.startswith("3,") else TINTA}">{b}</span>
          <span style="font-size:12px; color:{MUDO}; width:230px">{c}</span>
        </div><hr class="rule">""" for a,b,c in linhas)}
        <p style="font-size:12px; color:{MUDO}; line-height:1.6; margin-top:18px; max-width:60ch">
          O mínimo recomendado para texto é 4,5:1. O vermelho fica abaixo — por isso
          é acento e não tinta de leitura.</p>
      </div>
    </div>
  </div>
</div>''')

# ─────────────────────────────────────────────── tipografia
def amostraTipo(corte, corpo, peso, uso, texto, tam):
    return f'''<div style="display:flex; flex-direction:column; gap:9px; padding:22px 0">
      <div style="display:flex; gap:14px; align-items:baseline">
        <span class="lbl" style="color:{VERM}">{corte}</span>
        <span style="font-size:11px; color:{MUDO}">{corpo} · {peso}</span>
        <span style="font-size:11px; color:{MUDO}; margin-left:auto">{uso}</span>
      </div>
      <div style="font-size:{tam}; font-weight:{'700' if 'Bold' in peso else '400'};
        color:{TINTA}; line-height:1.1; letter-spacing:{'-.02em' if tam.endswith('px') and int(tam[:-2])>40 else '0'}">{texto}</div>
    </div><hr class="rule">'''

escrever("Tipografia.dc.html", f'''
<div class="folha">
  <div style="display:flex; gap:36px; flex-grow:1">
    <div class="rot">Tipografia</div>
    <div style="flex-grow:1; display:flex; flex-direction:column">
      <h1 class="tit">Neue Haas Grotesk</h1>
      <p class="sub" style="max-width:48ch; line-height:1.6">
        O numeral da placa antiga já era Helvetica. A Neue Haas Grotesk é a revisão
        do desenho original — não é mudar de voz, é repô-la afinada.</p>

      <div style="display:flex; gap:20px; margin-top:34px">
        <div style="flex-grow:1; border:1px solid {FILETE}; padding:20px">
          <div class="lbl" style="margin-bottom:9px">Display</div>
          <p style="font-size:12px; color:{CINZA}; line-height:1.6; margin:0">
            Espacejamento apertado, remates afinados. <b style="color:{TINTA}">Acima de 24 pt.</b>
            Numeral do gate, títulos do totem.</p>
        </div>
        <div style="flex-grow:1; border:1px solid {FILETE}; padding:20px">
          <div class="lbl" style="margin-bottom:9px">Text</div>
          <p style="font-size:12px; color:{CINZA}; line-height:1.6; margin:0">
            Mais aberta e robusta. <b style="color:{TINTA}">Abaixo de 24 pt.</b>
            Destinos, horário, avisos.</p>
        </div>
      </div>

      <div style="margin-top:30px">
        <hr class="rule">
        {amostraTipo("Display","Bold","Bold","Numeral do gate","3a","76px")}
        {amostraTipo("Display","Bold","Bold","Destino principal","Cargas — Cais 5","34px")}
        {amostraTipo("Text","Medium","Medium","Destino, português","Parque Clientes","22px")}
        {amostraTipo("Text","Roman","Roman","Tradução inglesa","Customer Parking","22px")}
        {amostraTipo("Text","Roman","Roman","Horário e avisos","Segunda a Sexta · 08:00–12:00 · 13:30–17:50","15px")}
      </div>

      <div style="margin-top:auto; padding-top:22px; display:flex; gap:26px">
        <div style="flex-grow:1">
          <div class="lbl" style="margin-bottom:8px; color:{VERM}">Licença</div>
          <p style="font-size:12px; color:{CINZA}; line-height:1.6; margin:0">
            Fonte comercial da Monotype. Quem <b>desenha</b> precisa de licença desktop;
            o produtor não, porque a arte-final vai vetorizada.</p>
        </div>
        <div style="flex-grow:1">
          <div class="lbl" style="margin-bottom:8px">Nesta folha</div>
          <p style="font-size:12px; color:{CINZA}; line-height:1.6; margin:0">
            Se a Neue Haas Grotesk não estiver instalada, isto está a ser
            desenhado em Helvetica — metricamente equivalente, desenho menos fino.</p>
        </div>
      </div>
    </div>
  </div>
</div>''')

# ─────────────────────────────────────────────── construção da placa
cota = f'stroke="{VERM}" stroke-width="2"'
escrever("PlacaConstrucao.dc.html", f'''
<div class="folha">
  <div style="display:flex; gap:36px; flex-grow:1">
    <div class="rot">Placa de gate · construção</div>
    <div style="flex-grow:1; display:flex; flex-direction:column">
      <h1 class="tit">Construção da placa</h1>
      <p class="sub" style="max-width:52ch; line-height:1.6">
        A fotografia da placa existente foi retificada e medida a pixel. Estas
        proporções são as do original — o desenho novo herda-as.</p>

      <div style="display:flex; gap:40px; margin-top:38px; align-items:flex-start">
        <svg viewBox="-90 -60 1240 1180" width="620" height="590"
             style="font-family:{PILHA.replace(chr(34), chr(39))}; flex-shrink:0">
          <rect width="1000" height="1000" fill="{RAL9010}" stroke="{FILETE}"/>
          <text x="{MARG_E}" y="{BASE}" font-size="{CORPO:.0f}" font-weight="700"
                fill="{RAL7016}">3</text>
          <text x="{MARG_E + AVANCO*CORPO + 14:.0f}" y="{BASE-CAP+150:.0f}"
                font-size="{150/XH_EM:.0f}" font-weight="700" fill="{RAL7016}">a</text>
          <g transform="translate({G_DIR},{BASE}) rotate(-90)">
            <text x="0" y="0" font-size="{G_CAP/CAP_EM:.0f}" font-weight="700"
                  letter-spacing="8" fill="none" stroke="{RAL7016}" stroke-width="5">GATE</text>
          </g>
          <g {cota} fill="none" stroke-dasharray="8 8" opacity=".85">
            <line x1="{MARG_E}" y1="-40" x2="{MARG_E}" y2="1040"/>
            <line x1="-60" y1="{BASE}" x2="1060" y2="{BASE}"/>
            <line x1="-60" y1="{BASE-CAP}" x2="1060" y2="{BASE-CAP}"/>
            <line x1="{G_DIR}" y1="-40" x2="{G_DIR}" y2="1040"/>
          </g>
          <g fill="{VERM}" font-size="30" font-weight="700">
            <text x="0" y="-24">8,1%</text>
            <text x="1010" y="{BASE+10}">4,8%</text>
            <text x="1010" y="{BASE-CAP+10}">6,9%</text>
            <text x="{G_DIR-96}" y="1058">10,8%</text>
            <text x="{MARG_E+16}" y="{BASE-CAP/2}" opacity=".9">88,3%</text>
          </g>
        </svg>

        <div style="flex-grow:1; display:flex; flex-direction:column">
          <div class="lbl" style="margin-bottom:12px">Medido no original</div>
          <hr class="rule">
          {"".join(f"""<div style="display:flex; padding:11px 0; gap:14px; align-items:baseline">
            <span style="flex-grow:1; font-size:13px; color:{CINZA}">{a}</span>
            <span style="font-size:14px; font-weight:700; color:{TINTA}">{b}</span>
          </div><hr class="rule">""" for a,b in [
            ("Altura do numeral","88,3%"),("Largura do numeral","63,8%"),
            ("Margem esquerda","8,1%"),("Linha de base, do fundo","4,8%"),
            ("GATE — caixa alta","11,8%"),("GATE — comprimento","37,6%"),
            ("GATE — margem direita","10,8%")])}
          <div style="margin-top:26px; border-left:2px solid {VERM}; padding-left:16px">
            <div class="lbl" style="color:{VERM}; margin-bottom:7px">A regra que não se vê</div>
            <p style="font-size:13px; color:{TINTA}; line-height:1.6; margin:0">
              O GATE e o numeral partilham <b>a mesma linha de base</b> — desvio medido
              de 0,0%. É o que segura a composição em toda a série.</p>
          </div>
          <div style="margin-top:22px">
            <div class="lbl" style="margin-bottom:7px">Sufixo do 3a e do 7a</div>
            <p style="font-size:12px; color:{CINZA}; line-height:1.6; margin:0">
              Um numeral a corpo cheio ocupa 68% da largura e o GATE outros 23%.
              Não sobra faixa para uma segunda letra ao lado, por isso o sufixo sobe
              a expoente — como a marca circular faz sobre a palavra do logótipo.
              A posição deriva da largura do numeral: fixa, encostava à barra do 7.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>''')

# ─────────────────────────────────────────────── série
escrever("Serie.dc.html", f'''
<div class="folha" style="padding:52px 56px">
  <div style="display:flex; gap:30px; flex-grow:1">
    <div class="rot">Série de gates</div>
    <div style="flex-grow:1; display:flex; flex-direction:column">
      <div style="display:flex; justify-content:space-between; align-items:flex-end">
        <div>
          <h1 class="tit" style="font-size:31px">Dez placas</h1>
          <p class="sub" style="margin-top:7px">Sem gate 1. O 3a e o 7a levam sufixo em expoente.</p>
        </div>
        <div class="lbl">Fundo RAL 9010 · Numeral RAL 7016</div>
      </div>
      <div style="display:grid; grid-template-columns:repeat(5, minmax(0, 1fr));
                  gap:22px; margin-top:30px">
        {"".join(f"""<div style="display:flex; flex-direction:column; gap:8px">
          <div style="border:1px solid {FILETE}">{plate_svg(g[0], g[1:], encher=True)}</div>
          <span class="lbl" style="{'color:'+VERM if len(g)>1 else ''}">gate {g}</span>
        </div>""" for g in GATES)}
      </div>
    </div>
  </div>
</div>''')

# ─────────────────────────────────────────────── totem
def seta(cor=VERM, virada=False):
    r = ' transform="scale(-1,1) translate(-26,0)"' if virada else ''
    return (f'<svg viewBox="0 0 26 18" width="26" height="18" style="flex-shrink:0"><g{r}>'
            f'<path d="M1 9h22M16 2l7 7-7 7" fill="none" stroke="{cor}" '
            f'stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></g></svg>')

def lamela(dir_, pt, en, pend=False):
    fundo = "#EFEDE7" if pend else RAL9010
    return f'''<div style="display:flex; align-items:center; gap:18px; padding:19px 22px;
        background:{fundo}; border:1px solid {FILETE};
        {'border-left:3px solid '+VERM if pend else ''}">
      {seta(virada=(dir_=='esq'))}
      <div style="display:flex; flex-direction:column; gap:3px; flex-grow:1">
        <span style="font-size:19px; font-weight:700; color:{RAL7016}; line-height:1.15">{pt}</span>
        <span style="font-size:14px; color:{MUDO}; line-height:1.15">{en}</span>
      </div>
      {f'<span class="lbl" style="color:{VERM}">por definir</span>' if pend else ''}
    </div>'''

picto = f'''<div style="display:flex; gap:26px; justify-content:center; padding-top:4px">
  <svg viewBox="0 0 60 60" width="52" height="52"><circle cx="30" cy="30" r="25"
    fill="none" stroke="{RAL7016}" stroke-width="4"/><line x1="12" y1="48" x2="48" y2="12"
    stroke="{RAL7016}" stroke-width="4"/><circle cx="30" cy="22" r="5" fill="{RAL7016}"/>
    <path d="M22 44v-9a8 8 0 0 1 16 0v9" fill="none" stroke="{RAL7016}" stroke-width="4"/></svg>
  <svg viewBox="0 0 60 60" width="52" height="52"><circle cx="30" cy="30" r="25"
    fill="none" stroke="{VERM}" stroke-width="6"/><text x="30" y="39" text-anchor="middle"
    font-size="24" font-weight="700" fill="{RAL7016}"
    style="font-family:{PILHA.replace(chr(34), chr(39))}">10</text></svg>
  <svg viewBox="0 0 60 60" width="52" height="52"><path d="M30 7 56 52H4Z" fill="none"
    stroke="{RAL7016}" stroke-width="4" stroke-linejoin="round"/>
    <rect x="21" y="30" width="12" height="11" fill="{RAL7016}"/>
    <path d="M35 30v11h6" fill="none" stroke="{RAL7016}" stroke-width="3"/>
    <circle cx="24" cy="44" r="2.6" fill="{RAL7016}"/><circle cx="33" cy="44" r="2.6" fill="{RAL7016}"/></svg>
</div>'''

escrever("Totem.dc.html", f'''
<div class="folha" style="padding:44px 40px 40px">
  <div style="display:flex; justify-content:space-between; align-items:flex-start">
    <div class="lbl">Totem de entrada</div>
    <div class="lbl" style="color:{VERM}">Proposta</div>
  </div>
  <div style="margin-top:26px; background:{PAPEL}; border:1px solid {FILETE};
              padding:26px 22px; display:flex; flex-direction:column; gap:24px">
    <div style="display:flex; justify-content:center; padding:6px 0 2px">{logo(30)}</div>
    <div style="display:flex; flex-direction:column; gap:7px">
      {lamela('esq','Receção','Reception')}
      {lamela('esq','Parque Clientes','Customer Parking')}
      {lamela('dir','Cargas — Cais 5','Loading — Gate 5')}
      {lamela('dir','Descargas · Transportadoras e Tecidos','Deliveries · Carriers &amp; Fabrics', pend=True)}
      {lamela('dir','Cais 2 a 9','Gates 2 to 9')}
    </div>
    <div style="border-top:1px solid {FILETE}; padding-top:18px; text-align:center">
      <div style="font-size:15px; font-weight:700; color:{RAL7016}">Segunda a Sexta · Monday to Friday</div>
      <div style="font-size:14px; color:{CINZA}; margin-top:5px">08:00 – 12:00 &nbsp;·&nbsp; 13:30 – 17:50</div>
    </div>
    {picto}
  </div>
  <div style="margin-top:24px; display:flex; flex-direction:column; gap:14px">
    <div style="border-left:2px solid {VERM}; padding-left:14px">
      <div class="lbl" style="color:{VERM}; margin-bottom:6px">Porquê lamelas</div>
      <p style="font-size:12px; color:{CINZA}; line-height:1.6; margin:0">
        A atribuição de cais ainda está a mudar. Num painel único, mudar um número
        obriga a refazer a peça inteira; em lamelas troca-se uma linha. E responde
        à fachada perfilada e à madeira ripada da marca.</p>
    </div>
    <div style="border-left:2px solid {FILETE}; padding-left:14px">
      <div class="lbl" style="margin-bottom:6px">Dois erros corrigidos</div>
      <p style="font-size:12px; color:{CINZA}; line-height:1.6; margin:0">
        O totem antigo escreve <b>Costumer</b> Parking, e anuncia Cais 3 a 9
        quando a série começa no 2.</p>
    </div>
  </div>
</div>''')
