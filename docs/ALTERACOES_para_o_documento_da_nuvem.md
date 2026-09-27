# Roteiro de alterações — da v2.0 (nuvem) para a v2.1

**Documento de destino:** `DVP_Agiliza_Delivery_versao_final_nuvem.docx` (sua cópia no Google Docs)
**Documento de origem:** `DVP_Agiliza_Delivery_v2.1.docx` / `DVP_Agiliza_Delivery_v2.1.pdf`

Verificado: o arquivo da nuvem é a v2.0 sem nenhuma edição posterior. Não há nada nele que precise ser preservado — tudo o que ele tem já está na v2.1.

As referências "v2.1 §X (p. N)" apontam a seção e a página no PDF da v2.1, de onde você copia o bloco pronto.

---

## ⚠ Antes de colar qualquer coisa: como a numeração funciona

No seu documento da nuvem, **os números dos títulos não são texto** — são gerados automaticamente. Todos os títulos usam o mesmo estilo (`Heading1`) e a hierarquia vem do nível de lista (`ilvl` 0, 1, 2, 3) sobre uma lista multinível compartilhada. É o mesmo esquema do template da UPF, que usa `Título 1` com a lista `numId=9`.

Na v2.1 os números são **texto literal** ("1.2.3. Escopo do Produto"), porque o pandoc não reproduz lista multinível.

**Consequência prática:** se você colar direto, vai ficar com numeração dobrada — "1.2.3. 1.2.3. Escopo do Produto".

Ao colar cada título novo:
1. apague o número literal do começo (`1.2.3. `), deixando só o texto;
2. aplique o estilo de título do seu documento;
3. ajuste o nível com **Tab / Shift+Tab** (nível 1 = seção, 2 = subseção, 3 = sub-subseção).

Para o corpo do texto, cole com **Ctrl+Shift+V** (colar sem formatação) e depois aplique os estilos do documento — senão você traz junto os estilos do pandoc e reintroduz a bagunça que fez o arquivo não bater com o template.

---

## Resumo

| | Quantidade |
| ----- | :---: |
| Seções inteiramente novas | 8 |
| Blocos a substituir | 7 |
| Edições pontuais de texto | 19 |
| Imagens a trocar | 2 |

---

## A. Abertura

### A1. Histórico de alterações — ADICIONAR LINHA

Acrescente uma quarta linha na tabela:

| 2.1 | Revisão técnica: stack padronizada em Spring Boot; inclusão de escopo, premissas, restrições, riscos e glossário; descrição dos casos de uso; matriz de rastreabilidade; máquina de estados; definição da regra de precificação; reformulação do modelo lógico do banco de dados | Eduardo S.C | 16/09/2026 |

### A2. Sumário — REGERAR NO FINAL

Deixe por último. No Google Docs: clique no sumário → ícone de atualizar. No Word: Ctrl+A, F9.

---

## B. Seção 1.2 — Concepção dos Requisitos

### B1. §1.2.2 Principais Stakeholders — SUBSTITUIR A TABELA INTEIRA

**Está assim (3 linhas):** Gestor/Dono · Operador de Caixa · Motoboy

**Passa a ser (5 linhas):**

| Nome do Stakeholder | Responsabilidade | Contato |
| ----- | ----- | ----- |
| Administrador Geral | Dono da plataforma. Cadastra, ativa e inativa restaurantes parceiros; patrocinador do produto. | [a preencher] |
| Administrador do Restaurante | Gestor/dono da loja. Define métricas financeiras, cadastra entregadores e configura a tabela de preços. | [a preencher] |
| Operador de Logística | Agrupa entregas visualmente, despacha lotes e fecha o acerto financeiro do turno. | [a preencher] |
| Entregador | Executa as entregas em campo via aplicativo e reporta o status de cada etapa. | [a preencher] |
| Sistema Externo (iFood) | Ator de sistema. Origem automática dos pedidos consumidos pela plataforma. | Portal do Desenvolvedor iFood |

Motivo: os nomes da tabela não batiam com os atores do diagrama de casos de uso ("Operador de Caixa" vs. "Operador de Logística", "Motoboy" vs. "Entregador"), e dois atores do diagrama nem apareciam aqui.

