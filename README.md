 # Agente Inteligente para Recomendação de Cargos em Dados

### Universidade Federal do Pará
### Instituto de Ciências Exatas e Naturais
### Faculdade de Computação

**Equipe:**
* Ana Paula (202111140019)
* Antônio Vidal (202111140003)
* Lucas Moreno (201904940025)
* Luis Carlos (201904940012)
* Rodrigo Gois (202011140002)

![Python](https://img.shields.io/badge/Python-3.9-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0-lightgrey.svg)
![Docker](https://img.shields.io/badge/Docker-Compose-blue.svg)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-1.3-orange.svg)

---

## 1. Resumo do Projeto

Este projeto consiste na construção de um sistema completo de Machine Learning para recomendar o cargo ideal na área de dados, com base no perfil de um usuário. O sistema foi desenvolvido como trabalho final da disciplina de Inteligência Artificial da UFPA.

A solução final é uma aplicação web interativa que integra um modelo de classificação treinado em Python. A aplicação utiliza **Flask** para o backend (API) e é totalmente orquestrada por **Docker Compose**, o que garante uma execução simplificada, portabilidade e um ambiente de produção robusto.

## 2. O Processo de Data Science (KDD)

Toda a análise de dados, pré-processamento, treinamento e avaliação dos modelos de Machine Learning estão documentados em detalhes no Jupyter Notebook principal do projeto:
**[`ml/state-of-data-brazil.ipynb`](ml/state-of-data-brazil.ipynb)**

As principais etapas do processo KDD, detalhadas no notebook, foram:

* **Seleção e Análise Exploratória:** Investigação do dataset "State of Data Brazil 2022" para identificar características como distribuição de classes e valores ausentes. A principal conclusão foi o forte desbalanceamento de classes na variável alvo (`cargo`), o que guiou as etapas seguintes.
* **Pré-processamento e Enriquecimento:** Limpeza dos dados, tratamento de valores ausentes e engenharia de features, com destaque para a transformação do atributo `tempo_experiencia_dados` em uma variável numérica ordinal.
* **Mineração de Dados (Modelagem):** Foram treinados e avaliados dois modelos de classificação (Árvore de Decisão e Rede Neural). Após a avaliação, o modelo de **Árvore de Decisão** foi selecionado como a versão final devido ao seu desempenho superior.

### Escolha do Modelo Final

A performance dos modelos no conjunto de teste foi a seguinte:

| Modelo              | Acurácia (Teste) | F1-Score (Teste) |
| :------------------ | :--------------- | :--------------- |
| **Árvore de Decisão** | **50.92%** | **0.4959** |
| Rede Neural         | 40.48%           | 0.4086           |

---

## 3. Arquitetura e Evolução do Agente

A arquitetura do projeto passou por uma evolução, começando com uma prova de conceito no n8n e finalizando com uma solução mais integrada e profissional via Docker Compose.

### 3.1. Prova de Conceito com n8n

Conforme os requisitos originais do projeto, foi desenvolvida uma prova de conceito utilizando a plataforma de automação n8n. O fluxo construído realizava o ciclo completo: recebimento de dados via Webhook, pré-processamento em nós de código, requisição à API Flask e envio da resposta. Durante esta fase, foram superados desafios de integração, como a configuração de rede entre containers e a resolução de políticas de segurança (CORS). O workflow funcional desta etapa pode ser encontrado no arquivo `n8n/state-of-data-brazil-workflow.json`.

### 3.2. Arquitetura Final com Docker Compose

Com a concordância do professor, e devido às complexidades de depuração do n8n em ambiente local, a arquitetura final evoluiu para uma solução mais coesa e portátil, integrando o front-end diretamente com a API Flask, com todo o sistema sendo orquestrado pelo Docker Compose.

```
+---------------------------+      HTTP Request      +---------------------------+
|                           |  (Payload com perfil)  |                           |
|  Front-End (index.html)   | ---------------------> |   API Flask (app.py)      |
|  (Servido pelo Flask)     |                        |   (Dentro do Container    |
|                           | <--------------------- |   Docker)                 |
+---------------------------+   (Resposta com a     +---------------------------+
                                  recomendação)                |
                                                               | Carrega modelo treinado
                                                               v
                                                      +------------------------+
                                                      |   Modelo de ML         |
                                                      |   (decision_tree.joblib)|
                                                      +------------------------+
```

Esta abordagem final é mais robusta, fácil de executar e alinhada com práticas modernas de deployment de aplicações de IA.

---

## 4. Guia de Execução

Este projeto foi containerizado com Docker para garantir uma execução simples e livre de problemas de dependência.

### 4.1. Pré-requisitos

* **Docker Desktop:** Instalado e em execução na sua máquina.

### 4.2. Como Rodar

Com o Docker Desktop rodando, o processo é extremamente simplificado:

1.  Clone este repositório para a sua máquina.
2.  Abra um terminal na pasta raiz do projeto.
3.  Execute o seguinte comando:
    ```bash
    docker-compose up
    ```
4.  Aguarde o Docker construir a imagem e iniciar o servidor. Quando os logs indicarem que o servidor está rodando na porta `5000`, a aplicação estará pronta.
5.  Abra seu navegador e acesse: **`http://localhost:5000`**

A interface do usuário aparecerá. Preencha o formulário para obter sua recomendação de cargo. Para desligar a aplicação, volte ao terminal e pressione `Ctrl + C`.

---
## 5. Estrutura do Repositório

```
.
├── app/                  # Contém a aplicação Flask (API e Front-End)
│   ├── templates/
│   │   └── index.html    # Arquivo do Front-End
│   ├── app.py            # Lógica da API Flask
│   └── requirements.txt  # Dependências da API
├── ml/                     # Contém os ativos de Machine Learning
│   ├── data/
│   │   └── sods.csv      # Dataset original
│   ├── models/           # Modelos treinados (.joblib)
│   └── state-of-data-brazil.ipynb  # Notebook principal com toda a análise
├── n8n/                    # Contém o workflow da prova de conceito com n8n
│   └── state-of-data-brazil-workflow.json
├── .gitignore              # Arquivos a serem ignorados pelo Git
├── docker-compose.yml      # Orquestrador da aplicação
└── requirements.txt        # Dependências para a fase de experimentação
