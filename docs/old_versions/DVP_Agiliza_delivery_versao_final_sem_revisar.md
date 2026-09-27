Universidade de Passo Fundo – UPF







DOCUMENTO DE VISÃO DO PRODUTO - DVP 



AGILIZA DELIVERY





Eduardo dos Santos de Camargo
2026


Histórico de alterações do documento
Versão
Alteração efetuada
Responsável
Data
1.0
Criação do DVP
Eduardo S.C
04/08/2026
1.5
Finalização do DVP
Eduardo S.C
12/08/2026






















Sumário
 TOC \h \u \z \t "Heading 1,1,Heading 2,2,Heading 3,3,Heading 4,4,Heading 5,5,Heading 6,6,"1. PAGEREF _vatsrsm8ce8a \h REQUISITOS3
1.1. PAGEREF _nitcwps04ewy \h Fundamentação dos Requisitos3
1.1.1. PAGEREF _4clbmboqi1yl \h Técnicas Utilizadas para Requisitos3
1.2. PAGEREF _exr1er7geg3 \h Concepção dos Requisitos3
1.2.1. PAGEREF _uijn2spz1qum \h Identificação do Domínio3
1.2.2. PAGEREF _vekvwj7fu9zb \h Principais Stakeholders3
1.3. PAGEREF _vm0zbyuv43gj \h Elicitação dos Requisitos3
1.3.1. PAGEREF _vckr0d5olu5i \h Requisitos Funcionais (RF)3
1.3.1.1. PAGEREF _hnh171e6ixmh \h RF01 Gerenciar Login3
1.3.2. PAGEREF _ac2qfzivw58w \h Requisitos Não-Funcionais (RNF)4
1.4. PAGEREF _y4fkg21727f7 \h Especificação dos Requisitos4
1.4.1. PAGEREF _ejhpoz48u1wh \h UML – Diagrama de Casos de Uso4
1.4.2. PAGEREF _d99uukgcl1w3 \h Histórias de Usuário Por Caso de Uso5
1.4.2.1. PAGEREF _lsyl5lec4jal \h UC01 Gerenciar Login5
1.5. PAGEREF _r077vti6kma3 \h Projeto Técnico6
1.5.1. PAGEREF _2xqaprqcucg9 \h Tecnologias e Ferramentas6
1.5.2. PAGEREF _na0cwc7d2982 \h Modelo Lógico do Banco de Dados6


REQUISITOS
Fundamentação dos Requisitos
Técnicas Utilizadas para Requisitos
Entrevistas e reuniões com stakeholders (Gestores de Restaurantes).
Análise de Documentos (Planilhas de acerto financeiro atuais).
Brainstorming para definição de arquitetura de integração (iFood).
Prototipação conceitual (User Stories / Casos de Uso).
Concepção dos Requisitos
Identificação do Domínio
O **Agiliza Delivery** é uma plataforma que atua como o sistema nervoso central da logística de entregas para restaurantes com frota própria. O problema atual é a gestão "cega" da frota, o acerto financeiro manual e empírico de quilometragem, e a perda de tempo na digitação e agrupamento de pedidos.
A plataforma propõe um ecossistema descentralizado composto por: um aplicativo móvel impositivo (Flutter) para motoboys (rastreamento e marcação de status), um Backoffice Web para o operador realizar despacho visual via mapa, e um Backend focado em integrações automáticas de pedidos (ex: API do iFood) e cálculo da precificação baseada na quilometragem ideal.
Principais Stakeholders
STAKEHOLDER
Nome do Stakeholder
Responsabilidade
Contato
Gestor/Dono
Patrocinador, define métricas financeiras e aprova integrações.

Operador de Caixa
Agrupa entregas visualmente e despacha pedidos.

Motoboy
Executa entregas em campo via app e reporta status.


Elicitação dos Requisitos 
Requisitos Funcionais (RF)
RF01 Gestão Operacional de Despacho (Web)
Importância:
[ X ] essencial       [   ] importante       [    ] desejável
Priorização:
[X] 1   [   ] 2   [   ] 3   [   ] 4    [   ] 5
Dependência com outro(s) requisito(s):
Nenhuma
Problema /Necessidades Identificadas:
Centraliza o recebimento automático de pedidos (ex: integração iFood), a visualização da localização dos clientes em mapa e o agrupamento de múltiplos pedidos em uma única corrida (rota), permitindo o despacho dinâmico para os entregadores e o registro de tempos operacionais.

