# Sinalética — Área de Cargas | Fenabel

Projeto de redesenho do sistema de sinalética da zona de cargas.

## Briefing

### 1. Totem de entrada
- Substituição do totem existente, na **mesma posição** (junto à entrada do
  pavilhão, à esquerda do portão principal — ver foto do local).
- **Manter a mesma lógica de informação** do totem antigo:
  - Receção / Reception (←)
  - Parque Clientes / Costumer Parking (←)
  - Cargas – Cais 5 / Loading Docks – Gate 5 (→)
  - Cais 3 a 9 / Gates 3 to 9 (→)
  - Horário — Segunda a Sexta: 08:00–12:00 / 13:30–17:50
  - Pictogramas: entrada proibida a pessoas não autorizadas · limite de
    velocidade 10 km/h · perigo empilhadores em circulação
- **Redesign ligeiro** alinhado com o novo estilo gráfico da empresa.

### 2. Numeração de portas (Gates)
- **Mesmas dimensões** das placas originais.
- Nova cor: **RAL 9010** (branco puro).
- Design pode ser ligeiramente alterado.

## Estrutura

```
referencias/          <- É AQUI QUE DEIXAS OS FICHEIROS
  01-local-fotos/       fotos do sítio, enquadramento, medições in loco
  02-sinaletica-atual/  totem antigo, placas de porta atuais, o que existe hoje
  03-identidade-marca/  logo, manual de marca, fontes, cores, RAL
  04-inspiracao/        referências externas, moodboard, exemplos que gostas
  05-tecnico-medidas/   dimensões, materiais, desenhos, fornecedor

propostas/
  totem-entrada/        saída: propostas de design do totem
  porta-gates/          saída: propostas de design das placas de porta
```

## Como meter ficheiros aqui

O upload do GitHub pelo browser rebenta com ficheiros grandes
(**limite de 25 MB por ficheiro**, e lotes grandes dão timeout).

Ordem de preferência:

1. **Poucos de cada vez** — 1 ou 2 fotos por upload, não o lote todo.
2. **Encolher antes** — telemóvel: partilhar por email/WhatsApp em tamanho
   "médio" e voltar a guardar; Windows: Paint > Redimensionar 50%;
   Mac: Pré-visualização > Ferramentas > Ajustar Tamanho.
3. **Link de partilha** (Drive, Dropbox, WeTransfer) — manda o link no chat
   que eu descarrego, encolho e arrumo. É o caminho mais rápido para lotes.

Fotos enviadas **no chat** eu consigo ver e analisar, mas **não consigo
gravar** no repositório — chegam-me como imagem na conversa, não como
ficheiro. Serve para eu tirar notas, não para arquivar.

As fotos aqui são reduzidas para 3000 px no lado maior (~1 MB cada).
Chega e sobra para desenho; os originais ficam contigo.

## Informação em falta (para arrancar)

> A linguagem da marca já está lida a partir do estacionário — ver
> `referencias/03-identidade-marca/IDENTIDADE-ANALISE.md`. Falta o material
> de origem (vetores, fontes, valores de cor).

**Totem**
- [ ] Dimensões do totem antigo (altura, largura, espessura)
- [ ] Material e tipo de fixação (chapa sobre estrutura? monobloco? chumbado?)
- [ ] Ficheiro vetorial do logo Fenabel (`.ai` / `.svg` / `.eps`) — **bloqueio nº 1**
- [ ] Fonte(s) do novo estilo gráfico + cores oficiais (RAL / Pantone / HEX)
- [ ] Confirmar se a lista de destinos e o horário se mantêm iguais

**Portas / Gates** — ver análise detalhada em
`referencias/02-sinaletica-atual/placa-gate-ANALISE.md`
- [ ] Dimensões exatas da placa original
- [ ] Quantas placas ao todo e que números (o totem fala em Cais 3 a 9, mas
      a placa fotografada é a 2 — a série vai de 1 a 9?)
- [ ] Substrato e processo (ACM? chapa quinada? vinil recortado?)
- [ ] Cor RAL atual do numeral (aparenta cinza-carvão, não preto)
- [ ] Confirmar: RAL 9010 é o **fundo** (assumido) e o numeral mantém-se escuro?
- [ ] Distância de leitura (a partir de onde tem de ser legível)
