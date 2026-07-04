# Documento de Visão


---

## Identificação

| Campo | Valor |
|---|---|
| **Nome do projeto** | Gerenciamento de Motoboys e Otimização de Entregas |
| **Aluno** |  Eduardo dos Santos de Camargo
| **Disciplina** | Desenvolvimento com Jakarta EE |
| **Data de criação** | 06/05/2026
| **Última atualização** |  13/05/2026
| **Versão** | 1.5 |

---

## 1. Introdução

### 1.1 Propósito do documento



O propósito deste documento é fornecer uma visão clara sobre o escopo e os objetivos do sistema de backoffice focado na gestão financeira e logística de entregadores. O público-alvo abrange os desenvolvedores do sistema e as partes interessadas na operação do delivery. Ele documenta os requisitos essenciais para a leitura de endereços, automação de pagamentos por quilometragem e o mapeamento conjunto de rotas.

### 1.2 Escopo do produto


**O sistema irá:**
- Gerenciar o cadastro dos motoboys vinculados ao estabelecimento.
- Receber e processar os dados de endereços de entrega enviados pelo aplicativo móvel dos motoboys.
- Configurar e gerenciar os parâmetros de remuneração (ex: definição do valor pago por quilômetro rodado).
- Realizar análises geográficas do histórico de endereços para sugerir rotas otimizadas e agrupamento de entrega (teles que podem ser feitas na mesma viagem).
- Calcular automaticamente os valores devidos a cada entregador ao final de um turno e emitir os respectivos recibos/relatórios de fechamento.

**O sistema não irá (fora do escopo):**
- O sistema não possui integração com gateways de pagamento ou bancos; ele apenas calcula os valores e gera relatórios para o acerto manual.
- O sistema não atua como um ERP ou PDV do restaurante. O foco é estritamente na logística e no acerto financeiro com os entregadores.
- O rastreio (caso implementado) será para controle interno do estabelecimento, e não para o cliente final acompanhar a entrega.

### 1.3 Definições e siglas


| Termo | Definição |
|---|---|
| Tele| É a ida para o endereço do cliente
|  | 

---

## 2. Posicionamento

### 2.1 Declaração do problema


| Campo | Descrição |
|---|---|
| **O problema de** | gestão manual dos pagamentos por quilometragem e a falta de planejamento no agrupamento de teles para a mesma região|
| **Afeta** | os gestores/donos de estabelecimentos de delivery e os próprios motoboys|
| **Cujo impacto é** | altos custos operacionais devido a rotas não otimizadas, fechamentos financeiros lentos e suscetíveis a erros manuais, e falta de transparência no acerto de contas com os motoboys |
| **Uma solução adequada seria** | uma plataforma de backoffice integrada ao aplicativo móvel dos motoboys, que automatize a conciliação de endereços, calcule os valores devidos com base em regras predefinidas e sugira o agrupamento inteligente de rotas, centralizando a logística e o fechamento financeiro. |

### 2.2 Declaração de posição do produto


- **Para** estabelecimentos de delivery com frota própria de motoboys
- **Que** precisam gerenciar múltiplos profissionais e calcular suas respectivas remunerações de forma precisa
- **O** Agiliza Aí
- **É** um sistema de backoffice e gestão logística
- **Que** automatiza o fechamento financeiro por quilometragem e sugere o agrupamento inteligente de rotas 
- **Diferente de** planilhas eletrônicas, mapas genéricos ou processos manuais de acerto de caixa
- **Nosso produto** centraliza a operação, reduzindo custos de deslocamento e garantindo total transparência e agilidade no pagamento dos entregadores.
---

## 3. Partes interessadas (Stakeholders)


| Stakeholder | Papel | Interesse no sistema |
|---|---|---|
|Gestores / Donos | Administrador | Configurar as regras de negócio, monitorar a eficiência logística, reduzir custos com rotas otimizadas e ter acesso a relatórios gerenciais | 
| Equipe Operacional | Usuário Direto | Analisar as rotas agrupadas sugeridas pelo sistema, verificar o cálculo gerado no fim do turno e extrair os relatórios/recibos para efetuar o pagamento |
|Motoboys| Beneficiado / Usuário Indireto |	Ter a garantia de um cálculo transparente, exato e rápido de suas remunerações com base nos percursos efetivamente realizados|
|Aplicativo Mobile | Sistema Externo | Consumir e enviar dados via API (ex: localização e endereços visitados) para que o backoffice processe os cálculos e gere as rotas.|

---

## 4. Descrição dos usuários


### 4.1 Perfil: Gestor

| Campo | Descrição |
|---|---|
| **Descrição** | Responsável pela administração geral do sistema, configurações de negócio e visão estratégica.|
| **Responsabilidades** | Gerenciar o cadastro dos motoboys, definir as tabelas de preços/valores por quilometragem e analisar eventuais relatórios de operação.|
| **Nível técnico** | Intermediário |
| **Frequência de uso** | Eventual |
| **Principal necessidade** | Ter uma interface clara para atualizar rapidamente os parâmetros de remuneração e gerenciar os dados cadastrais da frota|

