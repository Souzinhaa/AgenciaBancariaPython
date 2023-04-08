## AGÊNCIA BANCÁRIA ##
Esse programa tem o objetivo de simular uma agência bancária.

# Classe Cliente #
A classe Cliente possui os seguintes atributos:

senha: número da senha do cliente;
preferencial: indica se o cliente é preferencial ou não (padrão é False);
horario_entrada: data e hora de entrada na agência;
necessidade_especial: indica se o cliente possui alguma necessidade especial (padrão é False).
O método "init" é o construtor da classe, que recebe os parâmetros mencionados e define os valores dos atributos. Caso o horário de entrada não seja fornecido, o valor padrão é o momento da criação do objeto.
O método "str" retorna uma representação em string do objeto Cliente, que contém informações relevantes sobre o cliente.
 
# Classe Caixa #
Explicando brevemente as funcionalidades da classe:
O método __init__ é responsável por inicializar as variáveis da classe.
O método adicionar_cliente adiciona um cliente à fila de espera do caixa.
O método remover_cliente remove um cliente da fila de espera e o coloca em atendimento pelo caixa. Se não houver mais clientes na fila, o caixa fica livre.
O método tempo_medio_espera calcula o tempo médio de espera dos clientes na fila de espera do caixa.
O método __str__ retorna uma string contendo informações sobre o estado atual do caixa, incluindo se ele está livre ou atendendo um cliente, quantos clientes estão na fila de espera e qual é o tempo médio de espera desses clientes.

# Classe Agencia #
A classe Agencia possui um construtor que inicializa as filas de clientes normais e preferenciais, os caixas normais e preferenciais e a hora de abertura da agência.
O método atender_clientes é responsável por fazer a chamada dos clientes para atendimento, considerando a prioridade de atendimento dos clientes preferenciais. Além disso, ele verifica se o tempo médio de espera está acima do limite de 15 minutos e adiciona um novo caixa, caso necessário.
O método emitir_senha é responsável por emitir a senha para o cliente e adicioná-lo na fila correspondente.
Note que, para que o código funcione corretamente, é necessário que a classe Caixa tenha sido implementada anteriormente, como explicado em outra resposta.
Essa classe contém as informações necessárias para gerenciar as filas de clientes em uma agência bancária, com suporte a atendimento prioritário para clientes com necessidades especiais e clientes preferenciais. A função atender_clientes é responsável por alocar os clientes nas filas de atendimento, enquanto a função emitir_senha emite senhas para novos clientes.

# Classe Principal #
Explicação do código:
Importamos as classes Caixa, Cliente e Agencia do módulo model.
Criamos a função main, que representa o menu principal do programa.
Criamos um objeto Agencia.
No menu principal, se a opção escolhida for "1", o programa pergunta o tipo de cliente e se ele possui necessidade especial. Caso o cliente seja preferencial, o programa pergunta se ele possui necessidade especial e pede a idade do cliente para verificação de prioridade.
O programa então emite a senha para o cliente e a exibe na tela.
Se a opção escolhida for "2", o programa simula o atendimento aos clientes pelas caixas.
Se a opção escolhida for "3", o programa encerra.
Se a opção escolhida não for válida, o programa exibe uma mensagem de erro.
Observação: Para atender ao requisito de prioridade no atendimento a pessoas com necessidades especiais e idosos, adicionei o parâmetro idade na função emitir_senha da classe Agencia. Isso porque a verificação de prioridade depende da idade do cliente.

# Integrantes #
Bruno Henrique de Souza Pinto - RA: 110402

