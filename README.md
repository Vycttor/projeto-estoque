# Sistema Web de Controle de Estoque

## Contexto

Este projeto acadêmico foi desenvolvido para atender às necessidades de uma oficina mecânica, visando informatizar o controle de peças e insumos. O sistema permite o cadastro, movimentação e monitoramento de produtos, proporcionando maior organização, agilidade e precisão na gestão do estoque.

---

## Objetivo do Projeto

Desenvolver um sistema web funcional e didático para o controle de estoque, aplicando conhecimentos de lógica de programação, banco de dados, desenvolvimento web e documentação técnica. O projeto visa solucionar um problema real identificado em uma oficina mecânica, substituindo métodos manuais por uma ferramenta interativa e eficiente.

---

## Preview das Telas

### Tela Principal

![Tela de Produtos](assets/tela-principal.png)
> Tela principal do sistema, exibe a listagem completa de produtos cadastrados, 
> com opções de entrada e saída de estoque, edição e exclusão de cada item.

### Tela de Cadastro

![Tela de Cadastro](assets/tela-cadastro-de-produto.png)
> Tela de cadastro de novos produtos, permite registrar informações como nome, 
> código, fornecedor, quantidade, estoque mínimo e preço unitário.

### Tela de Edição

![Tela de Edição de Produto](assets/tela-editar-produto.png)
> Tela de edição de produtos, permite atualizar as informações de um produto 
> já cadastrado, garantindo a precisão dos dados no sistema.

### Alerta de Estoque Mínimo

![Tela Alerta de estoque mínimo](assets/alerta-minimo.png)
> Alerta visual destacado em vermelho para produtos com quantidade igual ou 
> inferior ao estoque mínimo estabelecido, facilitando a tomada de decisão 
> para reposição de peças.



---

## Funcionalidades

- Cadastro de produtos (nome, código, fornecedor, quantidade, estoque mínimo, preço, data de cadastro)
- Listagem de todos os produtos em tabela
- Edição e exclusão de produtos
- Registro de entrada e saída de estoque
- Validação automática para impedir saída maior que a quantidade disponível
- Alerta visual para itens com quantidade igual ou inferior ao estoque mínimo
- Interface web intuitiva e responsiva

---

## Tecnologias Utilizadas


- **Python 3** ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
- **Flask** (framework web)![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
- **SQLite** (banco de dados)![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
- **HTML5 / CSS3**![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
- **Jinja2** (templates Flask)![Jinja](https://img.shields.io/badge/jinja-white.svg?style=for-the-badge&logo=jinja&logoColor=black)

---
## Como Executar

### Pré-requisitos

- Python 3 instalado
- pip instalado

### Passo a Passo

1. Clone o repositório:
    ```bash
    git clone https://github.com/Vycttor/projeto-estoque.git
    cd projeto-estoque
    ```

2. Crie e ative um ambiente virtual (opcional, mas recomendado):
    ```bash
    python -m venv venv
    venv\Scripts\activate   # Windows
    source venv/bin/activate # Linux/Mac
    ```

3. Instale as dependências:
    ```bash
    pip install flask
    ```

4. Inicialize o banco de dados:
    ```bash
    python init_db.py
    ```

5. Execute o sistema:
    ```bash
    python app.py
    ```

6. Acesse no navegador:
    ```
    http://127.0.0.1:5000
    ```

---



---

## Melhorias Futuras

- Dashboard de indicadores de estoque
- Histórico de movimentações
- Autenticação de usuários
- Implantação online (cloud)
- Integração com sistemas de vendas
- Responsividade para diferente tamanhos de tela

---

## Autor

- Victor Pinheiro
- Projeto Integrador: Laboratório de Programação.
- Universidade [UNISA - Universidade Santo Amaro]
- Ano: 2026

---

## Licença

Projeto acadêmico, sem fins comerciais.
