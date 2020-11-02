
db.drop_all()
db.create_all()

testuser = Users(first_name='Bruce',last_name='Wayne') # populates the table with an example entry
db.session.add(testuser)
db.session.commit()
