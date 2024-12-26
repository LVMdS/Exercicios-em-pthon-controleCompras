# Controle Mensal - Aplicativo de Gestão de Despesas

Este é um aplicativo de controle mensal de despesas desenvolvido com Tkinter, que permite ao usuário adicionar, visualizar e gerenciar despesas de forma simples e eficiente. O aplicativo permite o registro de despesas em um arquivo CSV, com a opção de marcar despesas como pagas e calcular o total das despesas não pagas.

## Funcionalidades

- **Adicionar Despesas**: O usuário pode adicionar uma despesa, informando o local, a data e o valor.
- **Visualizar Despesas**: As despesas são exibidas em uma tabela, com a possibilidade de visualizar o local, a data e o valor de cada despesa.
- **Marcar como Pago**: O usuário pode marcar uma despesa como paga ao dar um duplo clique na linha correspondente da tabela.
- **Cálculo do Total de Despesas Não Pagas**: O total das despesas não pagas é exibido e atualizado automaticamente.
- **Armazenamento de Dados**: As despesas são salvas em um arquivo CSV, que pode ser carregado e atualizado a qualquer momento.

## Requisitos

- Python 3.x
- Tkinter (já incluso na instalação padrão do Python)
- Bibliotecas: `csv`, `os`, `datetime`

## Como Usar

1. **Abrir o Aplicativo**: Execute o script Python para iniciar o aplicativo.
2. **Selecionar o Arquivo CSV**: O aplicativo abrirá a opção para selecionar ou salvar o arquivo CSV onde as despesas serão armazenadas.
3. **Adicionar Despesas**: Preencha os campos de local, data (formato dd/mm/yyyy) e valor (em R$) e clique em "Adicionar Despesa".
4. **Marcar Como Pago**: Dê um duplo clique na linha da despesa para marcá-la como paga.
5. **Visualizar Despesas Não Pagas**: O total das despesas não pagas será exibido automaticamente.

## Exemplo de Uso

- **Adicionar uma despesa**:
    - Local: Supermercado
    - Data: 15/12/2024
    - Valor: 100,00

- **Marcar uma despesa como paga**: Ao dar um duplo clique em uma despesa na tabela, o sistema perguntará se a despesa foi paga. Se confirmado, a despesa será removida da lista e o total de não pagos será atualizado.

## Estrutura de Arquivos CSV

O arquivo CSV utilizado para armazenar as despesas segue a seguinte estrutura:

```csv
Local,Data,Valor,Pago
Supermercado,15/12/2024,100.00,False
Farmácia,20/12/2024,50.00,True
