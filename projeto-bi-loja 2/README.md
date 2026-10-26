# BI — Vendas de Loja de Eletrônicos

Projeto acadêmico didático. **Dados sintéticos**, gerados apenas para demonstração, com 500 vendas de 2025.

## Pergunta de negócio
Quais categorias concentram o faturamento e como as vendas variam ao longo do ano?

## Estrutura
- `dados/`: três arquivos CSV de origem e, após execução, DW SQLite e CSV do dashboard.
- `pentaho/`: transformação `.ktr` inicial de staging (não validada no Spoon).
- `sql/`: modelo dimensional em SQL PostgreSQL e consultas de validação.
- `python/`: script de construção do DW SQLite e notebook de exploração.
- `powerbi/`: medidas DAX e instruções para gerar o `.pbix` no Windows.

## Como executar no Mac
```bash
cd projeto-bi-loja
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python python/construir_dw.py
jupyter lab python/analise_exploratoria.ipynb
```

## Modelo dimensional
- `fato_vendas`: uma linha por venda/item; valor, quantidade, chaves de data, cliente e produto.
- `dim_produto`: produto e categoria.
- `dim_cliente`: cliente e cidade.
- `dim_tempo`: ano, mês e ano-mês.

## Fluxo e limitações
CSV bruto → transformação inicial Pentaho para staging (verificar no Spoon) → construção de DW SQLite pelo script Python → exploração Pandas → CSV para Power BI Desktop → `.pbix` criado no Windows.

**Atenção:** o pipeline integral Pentaho → DW não está automatizado neste pacote. A transformação Pentaho é um ponto de partida, e não deve ser apresentada como ETL completo já testado. O `.pbix` precisa ser criado no Power BI Desktop. O SQL PostgreSQL é um modelo de referência; o script local usa SQLite.

## Validação
O script deve produzir 500 registros na tabela fato. Conferir faturamento total e ticket médio com a consulta SQL e com o Power BI.
