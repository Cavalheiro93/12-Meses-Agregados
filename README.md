# 12 Meses de Programa de Produção de Agregados (12 MPP de Agregados)

Esse foi um dos grandes projetos que conclui, durante minha função de Analista de PCP com ênfase em Agregados (Motores, Cambios e Eixos).

A ideia principal do projeto é extrair o programa de Veiculos (Caminhões e Ônibus) e "abrir" em modelo de Agregados.

Dessa forma, as partes interessadas em Agregados identificarão como será a produção dos proximos meses de Agregados.<br>


---
***OBS: Os dados do reposítorio são todos fictícios, para preservar os dados reais da empresa... A idéia aqui é apenas mostrar o projeto*** 
<br>

---

# Ferramentas utilizadas

Para esse projeto, utilizei grande parte da biblioteca do PySide6 para aprimorar meus conhecimentos na parte de criação de formulários.

As bases de dados por trás do projeto foram manipuladas usando Pandas, e outras bibliotecas de suporte como datetime.

# Passo a Passo

A primeira parte do Projeto é juntar os Dados de Veiculos com os dados de Agregados que deverão ser montados
![image](https://github.com/Cavalheiro93/12-Meses-Agregados/assets/142948648/51524e20-996e-4d45-81ca-8704b48dd8a8)

Se por acaso não for identificado o agregados daquele veiculo, é possível cadastrarmos manualmente, sem ter que alterar dentro do arquivo.

Feita a conferência dos dados, estando tudo certo, ao fecharmos o arquivo serão gerados 2 ".csv" em uma pasta chamada *Arquivos BI*

Esses arquivos irão exibir nossos dados através do PowerBI
