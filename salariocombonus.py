#coding: utf-8

def comissaosalario ():
    nome = input("Entre com o nome do vendedor: ")
    salariofixo = float(input("Informe o salário: "))
    vendas = float(input("Informe valor das vendas: "))
    comissao = 0.15 * vendas
    pagamentoesperado = comissao + salariofixo
    return comissao, pagamentoesperado, nome

if __name__ == "__main__":
    comissao, pagamentoesperado, nome = comissaosalario()
    print("{0} obtve R${1:.2f} de comissão e vai receber {2:.2f}".format(nome, comissao, pagamentoesperado))