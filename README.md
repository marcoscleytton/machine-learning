# 💳 Detecção de Fraudes com Machine Learning

## 📌 Contexto

Fraudes em cartões de crédito representam um dos principais riscos financeiros para instituições financeiras.  
O desafio não é apenas detectar fraudes, mas **equilibrar segurança e experiência do cliente**.

- Detectar pouco → prejuízo financeiro  
- Detectar demais → fricção e insatisfação do cliente  

---

## 🎯 Problema

Construir um modelo capaz de:

> Identificar transações fraudulentas em um cenário altamente desbalanceado (<1% fraude)

com foco em **decisão de negócio**, não apenas performance técnica.

---

## 🧠 Abordagem

Este projeto foi estruturado como um pipeline de decisão:

- Tratamento de dados desbalanceados (RUS vs SMOTE)
- Modelagem com Regressão Logística
- Avaliação com métricas orientadas a fraude
- Ajuste de threshold para simular políticas de risco

---

## 📊 Resultado do Modelo

**Modelo selecionado:** Regressão Logística (RUS)

| Métrica | Resultado |
|--------|----------|
| AUC    | 0.975    |
| Recall (Fraude) | 85% |
| Precision | 11% |

---

## ⚖️ Decisão de Negócio (Ponto-chave)

O modelo não é apenas avaliado — ele é **controlado via threshold**.

| Threshold | Recall | Precision |
|----------|--------|-----------|
| 0.10     | 91%    | 2%        |
| 0.50     | 85%    | 13%       |
| 0.85     | 84%    | 29%       |

👉 Isso permite:

- Estratégia agressiva → bloquear mais fraudes  
- Estratégia conservadora → reduzir falsos positivos  

---

## 📉 Trade-off Real

O projeto evidencia o principal dilema de fraude:

> Maximizar detecção vs minimizar impacto no cliente

Esse equilíbrio é ajustável dinamicamente.

---

## 📊 Camada de Visualização

Foi desenvolvido um **dashboard interativo (Plotly Dash)** que permite:

- Ajustar threshold em tempo real
- Visualizar impacto nas métricas
- Analisar distribuição de risco
- Monitorar matriz de confusão

👉 Simula um ambiente real de tomada de decisão

---

## 💡 Impacto de Negócio

Com este modelo, é possível:

- Reduzir perdas financeiras por fraude
- Antecipar riscos em tempo real
- Ajustar políticas de risco dinamicamente
- Apoiar decisões operacionais e estratégicas

---

## ⚙️ Arquitetura do Projeto

```

fraud-detection/
│
├── models/        # modelo treinado (.pkl)
├── src/           # pipeline de ML
├── notebooks/     # exploração e análise
├── app.py         # dashboard interativo
├── train_and_save.py
└── requirements.txt

```

---

## 🚀 Próximos Passos

- Deploy como API (tempo real)
- Monitoramento de drift de dados
- Integração com sistemas transacionais
- Feature engineering avançado

---

## 👨‍💻 Autor

Marcos Cleyton  
Projeto de Machine Learning aplicado a risco financeiro
```
