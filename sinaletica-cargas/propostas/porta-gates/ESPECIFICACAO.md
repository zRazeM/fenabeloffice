# Placas de Gate — proposta

Série de 10: `2` `3` `3a` `4` `5` `6` `7` `7a` `8` `9`

Cada placa leva **numeral · GATE · descritivo**.

Ficheiros: `gate-*.svg` · `serie-completa.png` · `montagem-gate-*.jpg`
(aplicado na parede real) · `opcoes-descritivo.png` (as três hipóteses)

---

## Posicionamento do descritivo — três hipóteses

O descritivo é novo e não havia sítio óbvio para ele. Foram desenhadas três
saídas, todas com a palavra mais longa (`Acabamentos`) para julgar o pior caso.

| | O que faz | Veredicto |
|---|---|---|
| **A · rodapé com filete** | numeral e GATE em cima, filete, descritivo no rodapé | **proposta** |
| B · rodapé sólido | rodapé em RAL 7016 com GATE e descritivo a branco | alternativa |
| C · descritivo vertical | descritivo rodado na coluna do GATE | **não funciona** |

**C está fora por razão técnica, não por gosto:** nas placas com sufixo (`3a`,
`7a`) o descritivo não tem onde caber e desaparece. Está no ficheiro de
comparação para se ver.

**A é a proposta.** Mantém o GATE rodado — o gesto que a marca usa nas três
peças de estacionário e que as placas existentes já têm — e usa o filete fino,
que é outro recurso da marca. E mantém a placa predominantemente RAL 9010,
que era o pedido.

**B é a alternativa a considerar** se a legibilidade do descritivo à distância
for prioritária: a barra sólida dá-lhe muito mais presença. O custo é perder o
GATE rodado e escurecer 21% de uma placa que se pediu branca.

O numeral tem a mesma altura em A e em B — a diferença é só o tratamento do
descritivo.

---

## Especificação

| | |
|---|---|
| Formato | Quadrado |
| Fundo | **RAL 9010** branco puro |
| Tinta | **RAL 7016** cinza antracite |
| Fonte | **Poppins** — Bold 700 no numeral, Medium 500 no descritivo |
| GATE | sólido, rodado 90°, caixa alta a 7,3%, partilha a linha de base do numeral |

### Grelha (em % do lado da placa)

| | |
|---|---|
| Margem esquerda | 8,1% |
| Filete, do topo | 76,8% |
| Caixa alta do numeral | 66,0% |
| Linha de base do numeral | 72,2% |
| GATE — margem direita | 10,8% |
| Descritivo | até 83,8% de largura |

A margem de 8,1% e a posição do GATE são herdadas da placa original medida
(`referencias/02-sinaletica-atual/placa-gate-2-retificada.png`).

### Porque o numeral caiu de 88,3% para 66,0%

Duas razões somam-se:
1. O rodapé do descritivo tira 23% da altura.
2. A Poppins é larga — à altura antiga, o `4` ocuparia 85% da largura contra
   68% da Helvetica.

O corpo é fixado pelo `4`, o mais largo da série, para que nenhuma placa
transborde. Ver `referencias/03-identidade-marca/TIPOGRAFIA.md`.

### O rótulo GATE

Era a contorno na placa antiga. **Deixou de ser** — o contorno funcionava na
Helvetica, mas a Poppins é monolinear: contorná-la deixa duas linhas finas
paralelas com um vazio grande no meio e as letras perdem a forma, sobretudo
o `G` circular.

Passou a **sólido e mais pequeno** (caixa alta a 7,3% contra 11,8%). Fica
subordinado pelo tamanho em vez de por um truque de traço, e mantém a rotação
de 90° que é o gesto da marca.

Foram desenhados cinco tratamentos — ver `opcoes-gate.png`. Trocar é uma linha
em `gerar-placas.py`: `GATE_ESTILO`, que aceita `solido-pequeno`,
`solido-claro`, `rodape`, `nenhum` ou `contorno`.

> **O GATE não é decorativo.** É a palavra inglesa da placa, para
> transportadores estrangeiros. Por isso "sem GATE", apesar de ser a versão
> mais limpa, custa alguma coisa.

### Sufixo do `3a` e do `7a`

Mantém-se em expoente, no canto superior direito — o gesto que o logótipo faz
com a marca circular sobre a palavra.

Duas coisas são **derivadas, não fixadas à mão**: a posição sai da largura real
do numeral (que na Poppins muda de gate para gate) e a altura sai de uma fração
fixa da caixa alta (17%), para o sufixo manter sempre a mesma relação com o
algarismo. Com valor absoluto, ao encolher o numeral o sufixo passou de 17%
para 23% dele e começou a competir com o algarismo.

O gerador tem verificações que falham se o sufixo sair da placa ou tocar no GATE.

---

## Descritivos — por preencher

Preencher `descritivos.json` e correr `python3 gerar-placas.py`. Onde estiver
vazio, sai o marcador `[descritivo]` — nunca uma palavra inventada.

**A palavra mais longa fixa o corpo de todas as placas.** Hoje é
`Acabamentos`. Se entrar uma maior, todas encolhem — vale a pena fechar a lista
antes de produzir.

## Por decidir

- [ ] Os 10 descritivos
- [ ] Variante **A** ou **B**
- [ ] Tratamento do GATE — proposto `solido-pequeno`
- [ ] `3a` ou `3A`?
- [ ] Dimensão real em mm
- [ ] Material e processo

## Regenerar

```
python3 gerar-placas.py A     # ou B
python3 montagem.py
```
