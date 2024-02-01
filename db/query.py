from typing import Any
import sqlite3

class Query:
    def __init__(self, db_name: str):
            self.db_name = db_name

    def execute_query(self, query: str, *params: Any) -> bool:
        """Executes a query on the database.
        
        Args:
            query(str): Query to execute.
            params(Any): Parameters of the query.
        Returns:
            True if the query was executed successfully otherwise False.
            Return False if the query is a SELECT statement.
        """

        query = query.strip().upper()

        if query == "SELECT":
            return False

        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()

        try:
            cursor.execute(query, params)
        except sqlite3.IntegrityError:
            pass
        except sqlite3.OperationalError as operational_error:
            print(f"QUERY Operational Error: {operational_error}")
            connection.rollback()
            return False
        except sqlite3.DatabaseError as database_error:
            print(f"QUERY Database Error: {database_error}")
            connection.rollback()
            return False
        except sqlite3.ProgrammingError as programming_error:
            print(f"QUERY Programming Error: {programming_error}")
            connection.rollback()
            return False
        except sqlite3.Warning as warning:
            print(f"QUERY SQLite Warning: {warning}")
            connection.rollback()
            return False
        except Exception as error:
            print(f"Error executing QUERY: {error}")
            connection.rollback()
            return False
        else:
            connection.commit()
            return True
        finally:
            connection.close()

    def get_last_id_inserted(self, table_name: str) -> int:
        """Returns the last inserted id from the given table on the database.
        
        Args:
            table_name(str): Name of the table.
        Returns:
            ID of the last register as a integer.
        """
        
        query = f"SELECT id FROM {table_name} ORDER BY id DESC LIMIT 1"
        
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        
        cursor.execute(query)

        row = cursor.fetchone()
        connection.close()
        return row[0]