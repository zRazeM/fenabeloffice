# Placa de Gate — análise do existente

Fonte: `placa-gate-2-existente.jpg` · detalhe em `placa-gate-2-detalhe.jpg`

## O que existe hoje (Gate 2)

**Formato**
- Painel aproximadamente quadrado, ligeiramente mais alto que largo
- Montado saliente da parede, com aba/rebordo visível a toda a volta
  (parece painel tipo bandeja — ACM ou chapa quinada)
- Fixo na chapa perfilada, acima e à direita do vão da porta

**Cor**
- Fundo: branco-sujo / marfim, do mesmo tom da chapa da fachada
  (aparenta RAL 9002 ou 1013 — **é isto que passa a RAL 9010**)
- Tipografia: cinza-carvão muito escuro, não preto puro
  (aparenta RAL 7016 / 7021 — confirmar)

**Composição**
- Numeral enorme, a ocupar praticamente toda a altura útil do painel,
  encostado à esquerda
- Grotesca pesada, tipo Helvetica Bold / Univers 67 — o `2` tem terminal
  horizontal reto na base e remate diagonal no arranque superior
- Palavra `GATE` rodada 90° (lê-se de baixo para cima), no canto inferior
  direito, alinhada pela base do numeral e pela sua direita
- `GATE` está a **contorno (outline), sem preenchimento** — traço fino;
  é o detalhe que dá carácter à placa e vale a pena manter na revisão
- Margens generosas: o numeral respira, não toca os bordos

## Notas para o redesign

- Manter: proporção quadrada, numeral dominante, `GATE` vertical em outline.
  É um sistema que já funciona e é legível à distância.
- Alterar: fundo para **RAL 9010** (branco puro) — vai destacar mais da
  fachada marfim do que a placa atual, que quase se camufla.
- **Atenção à cor do numeral.** O cinza da marca é `#4D4C4C`, mais claro do
  que parece — dá 7,26:1 sobre branco. Legível, mas fraco para um numeral que
  tem de ser lido por um camião a manobrar. **RAL 7016** (9,21:1) ou
  **RAL 9004** (11,25:1) seguram melhor a distância e continuam dentro da
  família cinza-escura da marca. Ver `03-identidade-marca/ESPECIFICACAO-MARCA.md`.
- **Vermelho não serve para o numeral** — 3,92:1 sobre branco. Fica para
  acento pontual, se entrar.
- O `GATE` em outline perde presença a longa distância. Ponderar engrossar
  ligeiramente o traço, ou manter fino assumindo que só se lê de perto
  (o numeral é que faz o trabalho à distância).

---

## Série a produzir — 10 placas

`2` · `3` · `3a` · `4` · `5` · `6` · `7` · `7a` · `8` · `9`

Não há gate 1. O totem antigo anuncia "Cais 3 a 9", o que deixa de fora o 2 —
**a sinalética do totem tem de ser corrigida** para cobrir a série real.

### Problema de desenho: o `3a` e o `7a`

A placa atual resolve **um** carácter a ocupar a altura toda. Com `3a` e `7a`
passam a ser **dois**, e isso parte a regra. Três saídas possíveis:

1. **Letra em índice** — numeral mantém o tamanho e a posição de sempre, o `a`
   entra pequeno, encostado à direita da base do numeral. As oito placas de um
   só dígito ficam **exatamente** como estão hoje; só as duas com letra ganham
   o sufixo. É a que menos mexe no sistema existente.
2. **Dois caracteres à mesma altura** — `3a` com os dois do mesmo corpo. Fica
   coerente entre si, mas as placas com letra ficam visualmente mais densas e
   o numeral tem de encolher em todas para o conjunto casar.
3. **Caixa de largura fixa** — desenhar a partir de uma grelha que reserve
   espaço para dois caracteres em todas as placas. Sistema mais rigoroso, mas
   as placas de um dígito ficam com um vazio à direita.

**Recomendação: opção 1.** O numeral é o que se lê à distância — o `a` só
precisa de ser legível de perto, ao mesmo nível de leitura do `GATE`. E não
obriga a redesenhar as oito placas que já funcionam.

Fica também por decidir se é `3a` ou `3A`. A marca escreve tudo em minúsculas
(`fenabel`, `the heart of seating`), o que aponta para **`3a`** — mas o `GATE`
da placa está em maiúsculas. A decidir junto com o desenho.

## Por confirmar

- [ ] Dimensão real do painel (largura × altura × profundidade da aba)
- [ ] Material e processo (vinil recortado? impressão? pintura?)
- [ ] Fonte exata usada, se ainda houver a arte-final
- [ ] Cor RAL atual do numeral
- [x] ~~Que gates entram nesta série~~ — confirmado: 2, 3, 3a, 4, 5, 6, 7,
      7a, 8, 9 (10 placas, sem gate 1)
- [ ] `3a` ou `3A`?
- [ ] Altura de montagem e distância de leitura
