import psycopg2

class DB():

	connection = None
	cursor = None
	

	def __init__(self):
		try:
			self.connection = psycopg2.connect(user="sergeysvinarenko",
							password="1",
							host="localhost",
							port="5432",
							database="test")
			# cursor = connection.cursor()
			self.connection.autocommit = True
			self.cursor = self.connection.cursor()

		except (Exception, psycopg2.Error) as error:
			print("Error while fetching data from PostgreSQL", error)
			raise ConnectionError

	# Создать таблицу
	def create(self):
		postgreSQL_create_users_Query = """create table users(user_id bigserial primary key, name text);"""
		postgreSQL_create_messages_Query = """create table messages( message_id bigserial primary key, message_text TEXT NOT NULL, user_id bigserial REFERENCES users (user_id));"""

		self.cursor.execute(postgreSQL_create_users_Query)
		self.cursor.execute(postgreSQL_create_messages_Query)

	# Дропнуть таблицу
	def drop(self):
		postgreSQL_drop_messages_Query = """drop table if exists messages;"""
		postgreSQL_drop_users_Query = """drop table if exists users;"""

		self.cursor.execute(postgreSQL_drop_messages_Query)
		self.cursor.execute(postgreSQL_drop_users_Query)

	def select_all(self,db_name):
		postgreSQL_Query = f"select * from {db_name};"
		self.cursor.execute(postgreSQL_Query)
		return self.cursor.fetchall()

	# Закрыть соединение
	def close(self):
		if self.connection:
			self.cursor.close()
			self.connection.close()
	# Открыть соединение
	def connect(self):
		try:
			self.connection = psycopg2.connect(user="sergeysvinarenko",
							password="1",
							host="localhost",
							port="5432",
							database="test")
			# cursor = connection.cursor()
			self.connection.autocommit = True
			self.cursor = self.connection.cursor()

		except (Exception, psycopg2.Error) as error:
			print("Error while fetching data from PostgreSQL", error)
			raise ConnectionError

	# Добавляет пользователя в бд users
	def add_user(self,user_id,user_name):
		postgreSQL_Query = """insert into users values (%s,%s)"""
		try:
			self.cursor.execute(postgreSQL_Query,(user_id,user_name))
		except (Exception, psycopg2.Error) as error:
			return True
		return False


	def get_cursor(self):
		pass

	# Добавляет сообщение в бд messages
	def add_message(self,message_id,text,user_id):
		postgreSQL_Query = """insert into messages values (%s,%s,%s)"""
		try:
			self.cursor.execute(postgreSQL_Query,(message_id, text, user_id))
		except (Exception, psycopg2.Error) as error:
			return True
		return False
		# print(self.cursor.fetchone())

	# Статус соединения
	def status_connection(self):
		if self.connection is not None:
			if self.connection.closed == 0:
				return True
		return False
		