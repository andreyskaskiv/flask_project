
def create_db(db, user, profile):
    # db.connect()
    db.create_tables([user, profile])
