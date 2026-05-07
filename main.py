from datetime import datetime

estoque = []
vendas = []



def cdt_produto(nome, quantidade):
   produto ={"nome": nome, 
             "quantidade": quantidade}
   estoque.append(produto)
   

def etq_baixo():
   print("\n----REPORT ESTOQUE----")

   for produto in estoque:
      if produto["quantidade"] == 0:
         print(f"{produto["nome"]} -> Fazer pedido urgente")
      elif produto["quantidade"] < 5:
         print(f"{produto["nome"]} -> Estoque baixo")




def rgt_venda(nome_produto, valor):
   for produto in estoque:
      if produto["nome"] == nome_produto:
      
         if produto ["quantidade"] > 0:
            produto["quantidade"] -= 1 
            
            venda = {"produto": nome_produto,
                     "valor": valor}
            
            vendas.append(venda)

            print(f"Venda registrada: {nome_produto}, {valor}")
            return
         
         else:
            print(f"{nome_produto} Sem Estoque!")
            return 
   

def calcular_faturamento():
   total = 0
   for venda in vendas:
      total += venda["valor"] 
   return total 

def pdt_mais_caro():
   if len(vendas) == 0:
      return None 
   
   return max(vendas, key=lambda
              venda: venda["valor"])

def pdt_mais_barato():
   if len(vendas) == 0:
      return None
   return min(vendas, key=lambda 
              venda:venda["valor"])

def qtd_produtos_acima_100():
   contador = 0 
   for venda in vendas:
      if venda["valor"] > 100:
         contador+= 1
   return contador 


      #RELATORIO FINAL 
def rlt_final():


   print("\n=================================")
   print("RELATORIO FINAL DA LOJA")
   print("=================================")


   print("\nESTOQUE FINAL")
   for produto in estoque:
      print(f"{produto["nome"]} -> {produto["quantidade"]} unidades")

   faturamento = calcular_faturamento()
   print(f"\nFaturamento total do dia:R${faturamento:.2f}")

   caro = pdt_mais_caro()
   barato = pdt_mais_barato()
   if caro:
      print(f"Produto mais caro vendido:{caro['produto']} - R${caro['valor']:.2f}")

   if barato:
      print(f"Produto mais barato vendido:{barato['produto']} - R${barato['valor']:.2f}")

   acima_100 = qtd_produtos_acima_100()
   print(f"Quantidade de produtos acima de R$100: {acima_100}")

   data = datetime.now().strftime("%d/%m/%Y %H:%M")
   print(f"Data do relatorio: {data}")

#Cadastro De Produtos
cdt_produto("Arroz", 10)
cdt_produto("Feijão", 3)
cdt_produto("Macarrão", 0)
cdt_produto("Café", 8)

#Estoque Baixo
etq_baixo()

#Registro De Vendas
rgt_venda("Arroz", 25.0)
rgt_venda("Café", 18.5)
rgt_venda("Arroz", 120.0)
rgt_venda("Feijão", 8.0)

#Relatorio Final
rlt_final()
