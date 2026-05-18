# Real Estate Sales Optimisation
### €5.8M in opportunities identified · ROI 320%

> **Sector:** Real Estate  
> **Data:** 500 clients · Conversion analysis  
> **Tools:** SQL · Excel · Power BI · Simplex · Dijkstra · Segmentation  
> **Languages:** Português · English

---

## Live Systems

| System | Link | Status |
|--------|------|--------|
| 📊 Interactive Dashboard | *[coming soon]* | In development |
| 🗄️ SQL Analysis (Google Colab) | *[coming soon]* | In development |
| ⚙️ Optimisation App (Streamlit) | *[coming soon]* | In development |

---

## STAR — Português

### Situação
Análise de **500 clientes** de uma imobiliária revelou que apenas **30% (148 clientes) compraram**, enquanto **70% (352 clientes) não concluíram a compra**.

Dados do perfil dos clientes:
- Género: Homens 51% (256), Mulheres 49% (244)
- Salário médio dos **compradores: €55.338**
- Salário médio dos **não compradores: €57.854** (diferença de 4,5%)
- Insight: compradores têm salário ligeiramente inferior → imóveis mais acessíveis têm maior apelo
- Idades com maior taxa de compra: **22, 29, 31 e 50 anos**

### Tarefa
Identificar os perfis de maior propensão de compra e optimizar dois processos críticos — alocação do orçamento de marketing e rotas de visita dos corretores — para maximizar conversões com o mesmo investimento.

### Ações

**Análise descritiva — O que aconteceu:**
- Taxa de conversão actual: **30%** (148 em 500 clientes)
- Campanhas de marketing genéricas aplicadas a todos os segmentos igualmente
- Visitas de corretores sem roteirização → custos excessivos de combustível e tempo
- Sem personalização de abordagem por perfil de cliente

**Análise diagnóstica — Porque aconteceu:**

1. **Segmentação ineficiente** — Campanhas genéricas ignoram faixas etárias e salariais com maior propensão → Perda estimada: €2,8M/ano
2. **Rotas sem optimização** — Corretores visitam clientes por ordem de cadastro ou aleatória → Perda estimada: €0,8M/ano
3. **Abordagem padronizada** — Sem personalização para diferentes perfis → Perda estimada: €0,8M/ano

**Análise prescritiva com algoritmos — O que fazer:**

Simplex — Segmentação de marketing:
- Modelagem da alocação de €100.000/mês em anúncios por segmento
- Alocação óptima: maior foco nos segmentos 22–29 (homens e mulheres)
- Resultado: +23% de conversões face à alocação uniforme
- Impacto adicional: +€0,64M → **Total: €3,44M**

Dijkstra — Rotas de visita:
- Representação das localizações dos clientes como grafo ponderado
- Cálculo da rota mais curta que visita todos os clientes do dia
- Redução média de 28% na distância percorrida (validado em 50 rotas)
- Economia: €224.000/ano + ganho de produtividade
- Impacto adicional: +€0,22M → **Total: €1,02M**

Abordagens personalizadas + Análise de sensibilidade:
- Identificação das variáveis que mais impactam a decisão de compra (salário, idade)
- Ofertas personalizadas por faixa etária de maior propensão
- Impacto adicional: +€0,54M → **Total: €1,34M**

### Resultado

| Acção | Antes | Depois | Ganho |
|-------|-------|--------|-------|
| Segmentação de marketing | €2,80M | €3,44M | +€0,64M |
| Optimização de rotas | €0,80M | €1,02M | +€0,22M |
| Abordagens personalizadas | €0,80M | €1,34M | +€0,54M |
| **TOTAL** | **€4,40M** | **€5,80M** | **+€1,40M** |

**ROI médio: 320%** — cada €1 investido retorna €3,20.  
A modelagem matemática gerou **+32% de impacto** face à análise descritiva isolada.

---

## STAR — English