RF02 Operação e Interação do Entregador (Mobile)
Importância:
[ X ] essencial       [   ] importante       [    ] desejável
Priorização:
[ X] 1   [  ] 2   [   ] 3   [   ] 4    [   ] 5
Dependência com outro(s) requisito(s):
RF01
Problema /Necessidades Identificadas:
O aplicativo móvel torna-se o terminal de trabalho do motoboy, permitindo gerenciar disponibilidade, receber notificações de corridas, visualizar rotas e detalhes, acionar atalhos nativos (Waze/WhatsApp) e atualizar o status do pedido (etapas logísticas) em tempo real.






RF03 Gestão Financeira e Precificação (Web)
Importância:
[ X ] essencial       [   ] importante       [    ] desejável
Priorização:
[   ] 1   [  X  ] 2   [  ] 3   [   ] 4    [   ] 5
Dependência com outro(s) requisito(s):
Nenhuma
Problema /Necessidades Identificadas:
O sistema gerencia uma tabela de preços e calcula automaticamente o valor devido ao motoboy com base na soma das teles (entregas) realizadas e seus respectivos endereços, culminando na geração de recibos para o acerto financeiro do turno, evitando erros manuais.

RF04 Rastreamento e Telemetria de Frota (Mobile/Web)
Importância:
[  ] essencial       [  X  ] importante       [    ] desejável
Priorização:
[ X ] 1   [   ] 2   [ X ] 3   [  ] 4    [   ] 5
Dependência com outro(s) requisito(s):
RF02
Problema /Necessidades Identificadas:
Captura contínua da localização GPS do entregador em segundo plano, integrando ao painel Web para monitoramento da frota em tempo real no mapa.
RF05 Administração do Sistema e Segurança (Web)
Importância:
[ X ] essencial       [   ] importante       [    ] desejável
Priorização:
[  X  ] 1   [   ] 2   [  ] 3   [   ] 4    [   ] 5
Dependência com outro(s) requisito(s):
Nenhuma
Problema /Necessidades Identificadas:
Controla a autenticação e autorização de todos os usuários, permitindo o CRUD de entregadores, parametrizações gerais do sistema e extração de relatórios gerenciais essenciais.


RF06 Gestão de Restaurantes Parceiros (Web)
Importância:
[ X ] essencial       [   ] importante       [    ] desejável
Priorização:
[  X  ] 1   [   ] 2   [  ] 3   [   ] 4    [   ] 5
Dependência com outro(s) requisito(s):
Nenhuma
Problema /Necessidades Identificadas:
Permite que o sistema funcione para múltiplos clientes, gerindo o cadastro, ativação, bloqueio e isolamento de dados de cada restaurante parceiro na plataforma.


Requisitos Não-Funcionais (RNF)
Identificação
Descrição
RNF01
O app mobile deve atualizar a localização (GPS) a cada 20 segundos para economizar bateria e dados.
RNF02
Segurança: Dados sensíveis de motoboys (CPFs) e senhas devem ser criptografados no banco de dados.
RNF03
O sistema deve ter alta resiliência (Worker de polling) ao se comunicar com a API externa, além de garantir tempo de resposta na API interna de até 3 segundos.
RNF04
O código do backoffice deve seguir rigorosamente a arquitetura em camadas (Presentation, Service, Repository, Entity).
RNF05
A tela de despacho (Mapa) deve operar em tempo real, refletindo a localização via WebSockets.













Especificação dos Requisitos
UML – Diagrama de Casos de Uso
O UC apresentado abaixo apresenta todos casos de usos definidos para solução.








Histórias de Usuário Por Caso de Uso
UC01 Gerenciar Fluxo de Entregas
Objetivo:
Fornecer suporte tecnológico ao entregador na rua para encontrar a rota e reportar o andamento.

HISTÓRIAS DE USUÁRIOS

História:
HU01 Planejar rotas via mapa

Descrição:
COMO Operador de Logística, QUERO visualizar os novos pedidos distribuídos geograficamente em um mapa PARA planejar rapidamente roteiros inteligentes.

Regras de Negócio:
Apenas pedidos com status "Aguardando Despacho" devem aparecer no mapa.
 
Critérios de Aceite:
Dado que o operador selecionou os pedidos A e B no mapa
Quando  ele clicar em "Despachar" e selecionar o Motoboy João
Então os pinos devem sumir do mapa de pendentes e a rota deve aparecer no App do João.

História:
HU02 - Despachar múltiplos pedidos

Descrição:
COMO Operador de Logística, QUERO selecionar e agrupar múltiplos pedidos próximos em um mesmo despacho PARA otimizar o tempo e custo do entregador.

