# Trabalho de IA - Marombot

Este repositório contém o código-fonte do Marombot, bot que tem como objetivo aconselhar praticamentes de musculação sobre medidas de segurança dentro da academia, para isso, você informa qual exercício está prestes a fazer e ele te fornece dicas de segurança, para evitar acidentes.

## Arquitetura do Robô

### Pasta Raiz

A pasta raiz armazena as informações dos exercícios e suas respectivas medidas de segurança, além disso,
armazena também o arquivo `main.py`, onde começa a execução, e as pastas model, view e controller especificadas abaixo.

### Model

A pasta "Model" contém o arquivo `dataProcess.py`, que é responsável por realizar o processamento de dados do robo.

### Controller

A pasta "controller" contém o arquivo `control.py`, que é responsável pelo controle do robô. Ele utiliza o reconhecimento de fala para entender comandos de voz e atuar em conformidade. Aqui está uma visão geral do funcionamento:

1. O arquivo `control.py` importa as funções de reconhecimento de fala da pasta "view" e as respostas pré-definidas do arquivo `dataset.json`.

2. Captura a entrada de fala do usuário e a converte em texto usando a biblioteca `speech_recognition`.

3. Compara as palavras reconhecidas com as categorias definidas no arquivo `dataset.json` (por exemplo, 'cumprimentos', 'supino', 'puxada', etc.).

4. Com base na correspondência com uma categoria, o robô seleciona uma resposta adequada a partir do `dataset.json` e a executa usando as funções da pasta "view".

### Visualização (View)

A pasta "view" contém os seguintes arquivos:

- `sense.py`: Este arquivo utiliza a biblioteca `speech_recognition` para capturar áudio do microfone e convertê-lo em texto. Ele fornece a entrada de fala para o controlador.

- `act.py`: Este arquivo, sintetiza a fala a partir do texto e a reproduz.

## Execução do Robô

Para executar o robô, siga estas etapas:

1. Certifique-se de ter o Python instalado.

2. Certifique-se de que todas as dependências, como `speech_recognition`, estão instaladas.

3. Execute o arquivo `main.py`.

4. Fale comandos de voz reconhecíveis pelo robô e observe suas respostas.

Este README fornece uma visão geral do projeto atual. Sinta-se à vontade para contribuir e expandir este projeto de IA robótica controlada por voz.