Logo abaixo da tabela, inclua a nota:

> **Nota de padronização:** os nomes acima são os mesmos utilizados no diagrama de casos de uso (seção 1.4.1) e nas histórias de usuário (seção 1.4.3). O termo "motoboy", usado coloquialmente, corresponde ao ator **Entregador**.

### B2. INSERIR 5 SEÇÕES NOVAS depois de Principais Stakeholders

Nesta ordem, antes de "1.3 Elicitação dos Requisitos":

| Nova seção | Copiar de | Conteúdo |
| ----- | ----- | ----- |
| 1.2.3 Objetivos do Produto e Métricas de Sucesso | v2.1 §1.2.3 (p. 4) | tabela de 5 métricas com linha de base e meta |
| 1.2.4 Escopo do Produto | v2.1 §1.2.4 (p. 4) | dentro do escopo (6 itens) e **fora do escopo** (7 itens) |
| 1.2.5 Premissas e Restrições | v2.1 §1.2.5 (p. 5) | 5 premissas e 4 restrições |
| 1.2.6 Riscos do Projeto | v2.1 §1.2.6 (p. 6) | tabela R01–R07 com probabilidade, impacto e mitigação |
| 1.2.7 Glossário | v2.1 §1.2.7 (p. 7) | 11 termos, padronizando "lote de entrega" |

---

## C. Seção 1.3 — Elicitação dos Requisitos

### C1. Requisitos funcionais — EDIÇÕES PONTUAIS

**RF01** — na descrição, troque `(ex: integração iFood)` por `(integração com provedor externo)` e `agrupamento de múltiplos pedidos em uma única corrida (rota)` por `agrupamento de múltiplos pedidos em um único lote`. Ao final, `e o registro de tempos operacionais` vira `e o registro dos tempos operacionais de cada etapa`.

**RF02** — troque `notificações de corridas, visualizar rotas e detalhes` por `notificações de lotes, visualizar as entregas e seus detalhes`; `atualizar o status do pedido (etapas logísticas)` por `atualizar o status de cada entrega`.

**RF03** — dependência: de `Nenhuma` para `RF01, RF06`. Substitua a descrição por:

> *O sistema mantém uma tabela de faixas de preço por distância e calcula automaticamente o valor devido ao entregador a cada entrega concluída, culminando na geração de recibos para o acerto financeiro do turno e eliminando os erros do cálculo manual em planilha.*

**RF04 — CORREÇÃO IMPORTANTE.** Hoje está marcado como prioridade **1 e 3 ao mesmo tempo**, e é o único classificado como "importante" embora esteja no MVP.
- Importância: desmarque `importante`, marque `essencial`
- Priorização: desmarque o 1 e o 3, marque apenas o **2**
- Descrição: acrescente `com histórico persistido para auditoria` depois de `em segundo plano`

**RF05** — dependência: de `Nenhuma` para `RF06`. Na descrição, `permitindo o CRUD de entregadores` vira `permitindo o CRUD de entregadores pelo Administrador do Restaurante`, e substitua `parametrizações gerais do sistema e extração de relatórios gerenciais essenciais` por:

> *e a parametrização operacional da loja (limite de pedidos por lote e faixas de preço). A extração de relatórios analíticos está fora do escopo do MVP, conforme a seção 1.2.4.*

Motivo: "relatórios gerenciais" era um requisito órfão — não existia nenhum caso de uso nem história cobrindo isso.

**RF06** — sem alteração.

### C2. §1.3.2 Requisitos Não-Funcionais — SUBSTITUIR A TABELA INTEIRA

De 5 para 13 RNFs, agora com coluna **Categoria**. Copiar de **v2.1 §1.3.2 (p. 10)**.

O que muda nos que já existiam:
- RNF01 ganha o envio em lotes de até 5 posições
- RNF02 especifica BCrypt com fator ≥ 10
- RNF03 era dois requisitos numa linha só (resiliência + tempo de resposta); virou RNF03 (desempenho, p95) e RNF04 (resiliência com backoff)
- RNF05 (antigo RNF04) troca "Presentation" por "Controller (REST)", que é o correto com SPA + API
- RNF06 (antigo RNF05) ganha o limite de 5 segundos de propagação

