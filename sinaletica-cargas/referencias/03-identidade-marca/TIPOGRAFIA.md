# Tipografia da sinalética

## Decisão: Poppins

> Substitui a decisão anterior (Neue Haas Grotesk). O histórico dessa análise
> está no fim, porque explica o que se ganhou e o que se perdeu.

Geométrica, monolinear, formas circulares. **É a mesma família de desenho do
logótipo** — o `fenabel` também é geométrico e de traço constante. Encaixa na
marca melhor do que uma grotesca encaixaria.

**Licença aberta (OFL).** Sem custo e sem restrição de uso — resolve o
problema que a Neue Haas Grotesk trazia, que obrigava a licenciar quem desenha.

## Pesos

| Peso | Onde |
|---|---|
| **SemiBold 600** | numeral do gate e o seu sufixo |
| **Bold 700** | rótulo GATE, destinos do totem |
| **Medium 500** | descritivo do gate, destaques |
| **Regular 400** | traduções inglesas, horário, avisos |

O numeral é **SemiBold**, não Bold: a esta dimensão o Bold fecha demasiado as
contraformas e a placa ganha peso a mais. O rótulo `GATE` fica em Bold porque
é pequeno — mais peso compensa oticamente o corpo reduzido.

Os descritivos escrevem-se **sem maiúscula inicial** (`acabamentos`), como a
marca faz em `fenabel` e `the heart of seating`. Acrónimos internos mantêm-se.

## Dois cuidados

### 1. Os algarismos não são tabulares

Na Poppins a largura varia **27%** entre o `7` (0,535 em) e o `4` (0,677 em).
Uma margem esquerda fixa deixa de produzir placas visualmente iguais.

**Como está resolvido:** o corpo do numeral é fixado pelo `4`, o mais largo,
para que nenhuma placa transborde. As restantes ficam com mais folga à
direita — variação subtil, aceitável.

### 2. É larga, e isso custa altura

À altura que o original tinha (88,3% da placa), o `4` em Poppins ocuparia
**85%** da largura contra **68%** da Helvetica. Somado ao rodapé do descritivo,
o numeral desce para **66%** da altura da placa.

Não há como evitar numa placa quadrada com descritivo. Se se quiser o numeral
maior, a saída é dar mais largura à placa.

### 3. Silhuetas de palavra menos distintas

As formas circulares da Poppins tornam as palavras menos reconhecíveis ao
longe do que uma grotesca. Sem consequência prática aqui: o numeral é que faz
a leitura à distância, o descritivo é de perto.

## Medidas usadas

Estão lidas do ficheiro da fonte, não estimadas — ver
`propostas/porta-gates/metricas.py`.

| | SemiBold 600 | Bold 700 |
|---|---|---|
| Caixa alta | 0,701 em | 0,705 em |
| Altura-x | 0,554 em | 0,558 em |
| `4` (o mais largo) | 0,661 em | 0,677 em |
| `7` (o mais estreito) | 0,548 em | 0,535 em |
| `GATE` | 2,593 em | 2,631 em |

`acabamentos` em Medium 500: **7,161 em**.

## Ficheiros

`fontes/Poppins-{400,500,600,700}.ttf`, obtidos do Google Fonts.

---

## Histórico — porque não é Neue Haas Grotesk

A escolha anterior tinha uma boa razão: o numeral da placa antiga já era
Helvetica, e a NHG é a revisão do desenho original — seria repor a mesma voz
afinada.

**O que se perde com a mudança:** a continuidade direta com as placas antigas,
e a distinção Display/Text que resolvia bem corpos grandes e pequenos com o
mesmo desenho.

**O que se ganha:** coerência com o logótipo, que é geométrico e não grotesco,
e o fim do problema de licenciamento.
