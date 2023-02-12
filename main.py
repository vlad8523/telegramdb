from db import DB
import psycopg2

try:
	db = DB()
	db.drop()
	db.create()
	# db.close()
except ConnectionError:
	print('Ошибка соединения')
except (Exception, psycopg2.Error) as error:	
	print("Error while fetching data from PostgreSQL", error)

print("1 - open connection")
print("2 - close connection")
print("3 - drop tables")
print("4 - create tables")
print("5 - get: 1 - users, 2 - messages")
print("6 - add: 1 - users, 2 - messages")
print("7 - status connection")


try:
	while True:
		com = input()
		match com:
			case '1':
				db.connect()
				print('db.connect()')
			case '2':
				db.close()
				print('db.close()')
			case '3':
				db.drop()
				print('db.drop()')
			case '4':
				db.create()
				print('db.create()')
			case '5':
				if db.status_connection():
					print('1 - users, 2 - messages')
					table = input()
					match table:
						case '1':
							print(db.select_all('users'))
						case '2':
							print(db.select_all('messages'))
						case _:
							print('Wrong code')
				else:
					print('Connection is closed')

			case '6':
				if db.status_connection():
					print('1 - users, 2 - messages')
					table = input()
					match table:
						case '1':
							comm = input().split()
							db.add_user(*comm)
							print('db.add_user(*comm)')
						case '2':
							comm = input().split()
							db.add_message(*comm)
							print('db.add_message(*comm)')
						case _:
							print('Wrong code')
				else:
					print('Connection is closed')
			case '7':
				print(f"Status connection: {'Connection is open' if db.status_connection() else 'Connection is close'}")
			case _:
				print('Wrong code')	
except KeyboardInterrupt:
	if db.status_connection():
		db.close()

	print(f"Status connection: {db.status_connection()}")

