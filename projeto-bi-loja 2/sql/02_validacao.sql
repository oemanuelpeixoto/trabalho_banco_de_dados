SELECT COUNT(*) AS total_vendas, SUM(faturamento) AS faturamento_total, ROUND(AVG(faturamento),2) AS ticket_medio FROM fato_vendas;
SELECT p.categoria, ROUND(SUM(f.faturamento),2) AS faturamento FROM fato_vendas f JOIN dim_produto p ON p.produto_id=f.produto_id GROUP BY p.categoria ORDER BY faturamento DESC;
