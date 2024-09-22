import requests

def salvar_links_por_postagem(post_id, token):
 
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"https://api.imgchest.com/v1/post/{post_id}", headers=headers)
    data = response.json()["data"]
    nome = data["title"]
    links_imagem = data["images"]

    # Cria um arquivo de texto com o nome da postagem
    with open(f"{nome}.txt", "w") as arquivo:
       
        arquivo.write(f"$im {nome}\n")
        arquivo.write(f"$ai removeall {nome}\n")

        contador = 0
        for link in links_imagem:
            if contador % 5 == 0:
                arquivo.write(f"\t$ai {nome} ")
            arquivo.write(f"${link['link']}\n ")
            contador += 1
            if contador % 5 == 0 or contador == len(links_imagem):
                arquivo.write("\n")

# Lista de IDs dos post
lista_de_posts = ["ID(s)dopost(s)"]

# Token de autenticação
token = "Token da conta do imagemchest"

# Processa cada postagem
for post_id in lista_de_posts:
    salvar_links_por_postagem(post_id, token)