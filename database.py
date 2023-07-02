from sqlalchemy import create_engine, text


db_connection_string = "mysql+pymysql://flvxfch9dho2mnw1rpic:pscale_pw_8P8rM8XMc0WRNvQvqvylpuE0TguyZSQuuEmPYCrV2Nk@aws.connect.psdb.cloud/shopndash?charset=utf8mb4"

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