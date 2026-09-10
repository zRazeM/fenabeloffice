import sys; sys.path.insert(0, '.')
from _comum import *

GATES = ["2","3","3a","4","5","6","7","7a","8","9"]
import json, pathlib as _p
_d = json.loads((_p.Path("../propostas/porta-gates/descritivos.json")).read_text())
DESC = {g: (_d.get(g) or "[descritivo]") for g in GATES}

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
          ("Tipografia","Poppins · pesos e limites"),
          ("Placa de gate — construção","Grelha, descritivo e sufixo"),
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
def amostraTipo(peso, uso, texto, tam, w=700):
    return f'''<div style="display:flex; flex-direction:column; gap:9px; padding:20px 0">
      <div style="display:flex; gap:14px; align-items:baseline">
        <span class="lbl" style="color:{VERM}">Poppins {peso}</span>
        <span style="font-size:11px; color:{MUDO}; margin-left:auto">{uso}</span>
      </div>
      <div style="font-size:{tam}; font-weight:{w}; color:{TINTA}; line-height:1.12">{texto}</div>
    </div><hr class="rule">'''

escrever("Tipografia.dc.html", f'''
<div class="folha">
  <div style="display:flex; gap:36px; flex-grow:1">
    <div class="rot">Tipografia</div>
    <div style="flex-grow:1; display:flex; flex-direction:column">
      <h1 class="tit">Poppins</h1>
      <p class="sub" style="max-width:50ch; line-height:1.6">
        Geométrica e monolinear — a mesma família de desenho do logótipo, que
        também é geométrico e de traço constante. Encaixa melhor na marca do que
        uma grotesca encaixaria.</p>

      <div style="display:flex; gap:20px; margin-top:32px">
        <div style="flex-grow:1; border:1px solid {FILETE}; padding:18px">
          <div class="lbl" style="margin-bottom:8px; color:{VERM}">Vantagem</div>
          <p style="font-size:12px; color:{CINZA}; line-height:1.6; margin:0">
            Licença aberta (OFL). Sem custo e sem restrição de uso — ao contrário
            de uma fonte comercial, que obrigaria a licenciar quem desenha.</p>
        </div>
        <div style="flex-grow:1; border:1px solid {FILETE}; padding:18px">
          <div class="lbl" style="margin-bottom:8px">Cuidado</div>
          <p style="font-size:12px; color:{CINZA}; line-height:1.6; margin:0">
            Formas circulares dão silhuetas de palavra menos distintas à
            distância. O numeral faz o trabalho longe; o descritivo é de perto.</p>
        </div>
      </div>

      <div style="margin-top:26px; border-left:2px solid {VERM}; padding-left:15px">
        <div class="lbl" style="color:{VERM}; margin-bottom:6px">Algarismos não são tabulares</div>
        <p style="font-size:12px; color:{TINTA}; line-height:1.6; margin:0">
          Na Poppins a largura varia <b>27%</b> entre o 7 (0,535 em) e o 4
          (0,677 em). Uma margem esquerda fixa deixa de dar placas visualmente
          iguais — o corpo do numeral é fixado pelo <b>4</b>, o mais largo, para
          que nenhuma placa transborde.</p>
      </div>

      <div style="margin-top:24px">
        <hr class="rule">
        {amostraTipo("Bold 700","Numeral do gate","3a","72px")}
        {amostraTipo("Medium 500","Descritivo do gate","Acabamentos","30px",500)}
        {amostraTipo("Bold 700","Destino do totem","Cargas — Cais 5","28px")}
        {amostraTipo("Regular 400","Tradução inglesa","Loading — Gate 5","20px",400)}
        {amostraTipo("Regular 400","Horário e avisos","Segunda a Sexta · 08:00–12:00 · 13:30–17:50","14px",400)}
      </div>
    </div>
  </div>
</div>''')

# ─────────────────────────────────────────────── construção da placa
import sys as _s; _s.path.insert(0, '../propostas/porta-gates')
from metricas import cap as _cap, corpo_para_cap as _cpc, corpo_para_largura as _cpl, adv as _adv

RODAPE = 232
ZONA   = 1000 - RODAPE
BASE_N = ZONA - 46
UTIL   = (892 - 118 - 22) - 81
CORPO_N = min(_cpc(ZONA - 108), _cpl("4", UTIL))
CAP_N  = _cap() * CORPO_N
TOPO_N = BASE_N - CAP_N