Regras de Negócio:
O motoboy destino deve estar com status "Online". Uma rota (lote) pode conter até 5 pedidos simultâneos.
 
Critérios de Aceite:
Dado que o operador selecionou os pedidos A e B no mapa
Quando  ele clicar em "Despachar" e selecionar o Motoboy João
Então os pinos devem sumir do mapa de pendentes e a rota deve aparecer no App do João.


História:
HU03 - Importar pedidos do iFood
Descrição:
COMO Sistema, DEVO importar os pedidos do iFood automaticamente PARA eliminar o gargalo de redigitação por parte do operador.

Regras de Negócio:
O sistema fará a captura (polling) a cada 30 segundos usando a API de integração oficial, garantindo que o endereço e itens sejam importados.
 
Critérios de Aceite:
Dado que o restaurante está online no iFood
Quando um cliente fizer e pagar um novo pedido
Então esse pedido aparecerá no painel "Aguardando Despacho" e no mapa do Agiliza Delivery sem intervenção manual.



UC02 Executar Rota de Entrega
Objetivo:
Fornecer suporte tecnológico ao entregador na rua para encontrar a rota e reportar o andamento.

HISTÓRIAS DE USUÁRIOS

História:
HU04 Atalhos nativos de GPS e Contato

Descrição:
COMO Entregador, QUERO abrir aplicativos de navegação (Waze/Maps) e o Whatsapp do cliente diretamente pelo app Agiliza PARA economizar tempo digitando na rua.

Regras de Negócio:
O aplicativo deve utilizar deep links para passar a localização exata ao GPS ou o número com a mensagem pronta para o WhatsApp.

Critérios de Aceite:
Dado que o entregador abriu a tela da entrega X
Quando ele tocar no botão "Navegar" ou "WhatsApp"
Então o aplicativo respectivo abrirá automaticamente já traçando a rota até o cliente ou abrindo a conversa com ele.



História:
HU05 Reportar andamento (Status)

Descrição:
COMO Entregador, QUERO alterar os status de cada etapa do pedido com poucos cliques PARA que a loja saiba do andamento em tempo real.

Regras de Negócio:
Se falhar (ex: cliente não atendeu), a rota de volta conta no fechamento. O status deve atualizar no Backoffice instantaneamente.

Critérios de Aceite:
Dado que o motoboy chegou ao local
Quando ele clicar em "Finalizar como Entregue" ou "Falha"
Então a entrega muda de status no painel web para que o operador seja notificado imediatamente.





UC03 Fechar Acerto Financeiro
Objetivo:
Automatizar e auditar o pagamento devido aos motoboys no encerramento de um período.

HISTÓRIAS DE USUÁRIOS

História:
HU06 Calcular preço de entrega automaticamente

Descrição:
COMO Operador, QUERO que o sistema calcule automaticamente o custo de entrega com base na soma das teles realizadas e a tabela de preços vigente PARA eliminar negociações e cálculos subjetivos.

Regras de Negócio:
O valor é calculado no momento em que a rota é concluída e baseado na distância linear ou configurada na Tabela de Preços.


Critérios de Aceite:
Dado que um motoboy finalizou seu turno
Quando o operador abrir o extrato dele
Então o valor de cada entrega e o total devido estarão já totalizados e calculados.


História:
HU7 Gerar recibo de acerto diário

Descrição:
COMO Operador, QUERO gerar um recibo unificado de todas as corridas feitas pelo entregador no dia PARA realizar o PIX do acerto financeiro com rapidez e exatidão.

Regras de Negócio:
Após gerado o recibo, os pedidos contidos nele não podem sofrer mais alterações de valores.

Critérios de Aceite:
Dado que o turno encerrou
Quando o operador confirmar o acerto
Então um comprovante digital detalhado é criado, marcando aquelas entregas como "Pagas".



UC04 Monitoramento de Logística em Tempo Real
Objetivo:
Manter a visibilidade total da frota para tomada rápida de decisões logísticas.

HISTÓRIAS DE USUÁRIOS

História:
HU08 Monitorar frota no mapa

Descrição:
COMO Operador, QUERO enxergar a posição em tempo real e o status atual de cada motoboy da frota no mapa PARA saber imediatamente quem está mais perto de uma nova retirada.


Regras de Negócio:
A posição GPS (telemetria) do celular do motoboy deve ser atualizada em background a cada 20 segundos enquanto ele estiver "Online".

Critérios de Aceite:
Dado que um motoboy está realizando uma entrega
Quando o operador observar o mapa de monitoramento
Então um ícone com o nome do motoboy se moverá em tempo real pelas ruas do mapa.


