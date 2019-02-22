from dbt.adapters.sql import SQLAdapter
from dbt.adapters.hive import HiveConnectionManager

import agate


class HiveAdapter(SQLAdapter):
    ConnectionManager = HiveConnectionManager

    @classmethod
    def date_function(cls):
        return 'from_unixtime(unix_timestamp())'

    @classmethod
    def convert_text_type(cls, agate_table, col_idx):
        return "VARCHAR"

    @classmethod
    def convert_number_type(cls, agate_table, col_idx):
        decimals = agate_table.aggregate(agate.MaxPrecision(col_idx))
        return "DOUBLE" if decimals else "INTEGER"

    @classmethod
    def convert_datetime_type(cls, agate_table, col_idx):
        return "TIMESTAMP"

    def drop_schema(self, database, schema, model_name=None):
        relations = self.list_relations(
            database=database,
            schema=schema,
            model_name=model_name
        )
        for relation in relations:
            self.drop_relation(relation, model_name=model_name)
        super(HiveAdapter, self).drop_schema(
            database=database,
            schema=schema,
            model_name=model_name
        )
