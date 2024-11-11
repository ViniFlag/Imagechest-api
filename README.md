# Salvar Links de Imagens do Imgchest

## Descrição
Este script Python tem como objetivo automatizar o processo de salvar links de imagens de uma determinada postagem no Imgchest. Ele cria um arquivo de texto para cada postagem, contendo comandos para um sistema de gerenciamento de imagens (não especificado), facilitando a organização e o download das imagens.

## Pré-requisitos
* **Python:** Certifique-se de ter o Python instalado em sua máquina.
* **requests:** Instale a biblioteca requests usando o comando `pip install requests`.

## Como Usar
1. **Lista de IDs:** Edite a variável `lista_de_posts` para incluir os IDs das postagens desejadas.
2. **Token de Autenticação:** Substitua o valor de `token` pelo seu token de acesso ao Imgchest.
3. **Execução:** Execute o script Python.
4. **Arquivos de Saída:** Os arquivos de texto com os links das imagens serão gerados no mesmo diretório do script, com o nome correspondente ao título da postagem.

**Observações:**
* **Sistema de Gerenciamento de Imagens:** Os comandos `$im`, `$ai` e `$ai removeall` são exemplos genéricos. Adapte-os para o sistema de gerenciamento de imagens que você utiliza.
* **Organização:** O script organiza os links em grupos de 5 por linha para facilitar a leitura e o processamento posterior.
