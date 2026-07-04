# Levantamento de Requisitos - Gerenciamento de Delivery e Motoboys

Com base nas definições de negócio levantadas, o sistema evoluiu para uma arquitetura distribuída e os requisitos foram refatorados para maior clareza.

## 1. Diagrama de Casos de Uso (Visão Geral)

```mermaid
flowchart LR
    %% Atores
    Operador([🧑‍💻 Operador Backoffice])
    Motoboy([🛵 Motoboy Mobile])
    
    %% Sistema Backoffice
    subgraph Backoffice ["Backoffice Web (BFF)"]
        direction TB
        UC1([Visualizar Mapa de Entregas])
        UC2([Agrupar Entregas])
        UC3([Despachar Entregas])
        UC4([Acompanhar Motoboys])
        UC8([Gerar Fechamento Financeiro])
        UC9([Comunicar via Chat Interno])
    end
    
    %% Sistema Mobile
    subgraph Mobile ["App Mobile (Flutter)"]
        direction TB
        UC5([Ficar Disponível / Online])
        UC6([Receber Nova Rota])
        UC7([Marcar Status - Entregue/Falhou])
        UC10([Comunicar com Backoffice])
    end
    
    %% Relacionamentos do Operador
    Operador --> UC1
    Operador --> UC2
    Operador --> UC3
    Operador --> UC4
    Operador --> UC8
    Operador --> UC9
    
    %% Relacionamentos do Motoboy
    Motoboy --> UC5
    Motoboy --> UC6
    Motoboy --> UC7
    Motoboy --> UC10
    
    %% Dependências (Includes/Excludes lógicos)
    UC3 -. "Requer (include)" .-> UC5
    UC6 -. "Disparado por" .-> UC3
```

## 2. Regras de Negócio Refinadas (Business Rules)

*   **RN-004 (Rastreamento):** A localização do motoboy deve ser atualizada em intervalos de aproximadamente 20 segundos para poupar bateria e dados, sendo suficiente para o controle logístico visual.
*   **RN-005 (Atribuição Compulsória):** O motoboy não pode rejeitar uma rota atribuída. A atribuição é compulsória, pois tratam-se de frotas próprias da loja.
*   **RN-006 (Cálculo Financeiro):** O cálculo da distância para pagamento não considera a rota real dirigida, mas sim a *distância da primeira rota sugerida pela API de Mapas* do estabelecimento até a casa do cliente.
*   **RN-007 (Status de Falha):** Caso o motoboy não consiga concluir a entrega (ex: cliente não atendeu), o sistema deve permitir o registro de "Falha na Entrega".

## 3. Épicos e Histórias de Usuário

### Épico 1: Despacho Visual Inteligente
Focado na experiência do Operador no Web App (BFF).

*   **US-01: Visualização Numérica no Mapa**
    *   **Como** operador, **eu quero** ver as entregas pendentes como pinos numerados em um mapa, com uma barra lateral detalhando cada número (Nome, Endereço, Valor, Itens), **para que** eu consiga visualizar geograficamente onde cada pedido está indo.
*   **US-02: Agrupamento e Despacho**
    *   **Como** operador, **eu quero** selecionar vários pinos no mapa e clicar em "Despachar", visualizando em seguida uma lista de motoboys ativos, **para que** eu possa otimizar as viagens mandando entregas próximas juntas.
    *   **Critérios de Aceite (BDD):**
        *   `Dado que` o operador selecionou as entregas 1, 2 e 5 no mapa
        *   `Quando` ele clicar no botão "Despachar"
        *   `Então` o sistema deve abrir um modal listando apenas os motoboys que estão com o status "Online/Disponível" no aplicativo.

### Épico 2: Operação Mobile em Campo
Focado na experiência do Motoboy no App Flutter.

*   **US-03: Ficar Online**
    *   **Como** motoboy, **eu quero** alternar meu status para "Disponível", **para que** o operador saiba que estou pronto para receber rotas.
*   **US-04: Gestão do Pedido Recebido**
    *   **Como** motoboy, **eu quero** receber os detalhes da entrega compulsoriamente e ter botões rápidos para notificar "Entregue" ou "Falha (Cliente não atendeu)", **para que** eu informe o backoffice sem precisar ligar.
    *   **Critérios de Aceite (BDD):**
        *   `Dado que` o motoboy chegou ao endereço e o cliente sumiu
        *   `Quando` ele clicar em "Falha na Entrega"
        *   `Então` o status da entrega atualiza no backoffice e o motoboy fica livre para a próxima entrega da sua rota agrupada.

### Épico 3 (Nova Feature): Comunicação Interna (Chat)
*   **US-05: Chat Integrado**
    *   **Como** operador e motoboy, **eu quero** um chat integrado na aplicação, **para que** possamos resolver problemas rápidos sem depender do WhatsApp, mantendo o histórico oficial vinculado à entrega.
    *   *Nota Arquitetural (Para a Skill de Arquitetura): Será necessário prever uso de WebSockets (ex: Socket.io ou SignalR).*
