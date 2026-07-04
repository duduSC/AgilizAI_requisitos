# Levantamento de Requisitos - Gerenciamento de Delivery e Motoboys

Com base nas definições de negócio levantadas, o sistema evoluiu para uma arquitetura distribuída e os requisitos foram refatorados para maior clareza.

## 1. Diagrama de Casos de Uso (Visão Geral)

```mermaid
usecaseDiagram
    actor Operador as "Operador (Backoffice)"
    actor Motoboy as "Motoboy (Mobile)"
    
    package "Backoffice Web" {
        usecase UC1 as "Visualizar Mapa de Entregas"
        usecase UC2 as "Agrupar Entregas (Teles)"
        usecase UC3 as "Despachar Entregas"
        usecase UC4 as "Acompanhar Motoboys (20s)"
        usecase UC8 as "Gerar Fechamento Financeiro"
        usecase UC9 as "Comunicar via Chat Interno"
    }
    
    package "App Mobile (Flutter)" {
        usecase UC5 as "Ficar Disponível (Online)"
        usecase UC6 as "Receber Nova Rota"
        usecase UC7 as "Marcar Status (Entregue/Falhou)"
        usecase UC10 as "Comunicar com Backoffice"
    }
    
    Operador --> UC1
    Operador --> UC2
    Operador --> UC3
    Operador --> UC4
    Operador --> UC8
    Operador --> UC9
    
    Motoboy --> UC5
    Motoboy --> UC6
    Motoboy --> UC7
    Motoboy --> UC10
    
    UC3 ..> UC5 : "Requer Motoboy Disponível"
    UC6 ..> UC3 : "Acionado por"
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