UC05 Configurar Estabelecimento e Frota
Objetivo:
Garantir a manutenção estrutural da loja e parâmetros financeiros específicos do restaurante.

HISTÓRIAS DE USUÁRIOS

História:
HU09 Gerir entregadores

Descrição:
COMO Administrador do Restaurante, QUERO cadastrar entregadores e aprovar ou bloquear seus perfis PARA garantir que apenas pessoas da minha frota atuem nas minhas entregas.
Regras de Negócio:
Entregadores com cadastro "Bloqueado" não podem receber corridas desta loja. O entregador só enxerga as corridas da loja em que está vinculado.

Critérios de Aceite:
Dado que um novo motoboy foi contratado pelo restaurante
Quando o administrador do restaurante criar o perfil na plataforma Web
Então o entregador conseguirá logar no aplicativo e ficar online para aquela loja.

História:
HU10 Configurar regras de precificação

Descrição:
COMO Administrador, QUERO cadastrar faixas e tabelas de preço com base na distância de entrega (raios km) PARA que a precificação da corrida obedeça regras justas preestabelecidas.


Regras de Negócio:
Faixas não podem sobrepor quilometragens (ex: 0 a 3km = R$9,00; 3.1km a 5km= R$12,00)

Critérios de Aceite:
Dado que o preço do combustível subiu
Quando o administrador editar o valor da faixa "0 a 3km" para R$ 6,00
Então as próximas entregas calcularão automaticamente o repasse usando o novo valor base.



UC06 Gerenciar Restaurantes
Objetivo:
Permitir a entrada e controle de diferentes restaurantes usando o mesmo sistema.

HISTÓRIAS DE USUÁRIOS

História:
HU11 Cadastrar novo Estabelecimento lParceiro

Descrição:
COMO Administrador Geral, QUERO cadastrar os dados básicos de um novo restaurante PARA gerar seu primeiro acesso e liberar o uso do sistema.
Regras de Negócio:
O CNPJ deve ser único no sistema. Ao criar o restaurante, os dados operacionais ficarão isolados das outras lojas.

Critérios de Aceite:
Dado que um novo restaurante deseja usar o serviço
Quando o Administrador Geral criar o cadastro da empresa
Então o dono do restaurante receberá suas credenciais de acesso Master.

História:
HU12 Inativar Restaurante

Descrição:
COMO Administrador Geral, QUERO inativar temporariamente o acesso de um restaurante PARA impedir o uso do sistema (ex: fim de contrato ou falta de pagamento).

Regras de Negócio:
Se a empresa estiver inativa, nenhum operador ou administrador do restaurante consegue fazer login. Motoboys não conseguirão ficar online para esta loja.

Critérios de Aceite:
Dado que o restaurante "Pizzaria XYZ" não utilizará mais o serviço
Quando o Administrador Geral alterar o status para "Inativo/Bloqueado"
Então os usuários do restaurante receberão uma mensagem de erro ao tentar realizar o login.




Projeto Técnico
Arquitetura Utilizada 
O sistema utiliza a arquitetura em camadas para o Backend e um SPA para o Frontend (BFF):
Frontend SPA (BFF): Interface Web separada, focada em consumir as APIs do Backend. (Substituindo o antigo JSF).
Service (CDI) / REST: Endpoints REST e regras de negócio para servir o SPA e o App Mobile.
Repository (JPA/EntityManager): Camada de acesso a dados.
Entity (JPA): Mapeamento objeto-relacional.
Integração Externa: Worker para consumir API de terceiros (polling) e App Mobile enviando GPS.


Ferramentas e Tecnologias 


Ferramentas e Tecnologias Utilizadas
Descrição
Versão
Objetivo
Quarkus + Jakarta EE
Latest
Plataforma de Backend
React
Latest
Plataforma Frontend
Flutter
Latest
App dos Motoboys (Android).
PostgreSQL
Latest
Armazenamento persistente de dados.
Maven
Latest
Gestor de Dependências

Modelo Lógico do Banco de Dados


Gestão de Projetos
Cronograma de Codificação do Projeto

Cronograma de Codificação do Projeto
DATA
ENTREGA
?
Setup inicial da Arquitetura (Repositórios, BD e Frameworks)
?
CRUD Base de Operadores e Motoboys
?
Integração de Login e Autenticação (OAuth)
?
Worker do iFood e Captura de Pedidos
?
Mapa Web e Fluxo de Despacho
?
App Mobile, Rastreamento GPS e Finalização

