# Calculadora em Tkinter

## Descrição:

Uma calculadora simples construída usando a biblioteca Tkinter do Python. O programa é composto por três arquivos: `main.py`, `func.py` e `keysym.py`.

## Arquivos:

### 1. **main.py**:

#### Descrição:

O arquivo `main.py` é o ponto de entrada do programa da calculadora. Ele é responsável por criar a interface gráfica do usuário (GUI) e interagir com as funções definidas em `func.py`.

#### Detalhes:

- **Importações**:
  - `Tk, Entry, Text, Frame, NONE, mainloop` do módulo `tkinter`: Usados para criar a janela principal, área de exibição, painel de botões e loop principal da aplicação.
  - `func`: Importa todas as funções definidas no arquivo `func.py`.

- **Inicialização**:
  - `calc`: É a janela principal da aplicação.
  - `calc.title("Calculadora")`: Define o título da janela.
  - `calc.resizable(False, False)`: Desativa o redimensionamento.
  - `calc.configure(bg='black')`: Define a cor de fundo.
  - `calc.bind("<Key>", lambda event: on_key_press(event, display))`: Vincula eventos de tecla à função `on_key_press`.

- **Área de Exibição**:
  - `display`: Área onde números e resultados são mostrados. Mudou de `Entry` para `Text` para suportar `wrap=NONE`.
  - `display.pack(fill='x', expand=True)`: Garante que a área de exibição ocupe toda a largura.

- **Painel de Botões**:
  - `painel`: Frame que contém todos os botões.
  - `create_button()`: Função para criar cada botão na GUI.

- **Botões**:
  - Organizados em linhas (`row`) e colunas (`col`).
  - Cada botão tem um rótulo, uma função associada e estilização específica.

- **Loop Principal**:
  - `mainloop()`: Mantém a janela da aplicação aberta.

### 2. **func.py**:

#### Descrição:

O arquivo `func.py` contém as funções essenciais que são usadas pelo arquivo `main.py` para executar as operações da calculadora e interagir com a GUI.

#### Detalhes:

- **Importações**:
  - `Button, END` do módulo `tkinter`: Usados para criar botões e manipular o widget de texto.

- **Funções**:
  - `insertValue(display, value)`: Insere um valor na área de exibição.
  - `clear(display)`: Limpa a área de exibição.
  - `calculate(display)`: Calcula o resultado da expressão.
  - `create_button(painel, text, command, row, col, ...)`: Cria um botão na GUI.
  - `on_key_press(event, display)`: Função chamada quando uma tecla é pressionada.

### 3. **keysym.py**:

#### Descrição:

Programa auxiliar usado para detectar e imprimir o nome das teclas pressionadas. Foi usado durante o desenvolvimento para descobrir os nomes das teclas para serem usados no programa principal.

## Como usar:

1. Execute o arquivo `main.py` para iniciar a calculadora.
2. Use os botões na GUI ou as teclas do teclado para inserir números e operações.
3. Pressione "=" ou "Enter" para calcular o resultado.
4. Use "C" ou a tecla "Backspace" para limpar a área de exibição.

## Características:

- Suporte para operações básicas: adição, subtração, multiplicação e divisão.
- Suporte para operações avançadas: potência (`^`) e raiz quadrada (`√`).
- Suporte para parênteses.
- Teclas do teclado numérico (NumLock) são suportadas.
- Janela não redimensionável.
- Tema escuro.

## Desenvolvimento futuro (To Do):

- Adicionar mais funções matemáticas, como trigonometria.
- Implementar um histórico de cálculos.
- Adicionar suporte para teclas de função.

---

A documentação foi organizada para destacar os principais componentes e funcionalidades do programa. As seções foram estruturadas para facilitar a leitura e compreensão.