Novos: RNF07 LGPD · RNF08 disponibilidade · RNF09 operação offline · RNF10 Android 8.0+ · RNF11 usabilidade · RNF12 escalabilidade · RNF13 auditabilidade.

---

## D. Seção 1.4 — Especificação dos Requisitos

### D1. §1.4.1 Diagrama de Casos de Uso — TROCAR A IMAGEM

Arquivo novo: **`docs/img/uc-casos-de-uso.png`**

O diagrama atual tem dois erros: dois casos de uso numerados **UC06** (o "Configurar Estabelecimento e Frota" é UC05 no texto) e o rótulo "Estabelecimento **a** Frota". Os atores também foram renomeados para bater com a tabela de stakeholders.

Depois da imagem, acrescente a tabela de atores — copiar de **v2.1 §1.4.1 (p. 13)**.

### D2. INSERIR §1.4.2 Descrição dos Casos de Uso

Seção nova inteira, antes das histórias de usuário. Seis tabelas (UC01 a UC06) com ator principal, pré-condições, fluxo principal, fluxos alternativos, fluxos de exceção e pós-condições.

Copiar de **v2.1 §1.4.2 (p. 14 a 16)**.

Motivo: uma versão anterior sua tinha essa seção e ela se perdeu. Se o template da disciplina pede fluxo principal e alternativo, a ausência conta contra.

### D3. Histórias de Usuário — RENUMERAR E EDITAR

A seção passa de **1.4.2** para **1.4.3** (por causa da inserção acima).

**Títulos de caso de uso a corrigir:**
- `UC02 Executar Rota de Entrega` → `UC02 – Executar Lote de Entrega`
- `UC04 Monitoramento de Logística em Tempo Real` → `UC04 – Monitorar Logística em Tempo Real`

**Histórias com alteração** (copiar o texto pronto de **v2.1 §1.4.3, p. 17 a 19**):

| História | O que muda |
| ----- | ----- |
| HU01 | "Planejar rotas via mapa" → "Planejar **lotes** via mapa"; regra ganha o tratamento de entregas sem coordenada |
| HU02 | limite de 5 pedidos vira "o limite configurado no estabelecimento (padrão: 5)"; exige cadastro ATIVO além de ONLINE |
| HU03 | reescrita: acrescenta a **regra de idempotência** (par provedor + identificador externo é único, para o polling de 30 s não duplicar pedido) e a lista de dados importados |
| HU04 | sem alteração de conteúdo |
| HU05 | reescrita: remete à máquina de estados, exige motivo na falha e trata operação sem conexão |
| HU06 | **reescrita completa** — ver item E1 abaixo |
| HU07 | acrescenta que a entrega não pode entrar em dois recibos e o que o recibo registra |
| HU08 | acrescenta que a coleta cessa quando OFFLINE e a retenção de 90 dias |
| HU09 | acrescenta que o cadastro **gera automaticamente um usuário** com perfil ENTREGADOR (antes o motoboy não tinha como fazer login) e que o CPF é criptografado |
| HU10 | acrescenta distância inicial e final por faixa, tabela por estabelecimento, e que alterar preço **não recalcula** entregas já finalizadas |
| HU11 | corrigir o erro de digitação `Estabelecimento lParceiro` → `Estabelecimento Parceiro` |
| HU12 | acrescenta que o worker de integração para de consultar o provedor da loja inativa |

### D4. INSERIR §1.4.4 Máquina de Estados dos Objetos de Negócio

Seção nova. Define formalmente todos os status citados nas histórias (AGUARDANDO_DESPACHO, EM_ROTA, ENTREGUE, FALHA, ONLINE, BLOQUEADO...), que hoje aparecem no texto sem estar definidos em lugar nenhum.

Copiar de **v2.1 §1.4.4 (p. 20)**.

### D5. INSERIR §1.4.5 Matriz de Rastreabilidade

Seção nova. Tabela ligando RF ↔ Caso de Uso ↔ Histórias ↔ RNF ↔ entidades do banco.

Copiar de **v2.1 §1.4.5 (p. 21)**.

