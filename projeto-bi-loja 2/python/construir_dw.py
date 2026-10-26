from pathlib import Path
import sqlite3
import pandas as pd

BASE = Path(__file__).resolve().parents[1]
DADOS = BASE / "dados"
produtos = pd.read_csv(DADOS / "produtos.csv")
clientes = pd.read_csv(DADOS / "clientes.csv")
vendas = pd.read_csv(DADOS / "vendas.csv", parse_dates=["data_venda"])
assert not vendas["venda_id"].duplicated().any()
assert vendas.notna().all().all()
vendas["faturamento"] = (vendas["quantidade"] * vendas["preco_unitario"]).round(2)
tempo = vendas[["data_venda"]].drop_duplicates().copy()
tempo["ano"] = tempo["data_venda"].dt.year
tempo["mes"] = tempo["data_venda"].dt.month
tempo["ano_mes"] = tempo["data_venda"].dt.strftime("%Y-%m")
tempo = tempo.rename(columns={"data_venda":"data_id"})
fato = vendas.rename(columns={"data_venda":"data_id"})
fato["data_id"] = fato["data_id"].dt.strftime("%Y-%m-%d")
tempo["data_id"] = tempo["data_id"].dt.strftime("%Y-%m-%d")
with sqlite3.connect(BASE / "dados" / "loja_dw.sqlite") as conn:
    produtos[["produto_id","produto","categoria"]].to_sql("dim_produto",conn,if_exists="replace",index=False)
    clientes.to_sql("dim_cliente",conn,if_exists="replace",index=False)
    tempo.to_sql("dim_tempo",conn,if_exists="replace",index=False)
    fato.to_sql("fato_vendas",conn,if_exists="replace",index=False)
    resultado = pd.read_sql_query("SELECT f.*, p.produto, p.categoria, c.cidade, t.ano, t.mes, t.ano_mes FROM fato_vendas f JOIN dim_produto p USING(produto_id) JOIN dim_cliente c USING(cliente_id) JOIN dim_tempo t USING(data_id)",conn)
resultado.to_csv(DADOS / "vendas_dashboard.csv",index=False)
print("DW SQLite criado e dados para Power BI exportados.")
print("Vendas:",len(resultado),"Faturamento:",round(resultado.faturamento.sum(),2))
