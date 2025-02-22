# 🎬 Lista de Filmes Favoritos  
![demo](MOVIES/static/movies_screenshot.PNG)

Este é um aplicativo web simples para gerenciar sua lista de filmes favoritos.

Você pode **adicionar, visualizar, atualizar e excluir filmes**, além de classificá-los com uma **nota e um comentário**.  

## 🚀 Tecnologias utilizadas  

- **Flask** - Framework web  
- **Flask-SQLAlchemy** - ORM para banco de dados  
- **Flask-WTF** - Formulários seguros  
- **Bootstrap-Flask** - Estilização com Bootstrap  
- **SQLite** - Banco de dados leve  

## 📂 Estrutura do projeto  

```
📁 Projeto
│-- 📄 main.py               # Código principal da aplicação
│-- 📄 requirements.txt      # Dependências do projeto
│-- 📄 favorite-movies.db    # Banco de dados SQLite
│-- 📄 index.html            # Página inicial
│-- 📄 add.html              # Página de adição de filmes
```

## ⚡ Como rodar o projeto  

1. **Clone este repositório:**  
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   ```

2. **Acesse a pasta do projeto:**  
   ```bash
   cd nome-do-projeto
   ```

3. **Crie um ambiente virtual e ative-o:**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

4. **Instale as dependências:**  
   ```bash
   pip install -r requirements.txt
   ```

5. **Execute a aplicação:**  
   ```bash
   python main.py
   ```

6. **Acesse no navegador:**  
   ```
   http://127.0.0.1:5000
   ```

## 🎥 Funcionalidades  

✅ Exibir os **TOP filmes favoritos**  
✅ **Adicionar** novos filmes  
✅ **Editar** nota e review dos filmes  
✅ **Remover** filmes da lista  

## 🛠️ Melhorias futuras  

- 🔍 Implementação de **API** para buscar filmes automaticamente  
- 🔐 Sistema de **login** para usuários  

---

📌 **Autor:** [gus-ant](https://github.com/gus-ant) 
📌 **Licença:** MIT  
