# Agente Inteligente para Recomendação de Cargos em Dados

![Python](https://img.shields.io/badge/Python-3.9-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0-lightgrey.svg)
![Docker](https://img.shields.io/badge/Docker-Compose-blue.svg)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-1.3-orange.svg)

## 1. Resumo do Projeto

Este projeto consiste na construção de um sistema completo de Machine Learning para recomendar o cargo ideal na área de dados, com base no perfil de um usuário. O sistema foi desenvolvido como trabalho final da disciplina de Inteligência Artificial da Universidade Federal do Pará (UFPA).

A solução final é uma aplicação web interativa que integra um modelo de classificação treinado em Python. A aplicação utiliza **Flask** para o backend (API) e é totalmente orquestrada por **Docker Compose**, o que garante uma execução simplificada, portabilidade e um ambiente de produção robusto.

## 2. O Processo de Data Science (KDD)

Toda a análise de dados, pré-processamento, treinamento e avaliação dos modelos de Machine Learning estão documentados em detalhes no Jupyter Notebook principal do projeto:
**[`ml/state-of-data-brazil.ipynb`](ml/state-of-data-brazil.ipynb)**

As principais etapas do processo KDD, detalhadas no notebook, foram:

* **Seleção e Análise Exploratória:** Investigação do dataset "State of Data Brazil 2022" para identificar características como distribuição de classes e valores ausentes. A principal conclusão foi o forte desbalanceamento de classes na variável alvo (`cargo`), o que guiou as etapas seguintes.
* **Pré-processamento e Enriquecimento:** Limpeza dos dados, tratamento de valores ausentes e engenharia de features, com destaque para a transformação do atributo `tempo_experiencia_dados` em uma variável numérica ordinal para melhor performance do modelo.
* **Mineração de Dados (Modelagem):** Foram treinados e avaliados dois modelos de classificação (Árvore de Decisão e Rede Neural) para a tarefa. Os hiperparâmetros foram otimizados e os experimentos rastreados com o auxílio do MLflow.

### Escolha do Modelo Final

Após a fase de avaliação, o modelo de **Árvore de Decisão** foi escolhido por apresentar um desempenho superior no conjunto de teste.

| Modelo              | Acurácia (Teste) | F1-Score (Teste) |
| :------------------ | :--------------- | :--------------- |
| **Árvore de Decisão** | **50.92%** | **0.4959** |
| Rede Neural         | 40.48%           | 0.4086           |

---

## 3. Arquitetura da Solução

O projeto evoluiu para uma arquitetura de microsserviço containerizado, mais robusta e alinhada com práticas modernas de engenharia de software.

```
+---------------------------+      HTTP Request      +---------------------------+
|                           |  (Payload com perfil)  |                           |
|  Front-End (index.html)   | ---------------------> |   API Flask (app.py)      |
|  (Executa no Navegador)   |                        |   (Dentro do Container    |
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

* **Front-End:** Interface de usuário em HTML/CSS/JS para entrada de dados.
* **API Flask:** Backend que serve o modelo de IA e responde às requisições.
* **Docker Compose:** Orquestrador que gerencia e executa a aplicação Flask de forma isolada e consistente.

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
## 5. Conclusão

O projeto cumpriu com sucesso o objetivo de criar um agente inteligente para recomendação de cargos, entregando uma aplicação web funcional que consome um modelo de Machine Learning treinado e validado. Os desafios encontrados, especialmente na configuração do ambiente de desenvolvimento, reforçam a importância de ferramentas como o Docker para garantir a reprodutibilidade e a facilidade de implantação em projetos de software.