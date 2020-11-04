import pandas as pd
import matplotlib.pyplot as plt

nomes = ['Paulo','Cardoso','Silva']

alunos ={'nome': nomes,
         'Nota':[2.0,8.8,10],
         'Sala':[1,3,8]}

dataframe = pd.DataFrame(alunos)
print(dataframe)
print("============================================")


tab_exc = pd.read_excel(r"C:\Tecnologia\Python\Lista_py.xlsx")
print("---------------toda a tabela-----------------")
print(tab_exc)

print("-------------Somente a coluna NOME------------")
print(tab_exc['Nome'])

print("-------------Somente a coluna IDADE------------")
print(tab_exc['Idade'])

print("-------------Somente a coluna IDADE da LINHA 02------------")
print(tab_exc['Idade'][2])

print("Gerando Gráficos com os dados IDADE")
plt.plot(tab_exc['Idade'])
plt.show()

print("Gerando Gráficos com os dados ALTURA")
plt.hist(tab_exc['Altura'])
plt.show()


print("Gerando Gráficos com os dados ALTURA(PIZZA)")
plt.pie(tab_exc['Altura'],labels=tab_exc['Nome'],autopct="%1.0f%%")
plt.show()
