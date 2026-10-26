# Criar o arquivo .pbix no Windows
1. Execute `python python/construir_dw.py` para criar `dados/vendas_dashboard.csv`.
2. Abra Power BI Desktop no Windows e escolha **Obter dados > Texto/CSV**.
3. Selecione `dados/vendas_dashboard.csv` e clique em **Carregar**.
4. Confirme `data_id` como data e `faturamento` como número decimal.
5. Crie as medidas de `medidas_dax.txt` (Modelagem > Nova medida).
6. Crie cartões para Faturamento Total, Total de Vendas e Ticket Médio.
7. Crie gráficos: faturamento por categoria, por ano_mes e por produto.
8. Adicione um filtro de categoria e salve como `powerbi/dashboard_loja.pbix`.

**Observação:** o `.pbix` não está incluído porque depende do Power BI Desktop. Não confundir o arquivo CSV preparado com o dashboard final.
