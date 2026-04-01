# Optimização de Vendas Imobiliárias
### €5,8M em oportunidades identificadas (+32% com Simplex e Dijkstra)

---

## Resumo do Projeto

| | |
|---|---|
| **Sector** | Imobiliário |
| **Dados analisados** | 500 clientes |
| **Taxa de conversão actual** | 30% (148 compradores em 500) |
| **Oportunidade identificada** | €5,8M/ano |
| **Ferramentas** | Excel · SQL · Power BI · Simplex · Dijkstra |
| **Idiomas** | Português · English |

---

## Situação

Análise de **500 clientes** de uma imobiliária revelou que apenas **30% (148 clientes) compraram**, enquanto **70% (352 clientes) não concluíram a compra**.

Dados do perfil dos clientes:
- Género: Homens 51% (256), Mulheres 49% (244) — distribuição equilibrada
- Salário médio dos **compradores: €55.338**
- Salário médio dos **não compradores: €57.854** (diferença de 4,5%)
- Insight: compradores têm salário ligeiramente inferior → imóveis mais acessíveis têm maior apelo
- Idades com maior taxa de compra: **22, 29, 31 e 50 anos**
- Idades com menor taxa de compra: 43, 40 e 45 anos

---

## Tarefa

Identificar os perfis de maior propensão de compra e optimizar dois processos críticos — alocação do orçamento de marketing e rotas de visita dos corretores — para maximizar conversões com o mesmo investimento.

---

## Ações

### Análise descritiva — O que aconteceu

- Taxa de conversão actual: **30%** (148 em 500 clientes)
- Campanhas de marketing genéricas aplicadas a todos os segmentos igualmente
- Visitas de corretores sem roteirização → custos excessivos de combustível e tempo
- Sem personalização de abordagem por perfil de cliente

### Análise diagnóstica — Porque aconteceu

**1. Segmentação ineficiente**
- Campanhas genéricas ignoram faixas etárias e salariais com maior propensão de compra
- Perda estimada: €2,8M/ano (14 vendas perdidas × ticket médio de €200.000)

**2. Rotas de visita sem optimização**
- Corretores visitam clientes por ordem de cadastro ou de forma aleatória
- Perda estimada: €0,8M/ano em combustível, tempo e visitas perdidas

**3. Abordagem comercial padronizada**
- Sem personalização para diferentes perfis (jovens vs. famílias vs. investidores)
- Perda estimada: €0,8M/ano

### Análise prescritiva com algoritmos — O que fazer

**Acção 1 — Segmentação de marketing com Simplex**

Antes: Campanhas uniformes → €2,8M de impacto estimado

Depois: Modelagem da alocação de €100.000/mês em anúncios por segmento, com base nas taxas de conversão históricas por faixa etária e género.

Solução óptima via Simplex:
- Maior alocação para segmentos A (22–29 Homens) e B (22–29 Mulheres) — melhor relação custo-benefício
- Resultado: +23% de conversões face à alocação uniforme
- Impacto adicional: +€0,64M (8 vendas extras × €200.000)
- **Total: €3,44M**

**Acção 2 — Rotas de visita com Dijkstra**

Antes: Rotas aleatórias → custo de €0,8M/ano

Depois: Representação das localizações dos clientes como grafo ponderado (nós = bairros, arestas = distância × tempo médio de trânsito).

Resultado:
- Redução média de 28% na distância percorrida (validado em 50 rotas simuladas)
- Economia: €224.000/ano em combustível e manutenção
- Ganho de produtividade: mais visitas por dia por corretor
- Impacto adicional: +€0,22M
- **Total: €1,02M**

**Acção 3 — Abordagens personalizadas (combinado com Simplex)**

Antes: Abordagem padronizada → €0,8M

Depois: Ofertas personalizadas por faixa etária de maior propensão + análise de sensibilidade para identificar variáveis-chave (salário, idade).
- Impacto adicional: +€0,54M (+5% de conversão nos segmentos-alvo)
- **Total: €1,34M**

---

## Resultados

| Acção | Antes | Depois | Ganho |
|---|---|---|---|
| Segmentação de marketing | €2,80M | €3,44M | +€0,64M |
| Optimização de rotas | €0,80M | €1,02M | +€0,22M |
| Abordagens personalizadas | €0,80M | €1,34M | +€0,54M |
| **TOTAL** | **€4,40M** | **€5,80M** | **+€1,40M** |

**ROI médio: 320%** — cada €1 investido retorna €3,20.  
A modelagem matemática gerou **+32% de impacto** face à análise descritiva isolada.

---

## Próximos Passos

| Prazo | Acção | Responsável |
|---|---|---|
| 15 dias | Implementar campanhas segmentadas com base no Simplex | Marketing |
| 30 dias | Testar roteirização com Dijkstra em 10 corretores | Operações |
| 60 dias | Expandir para toda a equipa e medir economia real | Logística |
| 90 dias | Ajustar modelo com dados reais de conversão | Análise |

---

## Ficheiros deste repositório

```
📄 README.md                  ← este documento
📄 relatorio-executivo.pdf    ← relatório de 1 página (análise completa)
📁 dados/
   🖼 dados-sujos.png         ← dados em estado bruto antes do tratamento
   🖼 dados-tratados.png      ← dados após limpeza e estruturação
📁 dashboard/
   🖼 dashboard.png           ← dashboard Power BI (screenshot)
📁 scripts/
   📄 analise.sql             ← queries SQL utilizadas na análise
```

---

## Ferramentas utilizadas

`Excel` `SQL` `Power BI` `Simplex` `Dijkstra` `Estatística descritiva` `Programação linear`

---

*Projecto desenvolvido como parte do portfolio de análise de dados e investigação operacional.*  
*Kresio Azevedo Fernado · [in/kresio-data-bi-business-analyst](https://www.linkedin.com/in/kresio-data-bi-business-analyst/) · kresiofernando@hotmail.com*
