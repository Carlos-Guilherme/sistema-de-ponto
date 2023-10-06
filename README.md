# Cronômetro com Registros

Este é um aplicativo de cronômetro desenvolvido em Python com PyQt5, projetado para controle de tempo pessoal. Ele permite que você inicie, pause e finalize diferentes tipos de pausas, registrando o tempo decorrido para cada uma delas. Além disso, os dados são armazenados em um banco de dados SQLite para referência futura.

## Funcionalidades

- **Controle de Pausas:** Inicie o cronômetro para contar o tempo dedicado a diferentes atividades, como trabalho, pausas para descanso, idas ao banheiro, pausas para o almoço e tarefas domésticas.

- **Registro Detalhado:** Registre o tempo gasto em cada tipo de pausa. Todos os dados são armazenados em um banco de dados SQLite para análise posterior.

- **Personalização:** O código pode ser facilmente personalizado para incluir mais tipos de pausas ou funcionalidades específicas, tornando-o adequado para uso pessoal ou empresarial.

## Requisitos

Certifique-se de ter Python e os seguintes módulos instalados:
```bash
pip install PyQt5 sqlite3
```
## Como usar

- **Execução:** Execute o arquivo main.py para iniciar o aplicativo.

- **Iniciar Pausa:** Clique em "Iniciar" para iniciar o cronômetro para a atividade desejada.

- **Pausar:** Clique em "Pausar" para interromper a contagem do tempo.

- **Finalizar Pausa:** Selecione o tipo de pausa no menu suspenso e clique em "Finalizar" para registrar o tempo da pausa.

- **Registros:** Todos os registros de pausas são exibidos na tabela na interface do usuário.

## Banco de Dados

Os registros são armazenados em um banco de dados SQLite com a seguinte estrutura:

- **data:** Data do registro (formato: 'yyyy-MM-dd').

- **tempo_trabalho:** Tempo total dedicado ao trabalho.

- **pausa_descanso:** Tempo total dedicado às pausas para descanso.

- **pausa_banheiro:** Tempo total dedicado às pausas para o banheiro.

- **pausa_almoco:** Tempo total dedicado às pausas para o almoço.

- **pausa_servico_domestico:** Tempo total dedicado às pausas para serviço doméstico.

## Uso e Personalização
Este aplicativo foi projetado para uso pessoal, mas pode ser adaptado para cenários empresariais. Você pode personalizar facilmente o código para incluir funcionalidades adicionais ou ajustá-lo conforme suas necessidades específicas.