escrever("PlacaConstrucao.dc.html", f'''
<div class="folha">
  <div style="display:flex; gap:36px; flex-grow:1">
    <div class="rot">Placa de gate · construção</div>
    <div style="flex-grow:1; display:flex; flex-direction:column">
      <h1 class="tit">Construção da placa</h1>
      <p class="sub" style="max-width:56ch; line-height:1.6">
        O descritivo entra num rodapé sob filete. O numeral perde altura para o
        acomodar — e perde mais ainda por a Poppins ser larga.</p>

      <div style="display:flex; gap:40px; margin-top:34px; align-items:flex-start">
        <svg viewBox="-96 -56 1250 1180" width="600" height="566" style="flex-shrink:0">
          <rect width="1000" height="1000" fill="{RAL9010}" stroke="{FILETE}"/>
          {plate_svg("3","a","Acabamentos").split(">",1)[1].rsplit("</svg>",1)[0]}
          <g stroke="{VERM}" stroke-width="2" stroke-dasharray="8 8" fill="none" opacity=".85">
            <line x1="81" y1="-36" x2="81" y2="1040"/>
            <line x1="-64" y1="{BASE_N}" x2="1064" y2="{BASE_N}"/>
            <line x1="-64" y1="{TOPO_N}" x2="1064" y2="{TOPO_N}"/>
            <line x1="892" y1="-36" x2="892" y2="{ZONA}"/>
          </g>
          <g fill="{VERM}" font-size="30" font-weight="600" font-family="Poppins">
            <text x="0" y="-20">8,1%</text>
            <text x="1012" y="{BASE_N+10:.0f}">72,2%</text>
            <text x="1012" y="{TOPO_N+10:.0f}">6,2%</text>
            <text x="97" y="{ZONA-16}">filete · 76,8%</text>
            <text x="97" y="{TOPO_N + CAP_N/2:.0f}" opacity=".9">66,0%</text>
            <text x="700" y="1056">10,8%</text>
          </g>
        </svg>

        <div style="flex-grow:1; display:flex; flex-direction:column">
          <div class="lbl" style="margin-bottom:12px">Grelha</div>
          <hr class="rule">
          {"".join(f"""<div style="display:flex; padding:10px 0; gap:14px; align-items:baseline">
            <span style="flex-grow:1; font-size:13px; color:{CINZA}">{a}</span>
            <span style="font-size:14px; font-weight:600; color:{TINTA}">{b}</span>
          </div><hr class="rule">""" for a,b in [
            ("Margem esquerda","8,1%"),("Filete, do topo","76,8%"),
            ("Caixa alta do numeral","66,0%"),("Linha de base do numeral","72,2%"),
            ("GATE — caixa alta","7,3%"),("GATE — margem direita","10,8%"),
            ("Descritivo — Medium 500","até 83,8%")])}

          <div style="margin-top:22px; border-left:2px solid {VERM}; padding-left:15px">
            <div class="lbl" style="color:{VERM}; margin-bottom:6px">Porque caiu de 88% para 66%</div>
            <p style="font-size:12px; color:{TINTA}; line-height:1.6; margin:0">
              Duas razões somam-se. O rodapé do descritivo tira 23% da altura.
              E a Poppins é larga: à altura antiga, o <b>4</b> ocuparia 85% da
              largura da placa contra 68% da Helvetica. O corpo é fixado pelo
              4 — o mais largo — para que nenhuma placa transborde.</p>
          </div>
          <div style="margin-top:18px">
            <div class="lbl" style="margin-bottom:6px">O rótulo GATE</div>
            <p style="font-size:12px; color:{CINZA}; line-height:1.6; margin:0 0 14px">
              Deixou de ser a contorno. O contorno funcionava na Helvetica; a
              Poppins é monolinear e contorná-la deixa duas linhas finas com um
              vazio no meio — o <b>G</b> circular perde a forma. Passou a sólido
              e mais pequeno: subordinado pelo tamanho, não por um truque de traço.</p>
            <div class="lbl" style="margin-bottom:6px">Sufixo e descritivo</div>
            <p style="font-size:12px; color:{CINZA}; line-height:1.6; margin:0">
              O sufixo do 3a e do 7a mantém-se em expoente, posicionado a partir
              da largura real do numeral — que na Poppins muda de gate para gate.
              O corpo do descritivo é fixado pela palavra mais longa da série,
              hoje <b>Acabamentos</b>, para que todas as placas fiquem iguais.</p>
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
          <p class="sub" style="margin-top:7px">Descritivos por preencher em <code>descritivos.json</code>. Sem gate 1.</p>
        </div>
        <div class="lbl">Fundo RAL 9010 · Numeral RAL 7016</div>
      </div>
      <div style="display:grid; grid-template-columns:repeat(5, minmax(0, 1fr));
                  gap:22px; margin-top:30px">
        {"".join(f"""<div style="display:flex; flex-direction:column; gap:8px">
          <div style="border:1px solid {FILETE}">{plate_svg(g[0], g[1:], DESC.get(g, "[descritivo]"), encher=True)}</div>
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
