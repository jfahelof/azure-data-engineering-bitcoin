# Databricks notebook source
# MAGIC %md
# MAGIC # Arquitetura Medallion
# MAGIC
# MAGIC  Vamos criar os banco de dados (schemas) para cada camada da estrutura medallion: 
# MAGIC
# MAGIC  **Bronze** -> **Silver** -> **Gold**. 
# MAGIC
# MAGIC  Onde:
# MAGIC
# MAGIC  **Bronze**: ingestão de dados brutos.
# MAGIC  **Silver**: limpeza, tratamento e padronização.
# MAGIC  **Gold**: tabelas analíticas e métricas.

# COMMAND ----------

dbutils.widgets.text("env", "prod")
env = dbutils.widgets.get("env")
print(f"Ambiente: {env}")

# COMMAND ----------

try:
    spark.sql("""
        CREATE DATABASE IF NOT EXISTS bronze
        MANAGED LOCATION 'abfss://bronze@stbitcoin.dfs.core.windows.net/'
    """)

    spark.sql("""
        CREATE DATABASE IF NOT EXISTS silver
        MANAGED LOCATION 'abfss://silver@stbitcoin.dfs.core.windows.net/'
    """)

    spark.sql("""
        CREATE DATABASE IF NOT EXISTS gold
        MANAGED LOCATION 'abfss://gold@stbitcoin.dfs.core.windows.net/'
    """)

    print('Databases criados com sucesso.')
    dbutils.notebook.exit("SUCCESS: Medallion databases criados.")

except Exception as e:
    error_msg = str(e)
    if "SUCCESS" in error_msg:
        dbutils.notebook.exit(error_msg)
    dbutils.notebook.exit(f"ERROR: Medallion falhou. {error_msg}")
