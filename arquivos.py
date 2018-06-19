arq = open('arquivo.txt', 'w')
# Modo de abertura de arquivos:
#	r - Leitura
#	w - Escrita, apaga o conteúdo se o arquivo existir
#	a - Excrita, mas inclui no final
#	b - Binario
#	Podemos somar os modos, tipo w+b
texto = '''
Aprendendo um monte de coisa maneira
Python é muito doido
Mais uma linha
'''
arq.write(texto)

arq.close()
