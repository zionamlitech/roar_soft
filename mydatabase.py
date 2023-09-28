from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://8djvzlpe90hmgv9b9unx:pscale_pw_nvplPnj6w6Jse9zBZV4aOBaT4uBmuHhoZuqYweQaNZp@gcp.connect.psdb.cloud/mydadatabase", echo='debug')
with engine.connect() as connection:
 result=connection.execute(text('SELECT * from company'))
 print(result.all())