### Situation
Analysis of **500 clients** from a real estate agency revealed that only **30% (148 clients) purchased**, while **70% (352 clients) did not complete a purchase**.

Client profile data:
- Gender: Male 51% (256), Female 49% (244)
- Average salary of **buyers: €55,338**
- Average salary of **non-buyers: €57,854** (4.5% difference)
- Insight: buyers have slightly lower income → more accessible properties have greater appeal
- Ages with highest purchase rate: **22, 29, 31 and 50**

### Task
Identify the highest-propensity buyer profiles and optimise two critical processes — marketing budget allocation and agent visit routes — to maximise conversions with the same investment.

### Actions

**Descriptive analysis — What happened:**
- Current conversion rate: **30%** (148 out of 500 clients)
- Generic marketing campaigns applied equally to all segments
- Agent visits without route optimisation → excessive fuel and time costs
- No personalisation of approach by client profile

**Diagnostic analysis — Why it happened:**

1. **Inefficient segmentation** — Generic campaigns ignore age and salary groups with highest propensity → Estimated loss: €2.8M/year
2. **Unoptimised routes** — Agents visit clients by registration order or randomly → Estimated loss: €0.8M/year
3. **Standardised approach** — No personalisation for different profiles → Estimated loss: €0.8M/year

**Prescriptive analysis with algorithms — What to do:**

Simplex — Marketing segmentation:
- Modelled allocation of €100,000/month in ads across segments
- Optimal allocation: greater focus on 22–29 segments (male and female)
- Result: +23% conversions vs. uniform allocation
- Additional impact: +€0.64M → **Total: €3.44M**

Dijkstra — Visit route optimisation:
- Represented client locations as weighted graph
- Calculated shortest route visiting all daily clients
- Average 28% distance reduction (validated on 50 routes)
- Savings: €224,000/year + productivity gain
- Additional impact: +€0.22M → **Total: €1.02M**

Personalised approaches + Sensitivity analysis:
- Identified variables most impacting purchase decision (salary, age)
- Personalised offers by highest-propensity age group
- Additional impact: +€0.54M → **Total: €1.34M**

### Result

| Action | Before | After | Gain |
|--------|--------|-------|------|
| Marketing segmentation | €2.80M | €3.44M | +€0.64M |
| Route optimisation | €0.80M | €1.02M | +€0.22M |
| Personalised approaches | €0.80M | €1.34M | +€0.54M |
| **TOTAL** | **€4.40M** | **€5.80M** | **+€1.40M** |

**Average ROI: 320%** — every €1 invested returns €3.20.

---

## Next Steps

| Timeline | Action | Owner |
|----------|--------|-------|
| 15 days | Implement segmented campaigns based on Simplex | Marketing |
| 30 days | Test Dijkstra routing with 10 agents | Operations |
| 60 days | Expand to full team and measure real savings | Logistics |
| 90 days | Adjust model with real conversion data | Analytics |

---

## Repository Structure

```
📁 projecto-imobiliaria/
   📄 README.md                    ← this file
   📄 executive-report-en.pdf      ← 1-page executive report (EN)
   📄 relatorio-executivo-pt.pdf   ← relatório executivo (PT)
   📄 apresentacao-executiva.pptx  ← executive presentation
   📁 dados/
      📄 dataset-anonimizado.xlsx  ← anonymised dataset
   📁 scripts/
      📄 etl_pipeline.py           ← ETL automation pipeline
      📄 simplex_model.py          ← Marketing optimisation model
      📄 dijkstra_routes.py        ← Agent route optimisation
   📁 notebooks/
      📄 sql-analysis.ipynb        ← SQL analysis (Google Colab)
```

---

*Project developed as part of the BI & Decision Optimisation portfolio.*  
*[Kresio Azevedo Fernando](https://www.linkedin.com/in/kresio-bi-business-data-analyst/) · kresiofernando@hotmail.com · [kresio-azevedo-fernando.github.io](https://kresio-azevedo-fernando.github.io)*