### 4.2 Perfil: Operador

| Campo | Descrição |
|---|---|
| **Descrição** | Usuário que atua na linha de frente da operação diária, lidando diretamente com o despacho e o acerto de contas|
| **Responsabilidades** | Conferir as rotas processadas pelo sistema, realizar o fechamento financeiro ao final do turno e emitir os recibos/relatórios para pagamento dos motoboys|
| **Nível técnico** | Básico |
| **Frequência de uso** | Diária |
| **Principal necessidade** | Um sistema ágil, sem travamentos, que calcule automaticamente o consolidado das rotas do dia para realizar o pagamento de forma rápida e livre de falhas humanas|

---

## 5. Visão geral do produto

### 5.1 Perspectiva do produto


O sistema não operará de forma isolada. Ele atuará como o módulo de backoffice integrado via API a um aplicativo móvel, onde os entregadores registram as rotas e endereços visitados. No contexto do negócio, o sistema substituirá os métodos manuais de acerto financeiro, como o uso de planilhas eletrônicas, que são lentos e suscetíveis a falhas operacionais. A aplicação centralizará a gestão, contabilizando o volume de entregas, processando os valores devidos em tempo real e sugerindo otimizações de rota. Adicionalmente, a arquitetura do produto preverá escalabilidade para, em etapas futuras (baixa prioridade), integrar o rastreamento geolocalizado da frota em tempo real.

### 5.2 Capacidades principais


| # | Capacidade | Descrição resumida |
|---|---|---|
| C01 | Gestão de Entregadores | CRUD dos dados cadastrais e o status operacional dos motoboys ativos no sistema|
| C02 | Gestão de Precificação e Distâncias | Configurar os parâmetros financeiros da operação, definindo taxas de remuneração com base em faixas de quilometragem|
| C03 | Auditoria e Edição de Entregas | Revisar as corridas registradas via aplicativo, permitindo à equipe operacional validar, editar, reatribuir a outro profissional ou invalidar registros antes do fechamento financeiro. |
| C05 | Otimização e Agrupamento de Rotas |Utilizar algoritmos (ou modelos de Machine Learning) para analisar as localizações e sugerir o agrupamento de entregas próximas, maximizando a eficiência das viagens|
| C04 |Monitoramento de Frota | Visualizar a geolocalização atualizada dos entregadores em um mapa interativo para controle logístico em tempo real (previsto para etapas futuras)|
### 5.3 Suposições e dependências


**Suposições:**
- Os entregadores possuem smartphones com conectividade contínua à internet móvel e permissão de GPS ativa para o envio de coordenadas geográficas.
- A equipe administrativa do estabelecimento manterá as tabelas de preços e cadastros de motoboys devidamente atualizados no backoffice.
- O volume de dados gerado pelas entregas diárias comportará a análise de rotas para futuras implementações de algoritmos de otimização.

**Dependências:**
- O sistema depende do pleno funcionamento e estabilidade do App mobile  para o envio correto dos pacotes de dados de viagens via API.
- Para as funcionalidades de rastreio (mapa da cidade) e roteirização, o projeto dependerá da integração com serviços terceirizados de mapas.
- O ambiente de produção dependerá de um servidor de aplicação compatível com Jakarta EE e um banco de dados estável para processar os fechamentos financeiros.
---

## 6. Restrições


| Tipo | Restrição |
|---|---|
| Tecnologia | Jakarta EE + JSF + JPA + CDI + PostgreSQL + Maven + Quarkus |
| Arquitetura | Arquitetura em camadas (Presentation / Service / Repository / Entity) |
| Controle de versão | GitHub Classroom obrigatório |
| Prazo | 5 sprints de desenvolvimento + apresentação |
| Documentação | Markdown |

---

## 7. Qualidade


| Atributo | Relevância para este sistema |
|---|---|
| Usabilidade | O sistema deve permitir que os gestores configurem parâmetros com facilidade e que a equipe operacional realize as edições e fechamentos diários de forma rápida, minimizando erros humanos durante o fim do expediente. |
| Eficiência de Desempenho | O sistema precisa garantir baixa latência no processamento em lote das rotas diárias. O fechamento financeiro e a transição entre telas devem ocorrer sem travamentos, garantindo fluidez na operação do caixa. |
| Confiabilidade | Como o sistema é responsável por consolidar rotas e gerar valores de pagamento, os cálculos matemáticos precisam ser exatos e consistentes. A integridade dos dados é crítica para evitar divergências financeiras, perdas para o estabelecimento ou atritos com os entregadores.
| | |

---

## 8. Histórico de revisões

| Versão | Data | Autor | Descrição da alteração |
|---|---|---|---|
| 1.0 | 06/05/2026| Eduardo S.C | Versão inicial |
| 1.5 | 13/05/2026  | Eduardo S.C | Versão Visão Finalizada |
