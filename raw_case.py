"""
Conseguimos implementar funcionalidades bem simples e ao mesmo tempo elegantes como esse 
"with" aqui na orientação a objetos em Python, e acaba se tornando uma ferramenta muito boa 
para a gente trabalhar com erros e exceções e até mesmo com conexões e desligamento de conexões 
em bancos de dados.

"""
class AlgumaCoisa:
    def __enter__ (self):
        print("Estou entrando" )
    def __exit__ (self, exc_type, exc_val, exc_tb):
        print ("Estou Saindo" )

with AlgumaCoisa() as something:
    print( "Estou no meio")

    """
    -> saídas da execuçao acima:
        Estou entrando
        estou no meio
        Estou Saindo
    -> a utilização do with acima, obriga os metodos de enter e exit a serem implementados
    -> que são quando inicia e termina a execuçao do with
    -> tudo que está abaixo da declaração do with, erá executado entre enter e exit
    exc_type:
        O tipo de exceçao que ocorreu, se houver.
        Se nao ocorreu nenhuma exceçao, este parâmetro será None.
    exc_val:
        O valor da exceçao que ocorreu, se houver.
        Se não ocorreu nenhuma exceçao, este parâmetro será None.
    exc_tb:
        O traceback(rastreamento de pilha) da exceçao que ocorreu, se houver.
        Se não ocorreu nenhuma exceçao, este parâmetro será None.
    """	