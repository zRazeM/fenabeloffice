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

## Informação em falta (para arrancar)

**Totem**
- [ ] Dimensões do totem antigo (altura, largura, espessura)
- [ ] Material e tipo de fixação (chapa sobre estrutura? monobloco? chumbado?)
- [ ] Ficheiro vetorial do logo Fenabel (`.ai` / `.svg` / `.eps`)
- [ ] Fonte(s) do novo estilo gráfico + cores oficiais (RAL / Pantone / HEX)
- [ ] Confirmar se a lista de destinos e o horário se mantêm iguais

**Portas / Gates**
- [ ] Dimensões exatas da placa original
- [ ] Quantas placas ao todo e que números (Cais 3 a 9? inclui o 5?)
- [ ] Substrato: chapa metálica pintada, ACM, vinil sobre porta?
- [ ] RAL 9010 é o fundo ou a numeração? Qual a cor do contraste?
- [ ] Distância de leitura (a partir de onde tem de ser legível)
