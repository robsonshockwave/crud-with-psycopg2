from datetime import datetime

class View():
    def inicio(self):
        return self.menu()

    def menu(self):
        print('--- MENU ---')
        print('[1] - Cadastrar um pedido')
        print('[2] - Deletar um pedido')
        print('[3] - Consultar um pedido')
        print('[4] - Alterar dados de um pedido')
        print('[5] - Sair\n')
        opcao = int(input('Digite a opção desejada: '))
        return opcao

    def coletadadosPedido(self):
        orderid = input('informe o identificador do pedido: ')
        customerid = input('informe o cliente: ')
        employeeid = input('Informe o identificador do funcionario: ')
        orderdate = input('Informe a data do pedido AAAA-MM-DD: ')
        requireddate = input('informe a data de fechamento do pedido AAAA-MM-DD: ')
        shippeddate = input('informe a data de envio do pedido AAAAMM-DD: ')
        freight = input('Informe o frete: ')
        shipname = input('informe o local de envio: ')
        shipaddress = input('informe o endereço: ')
        shipcity = input('informe a cidade de envio: ')
        shipregion = input('informe a regiao de envio: ')
        shippostalcode = input('informe o CEP: ')
        shipcountry = input('informe o País: ')
        shipperid = input('informe o id do endereço de envio: ')
        ano, mes, dia = map(int, orderdate.split('-'))
        orderdate = datetime(ano, mes, dia)
        ano, mes, dia = map(int, requireddate.split('-'))
        requireddate = datetime(ano, mes, dia)
        ano, mes, dia = map(int, shippeddate.split('-'))
        shippeddate = datetime(ano, mes, dia)
        valores = [orderid, customerid, employeeid, orderdate, requireddate, shippeddate, freight, shipname, shipaddress, shipcity, shipregion, shippostalcode, shipcountry, shipperid]
        return valores

    def coletaId(self):
        orderid = input('Informe o identificador do pedido: ')
        return orderid

    def coletadadoUpdate(self):
        orderid = input('Informe o identificador do pedido: ')
        campo = input('Informe o campo que deseja atualizar: ')
        novovalor = input('Informe o novo valor: ')
        valores = [orderid, campo, novovalor]
        return valores

    def imprimePedido(self, pedido):
        if pedido is not None:
            print(f'Identificador: {pedido.pedido}')
            print(f'Cliente: {pedido.cliente}')
            print(f'Funcionário: {pedido.empregadoId}')
            print(f'Data do pedido: {pedido.data}')
            print(f'Data de fechamento do pedido: {pedido.requisicao}')
            print(f'Data de envio do pedido: {pedido.dataEnvio}')
            print(f'frete: {pedido.frete}')
            print(f'Localde invio: {pedido.remetente}')
            print(f'Endereço: {pedido.endereco}')
            print(f'Cidade: {pedido.cidade}')
            print(f'Região: {pedido.regiao}')
            print(f'CEP: {pedido.postal}')
            print(f'País: {pedido.pais}')
            print(f'id do endereço de envio: {pedido.remetenteId}')
        else:
            print('Ocorreu algum erro no processo...')
            print('Ou não existe um pedido com este identificador...\n')

        def imprimeStatus(self, status):
            if status is not None:
                print(status)
            else:
                print('Ocorreu algum erro no processo...')
                view = View()