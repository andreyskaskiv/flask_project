
def create_db(db, user, profile, role):
    db.connect()
    db.create_tables([user, profile, role])
