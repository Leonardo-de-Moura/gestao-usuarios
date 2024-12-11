from flask import Blueprint, render_template
from database.cliente import CLIENTES

client_route= Blueprint('client', __name__)

"""""
rota de clientes

-/clientes/ (get)listar clientes
-/clientes/ (post) inserir clientes
-/çlientes/new (get) form para criar new client
-/clientes/id (get)- obter dados de um cliente por id
-/clientes/id/edit (get) renderizar um formulario para editar os dados
-/clientes/id/update (put) atualiza os dados
/clientes/id/delete (delete) deleta um cliente
"""
@client_route.route('/')
def lista_client():
    return render_template('listaclientes.html', clientes=CLIENTES)
    
@client_route.route('/', methods=['POST'])
def inserir_client():
    pass

@client_route.route('/new')
def for_new_client():
    return render_template('form_client.html')

@client_route.route('/<int:client_id>' )
def detalhe_client(client_id):
    return render_template('detalhe_client.html')

@client_route.route('/<int:client_id>/edit')
def form_edit_client(client_id):
    return render_template('form_edit_client.html')

@client_route.route('/<int:client_id>/update', methods=['PUT'])
def update_client(client_id):
    pass

@client_route.route('/<int:client_id>/delete', methods=['DELETE'])
def delete_client(client_id):
    pass
