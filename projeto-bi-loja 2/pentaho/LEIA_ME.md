# Pentaho — arquivo inicial
`01_staging_vendas.ktr` é uma transformação inicial de leitura de CSV e exportação de staging.
Abra no Spoon e confira os caminhos de entrada/saída antes de executar. O arquivo não foi testado no Spoon neste ambiente.
**Limitação:** esta transformação não faz a carga do modelo dimensional. A carga reproduzível do DW foi implementada em `python/construir_dw.py` (SQLite). Para cumprir integralmente a etapa Pentaho da disciplina, adapte o fluxo no Spoon para popular as dimensões e a fato, usando `sql/01_modelo.sql` como referência.
