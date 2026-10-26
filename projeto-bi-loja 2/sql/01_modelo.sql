-- Modelo estrela: cada linha da fato representa um item de venda (uma venda por linha na base didática).
CREATE TABLE IF NOT EXISTS dim_produto (produto_id INTEGER PRIMARY KEY, produto TEXT NOT NULL, categoria TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS dim_cliente (cliente_id INTEGER PRIMARY KEY, cliente TEXT NOT NULL, cidade TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS dim_tempo (data_id DATE PRIMARY KEY, ano INTEGER NOT NULL, mes INTEGER NOT NULL, ano_mes TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS fato_vendas (
 venda_id INTEGER PRIMARY KEY, data_id DATE NOT NULL REFERENCES dim_tempo(data_id),
 cliente_id INTEGER NOT NULL REFERENCES dim_cliente(cliente_id),
 produto_id INTEGER NOT NULL REFERENCES dim_produto(produto_id),
 quantidade INTEGER NOT NULL, preco_unitario NUMERIC(12,2) NOT NULL,
 faturamento NUMERIC(14,2) NOT NULL
);