---

## E. Seção 1.5 — Projeto Técnico

### E1. §1.5.1 Arquitetura Utilizada — SUBSTITUIR O BLOCO INTEIRO

**Está assim:**

> *O sistema utiliza a arquitetura em camadas para o Backend e um SPA para o Frontend (BFF):*
> - ***Frontend SPA (BFF):** Interface Web separada... (Substituindo o antigo JSF).*
> - ***Service (CDI) / REST:** ...*
> - ***Repository (JPA/EntityManager):** ...*
> - ***Entity (JPA):** ...*
> - ***Integração Externa:** Worker...*

**Três problemas:** "BFF" está usado errado (um SPA React não é um Backend For Frontend); "(Substituindo o antigo JSF)" é comentário de histórico interno que não pertence ao documento final; e "CDI" é Jakarta EE/Quarkus — em Spring seria `@Service`.

**Substituir por** o bloco de 9 camadas de **v2.1 §1.5.1 (p. 22)**, que descreve Controller (Spring Web) · Service · Repository (Spring Data JPA) · Entity · Integração (Spring Scheduler + Adapter) · Tempo real (Spring WebSocket/STOMP) · Segurança (Spring Security + JWT).

### E2. §1.5.2 Ferramentas e Tecnologias — SUBSTITUIR A TABELA

**Está assim:** Java Spring / React / Flutter / PostgreSQL / Maven, todos com versão "Latest".

**Passa a ser:**

| Descrição | Versão | Objetivo |
| ----- | ----- | ----- |
| Java | 21 LTS | Linguagem do backend |
| Spring Boot | 3.x | Plataforma de backend (Web, Data JPA, Security, WebSocket, Scheduler) |
| React | 18.x | Aplicação Web do operador e dos administradores (SPA) |
| Flutter | 3.x | Aplicativo do entregador (Android) |
| PostgreSQL | 16.x | Armazenamento persistente de dados |
| Maven | 3.9.x | Gestão de dependências e build |
| Flyway | 10.x | Versionamento e migração do esquema do banco |
| Leaflet + OpenStreetMap | Latest | Renderização de mapas no painel de despacho |
| JWT (jjwt) | Latest | Tokens de autenticação |
| Docker | Latest | Padronização do ambiente de execução |

### E3. §1.5.3 Modelo Lógico do Banco de Dados — TROCAR A IMAGEM

Arquivo novo: **`docs/img/der-modelo-logico.png`**

De 5 para 12 tabelas. O que faltava:

| Problema no modelo atual | Correção |
| ----- | ----- |
| Não existe tabela de restaurante, embora RF06/HU11/HU12 exijam multilocação com CNPJ único e isolamento de dados | Nova **ESTABELECIMENTO**, referenciada por todas as entidades operacionais |
| Nada do pedido do iFood é armazenado, e o polling de 30 s duplicaria pedidos | Novas **PEDIDO_EXTERNO** (com `UNIQUE (provedor, id_externo)`, itens, valor, forma de pagamento, `pago_online`, troco e o JSON bruto) e **PEDIDO_EXTERNO_ITEM** |
| HU07 exige recibo, mas não há entidade para ele | Nova **RECIBO** |
| MOTOBOY não tem login, mas HU09 diz que o entregador loga no app | `usuario_id` ligando MOTOBOY a USUARIO |
| USUARIO não tem perfil, mas RF05 depende de 4 perfis | Coluna `perfil` e `ativo` |
| Só a última posição de GPS é guardada | Nova **POSICAO_GPS** com histórico |
| Só `entregue_em`, mas RF01 promete "tempos operacionais" | Timestamps por etapa + **ENTREGA_STATUS_HISTORICO** |
| DISTANCIA_PRECO só tem `ate_km`, impossível validar sobreposição (HU10) | `de_km`, `estabelecimento_id`, `ativo`, `vigente_desde` |
| `lat_lng` como texto único | `latitude` e `longitude` decimais separados |

Acrescente também o parágrafo introdutório de **v2.1 §1.5.3 (p. 23)**.

### E4. INSERIR §1.5.4 Dicionário de Dados

