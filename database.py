from sqlalchemy import create_engine, text
import os 

db_connection_string = os.environ('DB_CONNECTION_STRING')

engine = create_engine(
  db_connection_string,
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  })

with engine.connect() as conn:
  result = conn.execute(text("select * from inventory"))
  print("type(result):", type(result))
  result_all = result.all()
  print("type(result.all()):", type(result_all))
  print("result.all():", result_all)