class ServerDatabase(object):
    """
    Main database class for server
    """
    from database.db_base import db_open, \
        db_close, \
        db_commit, \
        db_rollback, \
        db_table_index_check, \
        db_table_count, \
        db_query, \
        db_parallel_workers, \
        db_drop_table

    # class variables
    sql3_conn = None
    sql3_cursor = None
