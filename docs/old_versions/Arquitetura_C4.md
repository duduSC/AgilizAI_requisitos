# Documentação Arquitetural (C4 Model) - Agiliza Delivery

Este documento detalha a arquitetura do ecossistema "Agiliza Delivery" utilizando a abordagem C4 Model, focando nos Níveis 1 (Contexto) e 2 (Container).

---

## Nível 1: Diagrama de Contexto
O diagrama de contexto mostra a visão de alto nível do sistema, identificando os atores (usuários) e os sistemas externos com os quais o Agiliza Delivery interage.

```mermaid
flowchart TD
    %% Estilos Padrão C4
    classDef person fill:#08427b,stroke:#052e56,color:#fff
    classDef system fill:#1168bd,stroke:#0b4884,color:#fff
    classDef external fill:#999999,stroke:#6b6b6b,color:#fff
    
    %% Nodos
    usuario("🧑 Usuário Web<br/>[Person]<br/><br/>Gestor ou Operador do estabelecimento<br/>que gerencia as entregas."):::person
    
    agiliza("📦 Agiliza Delivery<br/>[System]<br/><br/>Plataforma central de despacho,<br/>logística e acerto financeiro."):::system
    
    motoboy("🛵 Motoboy<br/>[Person]<br/><br/>Entregador da frota própria<br/>do restaurante."):::person
    ifood("🍔 API iFood<br/>[External System]<br/><br/>Marketplace de onde os pedidos<br/>são importados."):::external
    
    waze("📍 Waze / Maps<br/>[External System]"):::external
    whatsapp("💬 WhatsApp<br/>[External System]"):::external
    
    %% Linha do usuario web até agiliza por cima
    usuario -- "Despacha pedidos<br/>[HTTPS]" --> agiliza
    
    %% Linha do agiliza até motoboy por baixo
    agiliza -- "Atribui rotas<br/>[HTTPS]" --> motoboy
    
    %% Linha da api ifood até agiliza delivery por baixo (A seta sobe do ifood pro agiliza)
    ifood -- "Envia pedidos<br/>[HTTPS/REST]" --> agiliza
    
    %% Outros
    motoboy -- "Abre rota" --> waze
    motoboy -- "Abre chat" --> whatsapp
```

---

## Nível 2: Diagrama de Container
Este nível abre a caixa do "Agiliza Delivery" e detalha as tecnologias de software que compõem o sistema. O sistema foi dividido para respeitar as restrições arquiteturais (Backend Jakarta EE/Quarkus) e a separação de Frontends (SPA e Mobile).

```mermaid
flowchart TD
    %% Estilos Padrão C4
    classDef person fill:#08427b,stroke:#052e56,color:#fff
    classDef container fill:#438dd5,stroke:#2e6295,color:#fff
    classDef database fill:#438dd5,stroke:#2e6295,color:#fff
    classDef external fill:#999999,stroke:#6b6b6b,color:#fff
    classDef boundary fill:none,stroke:#444,stroke-width:2px,stroke-dasharray: 5 5

    %% Atores e Sistemas Externos
    usuario("🧑 Usuário Web<br/>[Person]"):::person
    motoboy("🛵 Motoboy<br/>[Person]"):::person
    ifood("🍔 API iFood<br/>[External System]"):::external
    
    subgraph c1 ["📦 Ecossistema Agiliza Delivery"]
        direction TD
        spa("🖥️ SPA (BFF)<br/>[Container: React/Vue]<br/><br/>Painel web interativo de despacho."):::container
        mobile("📱 App Motoboy<br/>[Container: Flutter]<br/><br/>App que recebe corridas e rastreia."):::container
        backend("⚙️ API Core<br/>[Container: Quarkus]<br/><br/>Regras de negócio, workers e WebSockets."):::container
        db[("🗄️ Banco de Dados<br/>[Container: PostgreSQL]<br/><br/>Armazena usuários, motoboys e histórico.")]:::database
    end
    class c1 boundary
    
    %% Relacionamentos Top-Down
    usuario -- "Despacha pedidos<br/>[HTTPS]" --> spa
    motoboy -- "Usa App<br/>[Touch]" --> mobile
    ifood -- "Polling<br/>[HTTPS]" --> backend
    
    spa -- "Consome endpoints<br/>[JSON/WSS]" --> backend
    mobile -- "Envia GPS/Status<br/>[JSON/WSS]" --> backend
    
    backend -- "Lê/Escreve<br/>[JDBC/JPA]" --> db
```

---

## Resumo Arquitetural
* **Frontend Web:** Totalmente isolado do Backend. Consome a API Restful para desenhar o Mapa.
* **Aplicativo Mobile:** Consome a mesma API Restful que o Frontend Web.
* **Backend:** É a única ponte com o Banco de Dados. Ele gerencia o acesso simultâneo de múltiplos motoboys e faz o trabalho em *background* de puxar os dados do iFood a cada 30 segundos.
