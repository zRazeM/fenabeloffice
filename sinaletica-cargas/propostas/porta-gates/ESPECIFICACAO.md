# Placas de Gate — proposta

Série de 10: `2` `3` `3a` `4` `5` `6` `7` `7a` `8` `9`

Ficheiros: `gate-*.svg` (vetor, prontos a escalar) · `serie-completa.png`
(prova de conjunto) · `montagem-gate-*.jpg` (aplicado na parede real)

---

## De onde vêm as proporções

**Não foram inventadas.** A fotografia da placa existente foi retificada
(perspetiva corrigida para um quadrado) e medida a pixel. O resultado está em
`referencias/02-sinaletica-atual/placa-gate-2-retificada.png`.

| | Medido no original |
|---|---|
| Altura do numeral | **88,3%** do lado da placa |
| Largura do numeral | 63,8% |
| Margem esquerda | 8,1% |
| Linha de base | 4,8% acima do fundo |
| GATE — caixa alta | 11,8% |
| GATE — comprimento | 37,6% |
| GATE — margem direita | 10,8% |

**Descoberta útil:** o GATE e o numeral partilham exatamente a mesma linha de
base — desvio medido de 0,0%. Não era evidente a olho e é a regra que
mantém a composição estável em toda a série.

O desenho novo mantém estas proporções. O que muda é a cor de fundo, a
qualidade do desenho da letra, e a solução para as placas com sufixo.

---

## Especificação

| | |
|---|---|
| Formato | Quadrado |
| Fundo | **RAL 9010** branco puro |
| Tinta | **RAL 7016** cinza antracite |
| Fonte | **Neue Haas Grotesk Display Bold** |
| GATE | a contorno, traço 0,5% do lado, rodado 90° (lê-se de baixo para cima) |

### Porquê RAL 7016 e não o cinza da marca

O cinza do logótipo é `#4D4C4C` e dá **7,26:1** sobre branco. Legível, mas
fraco para um numeral que um camião tem de ler em manobra. O RAL 7016 dá
**9,21:1** e continua na mesma família cinza-escura. Se se preferir mais
presença, o RAL 9004 dá 11,25:1.

O vermelho da marca (`#E42313`) dá 3,92:1 — **não serve para o numeral.**

---

## O sufixo do `3a` e do `7a`

O sistema original resolve **um** carácter a ocupar 88% da placa. Com dois, a
regra parte-se: um numeral a corpo cheio ocupa 68% da largura e a coluna do
GATE ocupa outros 23%. Sobram 9% — não chega para uma segunda letra ao lado.

Foram desenhadas três saídas (`variante-*.svg`, comparadas em
`comparacao-variantes-3a.png`):

| | O que faz | Custo |
|---|---|---|
| **A · expoente** | numeral a corpo cheio, `a` em expoente no canto superior direito | nenhum no numeral |
| B · par à mesma altura | os dois caracteres do mesmo corpo | numeral cai para ~44% — placa esvazia-se |
| C · sufixo na base | `a` pequeno sobre a linha de base | numeral cai para ~62% |

**Proposta: A.** É a única em que as dez placas mantêm o numeral do mesmo
tamanho — o que faz a série ler como um sistema em vez de dez peças avulsas.
E não é um recurso arbitrário: **o logótipo faz o mesmo gesto**, com a marca
circular em expoente sobre o canto superior direito da palavra.

> Isto corrige a recomendação anterior. Antes de medir a placa eu tinha
> proposto o sufixo na base (variante C). A medição mostrou que não há
> largura para isso sem encolher o numeral, portanto a resposta mudou.

O `a` é posicionado a partir da largura real do numeral, não por coordenada
fixa — com valor fixo encostava à barra superior do `7`. O gerador tem
verificações que falham se algum sufixo sair da placa ou tocar no GATE.

---

## Por decidir

- [ ] **`3a` ou `3A`?** A marca escreve tudo em minúsculas, o `GATE` está em
      maiúsculas. A proposta usa minúscula.
- [ ] **Dimensão real em mm.** As proporções são relativas, o vetor escala
      para qualquer tamanho. Falta a medida do painel para fechar produção.
- [ ] **Consistência absoluta:** se se quiser o numeral rigorosamente igual em
      todas e sem expoente, a alternativa é dar **mais largura às duas placas
      com letra**. Deixam de ser quadradas, mas o numeral fica intocado.
- [ ] Material, processo (vinil recortado / impressão / pintura) e
      profundidade da aba do painel
- [ ] Licença da Neue Haas Grotesk — ver `03-identidade-marca/TIPOGRAFIA.md`

## Nota técnica

Os SVG estão desenhados com **Nimbus Sans Bold**, clone métrico da Helvetica,
como substituta da Neue Haas Grotesk Display Bold enquanto não há licença. As
proporções e posições não mudam ao trocar a fonte; muda o desenho fino das
letras. Antes de produzir, trocar a fonte e vetorizar os cortes.

Regenerar tudo: `python3 gerar-placas.py && python3 montagem.py`
