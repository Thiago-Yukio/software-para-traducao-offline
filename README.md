# Software para Tradução Offline

## O que é o projeto?

Um software de tradução desenvolvido em **Python**, com interface gráfica, capaz de realizar traduções **sem conexão com a internet**, preservando a privacidade dos usuários.

O projeto utiliza o **Argos Translate**, uma biblioteca open source de tradução automática neural offline, permitindo instalar apenas os modelos de idiomas desejados.

---

## Funcionalidades

- ✅ Tradução totalmente offline
- ✅ Interface gráfica intuitiva
- ✅ Suporte a múltiplos idiomas
- ✅ Preservação da privacidade (nenhum texto é enviado para servidores externos)
- ✅ Instalação automática dos modelos de tradução
- ✅ Fácil utilização
- ✅ Código aberto

---

## Tecnologias Utilizadas

- Python 3.13
- PySide6 (Qt)
- Argos Translate
- SQLite
- Requests
- PyInstaller

---
## Gerando o executável (.exe)

1. Caso deseje gerar o executável do projeto, utilize o PyInstaller.

2. Execute o comando abaixo na pasta do projeto:

pyinstaller --onefile --windowed --clean --name tradutor --icon=logo_tradutor.ico --add-data "desing_tradutor.ui;." app_tradutor.py

3. Após a compilação, o executável será gerado na pasta:

dist/
└── tradutor.exe

4. Abra a pasta dist pelo Explorador de Arquivos. Nela, você encontrará o executável tradutor.exe, pronto para ser utilizado ou distribuído.

---

## Imagem do Projeto

<img width="420" height="677" alt="Interface do software" src="https://github.com/user-attachments/assets/d9b2bcad-e98c-4857-9c0a-38c48723a873" />

---

## Observações

- Como o projeto utiliza o **Argos Translate** e o **SQLite**, o executável gerado possui um tamanho relativamente maior quando comparado ao de aplicações que dependem de serviços online.
- A tradução é realizada integralmente no computador do usuário, não sendo necessária conexão com a internet após a instalação dos modelos de idiomas.

----

👨‍💻 Autor

Thiago Yukio

GitHub:
https://github.com/Thiago-Yukio
