import cfg
import utils

class Thrasher:
    # ID OF THE GUY
    id_user = ""
    # THRASHCOINS
    thrashcoin = 0

    def __init__(self, id_user = None):
        self.id_user = id_user

        conn_info = utils.databaseConnect()
        conn = conn_info.get('conn')
        cursor = conn.cursor()

        # Retrieve object

        cursor.execute(
            "SELECT {} FROM thrashers WHERE {} = %s".format(
                cfg.col_thrashcoin,
                cfg.col_id_user,
            ), (
                id_user,
            ))
        result = cursor.fetchone();

        if result != None:
            # Record found: apply the data to this object.
            self.thrashcoin = result[0]

    def persist(self):
        try:
            conn_info = utils.databaseConnect()
            conn = conn_info.get('conn')
            cursor = conn.cursor()

            # Save the object.
            cursor.execute(
                "REPLACE INTO thrashers({}, {}) VALUES(%s, %s)".format(
                    cfg.col_id_user,
                    cfg.col_thrashcoin,
                ), (
                    self.id_user,
                    self.thrashcoin,
                ))

            conn.commit()
        finally:
            # Clean up the database handles.
            cursor.close()
            utils.databaseClose(conn_info)