from view import view
from model import Pedido

class Controle:
    def inicio(self):
        opcao = view.inicio()
        while opcao != 5:
            if opcao == 1:
                valores = view.coletadadosPedido()
                dados = Pedido.criaPedido(valores)
                status = Pedido.cadastraPedido(dados)
                view.imprimeStatus(status)
                opcao = view.inicio()
            elif opcao == 2:
                orderid = view.coletaId()
                status = Pedido.deletaPedido(orderid)
                view.imprimeStatus(status)
                opcao = view.inicio()
            elif opcao == 3:
                orderid = view.coletaId()
                registro = Pedido.consultaPedido(orderid)
                view.imprimePedido(registro)
                opcao = view.inicio()
            elif opcao == 4:
                valores = view.coletadadoUpdate()
                status = Pedido.atualizaPedido(valores)
                view.imprimeStatus(status)
                opcao = view.inicio()
                controller = Controle()
                controller.inicio()