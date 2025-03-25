# To-do App com Tkinter e Banco de Dados

## Descrição
Este projeto é um aplicativo de lista de tarefas (To-do App) desenvolvido em Python utilizando a biblioteca Tkinter para a interface gráfica e um módulo de banco de dados personalizado para armazenar e gerenciar tarefas. O aplicativo permite adicionar, atualizar e remover tarefas de uma lista.

## Funcionalidades
- **Adicionar Tarefas**: Permite ao usuário inserir novas tarefas na lista.
- **Atualizar Tarefas**: O usuário pode selecionar uma tarefa existente e atualizá-la.
- **Remover Tarefas**: O usuário pode remover tarefas selecionadas da lista.
- **Exibição de Tarefas**: As tarefas são exibidas em uma Listbox, permitindo fácil visualização e interação.

## Requisitos
- Python 3.x
- Tkinter (geralmente incluído com a instalação do Python)
- Um módulo de banco de dados personalizado (`db.py`) que deve conter funções para inserir, selecionar, atualizar e deletar tarefas.

## Estrutura do Código
O código é organizado em seções que definem cores, criam a janela principal, dividem a interface em frames e implementam as funcionalidades principais. 

### Cores
As cores são definidas no início do código para facilitar a personalização da interface.

### Janela Principal
A janela principal é criada utilizando a classe `Tk()` do Tkinter, e a interface é dividida em dois frames: um para a entrada de tarefas e outro para a exibição das tarefas.

### Funções Principais
- **main(a)**: Controla a exibição dos componentes da interface com base na ação (novo, atualizar).
- **adicionar()**: Adiciona uma nova tarefa ao banco de dados.
- **remover()**: Remove a tarefa selecionada da lista.
- **mostrar()**: Atualiza a Listbox com as tarefas do banco de dados.
- **atualizar()**: Atualiza a tarefa selecionada.

## Como Executar
1. Certifique-se de que você tem o Python 3.x instalado em seu sistema.
2. Salve o código em um arquivo chamado `main.py`.
3. Crie um arquivo `db.py` que contenha as funções necessárias para manipular o banco de dados.
4. Execute o aplicativo com o seguinte comando:
   ```bash
   python main.py

# Exemplo de Uso
- Abra o aplicativo.
- Use o botão "Novo" para adicionar uma nova tarefa.
- Selecione uma tarefa na lista e use o botão "Atualizar" para modificar a tarefa.
- Selecione uma tarefa e clique em "Remover" para excluí-la da lista.
