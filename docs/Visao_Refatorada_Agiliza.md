# Documento de Visão (Refatorado) - Plataforma "Agiliza Delivery"

---

## 1. Introdução

### 1.1 Propósito do documento
O propósito deste documento é fornecer uma visão clara, executiva e de alto nível sobre a evolução da plataforma "Agiliza Delivery". Ele estabelece as fronteiras do sistema, delineando a transição de um modelo monolítico para um ecossistema distribuído focado na gestão visual de entregadores (BFF Web) e na operação em campo via aplicativo móvel (Flutter).

### 1.2 Escopo do produto
O **Agiliza Delivery** é uma plataforma que atua como o sistema nervoso central da logística de entregas de frota própria.
**O sistema irá:**
*   Prover um "Painel de Controle Visual" (Mapa) para agrupamento e despacho de entregas.
*   Integrar os operadores de caixa aos motoboys em campo por meio de um aplicativo móvel impositivo (o motoboy não pode recusar a entrega atribuída).
*   Monitorar a posição da frota em tempo real (intervalos de 20s).
*   Automatizar o fechamento de caixa, calculando o valor de repasse ao entregador utilizando como base a quilometragem da *primeira rota ideal* fornecida por uma API de Mapas externa, e não a rota física efetivamente traçada.
*   Prover comunicação instantânea (Chat) para resolução de conflitos em campo (ex: cliente ausente).

**O sistema não irá (Fora do Escopo):**
*   Substituir um ERP ou gerenciar o fluxo de produção da cozinha.
*   Processar pagamentos eletrônicos via gateway (PIX, cartão) de repasse final para o motoboy. Ele gera apenas o cálculo financeiro para acerto de caixa.
*   Permitir que o cliente final rastreie a pizza pelo mapa.

---

## 2. Posicionamento

### 2.1 Declaração do problema
| Campo | Descrição |
|---|---|
| **O problema da** | gestão invisível da frota e do acerto financeiro manual e empírico de quilometragem |
| **Afeta** | donos de restaurantes com frota própria e operadores de caixa/expedição |
| **Cujo impacto é** | entregas ociosas na estufa por falha no agrupamento de destinos próximos, desconfiança e atritos no cálculo do pagamento do entregador, e impossibilidade de contato rápido durante incidentes em rota. |
| **Uma solução adequada seria** | um ecossistema descentralizado onde o operador agrupa visualmente as entregas em um mapa e as despacha diretamente para o smartphone do entregador, com cálculo de valores garantidos por APIs de mapas neutras, além de chat integrado para suporte instantâneo. |

### 2.2 Declaração de posição do produto
*   **Para** operações de food service com frotas de motoboys próprias
*   **Que** precisam despachar alto volume de entregas simultâneas e garantir agilidade no caixa
*   **O** Agiliza Delivery
*   **É** uma plataforma híbrida de logística e conciliação financeira
*   **Que** transforma o despacho cego em roteirização visual e automatiza a precificação por trecho ideal.
*   **Diferente de** soluções paliativas baseadas em planilhas ou sistemas monolíticos pesados sem visão de campo
*   **Nosso produto** coloca o gestor com controle em tempo real da rua, unificando comunicação e fechamento do turno de forma inquestionável.

---

## 3. Perfis das Partes Interessadas (Stakeholders) e Usuários

| Papel | Descrição / Interesse |
|---|---|
| **Dono/Gestor** | Patrocinador da ferramenta. Quer eliminar erros matemáticos no pagamento de diárias/rotas e reduzir o custo fixo de entregas mal otimizadas. |
| **Operador (Despachante)** | Usuário primário do Backoffice (Web). Quer uma interface rápida, baseada em mapa, que não exija digitar endereços manualmente, mas sim "clicar e despachar". |
| **Motoboy (Frota Própria)** | Usuário do aplicativo móvel (Flutter). Deseja saber exatamente quanto vai receber por cada corrida (via regra transparente de API), quer botões de acesso rápido ao Waze e não quer usar seu WhatsApp pessoal para discutir com o operador se o cliente não atender. |

---

## 4. Suposições e Dependências Críticas

*   **Infraestrutura de Nuvem:** Espera-se que a camada Backend possua conectividade ininterrupta e consiga gerenciar chamadas massivas concorrentes (WebSockets para Chat e Polling de GPS).
*   **Dependência de APIs de Terceiros:** A "Verdade Financeira" do sistema depende da robustez da API de Geocodificação/Rotas (Google Maps, OpenStreetMap ou similar) para retornar a distância ideal da viagem sem interrupções.
*   **Hardware (Motoboys):** Assume-se que os motoboys estarão utilizando dispositivos móveis Android/iOS com GPS ativado e pacote de dados com cobertura satisfatória ao longo da jornada.

---

## 5. Dimensões de Qualidade (Trade-offs)
O projeto valoriza fortemente a **Usabilidade (BFF)** e a **Confiabilidade Matemática** no backoffice. Entretanto, para garantir a viabilidade da bateria do smartphone do motoboy, abre-se mão da **Precisão Extrema de Rastreador** (streaming de GPS em milissegundos), optando por um modelo assíncrono e leve (atualizações a cada 20 segundos), suficiente para a consciência situacional do Operador.