Seção nova e longa: uma tabela por entidade, com coluna, tipo, restrições e descrição.

Copiar de **v2.1 §1.5.4 (p. 25 a 31)**.

### E5. INSERIR §1.5.5 Regra de Precificação e Cálculo do Repasse

Seção nova. Resolve a ambiguidade mais séria do documento: HU06 dizia "distância linear **ou** configurada", a tabela DISTANCIA_PRECO sugeria faixa fixa e o campo `valor_km_aplicado` sugeria preço por quilômetro — três regras diferentes.

**Regra definida:** valor apurado **por entrega** (não por lote); cada entrega recebe o valor da faixa correspondente à distância loja → cliente; o total do lote é a soma; entrega com **falha paga integral**; a faixa é congelada quando a entrega atinge estado final.

Copiar de **v2.1 §1.5.5 (p. 32)**, que traz o algoritmo em 6 passos e o exemplo numérico.

### E6. INSERIR §1.5.6 Integração com Provedores de Pedidos

Seção nova. Descreve a interface `ProvedorDePedidos` com dois adaptadores (`IFoodAdapter` e `SimuladorAdapter`), o ciclo do worker em 6 passos e a tabela de dados capturados com sua finalidade.

Copiar de **v2.1 §1.5.6 (p. 33)**.

Motivo: o acesso à API do iFood depende de homologação comercial que pode não sair no prazo. O adaptador com simulador é o que impede o projeto inteiro de travar na Entrega 3.

---

## F. Seção 2 — Gestão de Projetos

### F1. §2.1 MVP — CORRIGIR A STACK

Primeiro item: `Integração Base (Quarkus/Worker)` → `Integração base (Spring Scheduler + Adapter)`, acrescentando `com simulador como alternativa de contingência`.

Segundo item: `Painel de Despacho (React/BFF)` → `Painel de despacho (React)`.

Quarto item: `Cálculo automático do valor de repasse baseado no fechamento da rota` → `Cálculo automático do repasse por faixa de distância`.

### F2. §2.2 Cronograma — PREENCHER AS DATAS E CORRIGIR

A coluna DATA está inteira com `?`. Entregas semanais às sextas, começando em 21/09/2026:

| Data | Entrega |
| :---: | ----- |
| 25/09/2026 | Entrega 1 – Setup e infraestrutura base |
| 02/10/2026 | Entrega 2 – Autenticação e perfis (API) |
| 09/10/2026 | Entrega 3 – Integração e *worker* de pedidos |
| 16/10/2026 | Entrega 4 – Painel de retaguarda (React) |
| 23/10/2026 | Entrega 5 – Aplicativo do entregador (Flutter) |
| 30/10/2026 | Entrega 6 – Mapa, WebSocket e despacho |
| 06/11/2026 | Entrega 7 – Telemetria GPS e status em campo |
| 13/11/2026 | Entrega 8 – Acerto financeiro e fechamento do MVP |
| 20/11/2026 | **Entrega 9 – Testes, documentação e apresentação** (linha nova) |

Na Entrega 1, `projeto Quarkus` → `projeto Spring Boot`, acrescentando as migrações Flyway. Na Entrega 3, `Worker no back-end para consumir a API externa` → a descrição da v2.1, que cita a interface e o simulador. Na Entrega 4, tirar `(BFF)`.

A tabela também tem um defeito estrutural: o cabeçalho declara 3 colunas mas só nomeia 2 (DATA e ENTREGA, com a terceira sem título). Nomeie a terceira como **Descrição**.

---

## G. Pendências que continuam em aberto

Três coisas que preenchi por estimativa e que só você pode confirmar:

1. **Linha de base das métricas** (§1.2.3): "~8 min" para despacho e "~30 min" para o acerto em planilha são estimativas minhas a partir da narrativa do documento, apresentadas como situação atual medida. Se você não mediu, troque por "não medido".
2. **Volumetria do RNF12** (50 lojas, 200 entregadores, 2.000 entregas/dia) e os 99% de disponibilidade do RNF08 — valores plausíveis que escolhi, mas são metas suas.
3. **Contatos dos stakeholders** — deixei `[a preencher]`; não inventei nomes nem e-mails.
