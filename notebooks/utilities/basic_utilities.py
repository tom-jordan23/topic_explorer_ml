import uuid
#import pandas as pd

def persist_to_postgres(db_conf, target_table, df):
    # This remains under-developed after finding out how much
    # AWS charges just to have a db exist

    from sqlalchemy import create_engine


    engine = create_engine("postgresql://{user}:{password}@{host}:{port}/{database}".format(**db_conf))

    connection = engine.connect()
    df.to_sql(target_table ,connection, schema='rc', if_exists='replace', index=False)
    connection.close()

def write_to_excel(df,filepath='stored_data',filename='file'):
    guid = generate_uuid()
    full_filepath = f"{filepath}\\{filename}_{guid}.xlsx"
    df.to_excel(full_filepath, index=False)

    return full_filepath


def generate_uuid():
    return uuid.uuid4().hex




def docid_from_url(url):
    if isinstance(url, str) == False:
        return url

    # Regular expression to remove trailing "/"
    url = re.sub(r'/$', '', url)

    segments = url.split("/")
    docid = segments[-1]

    if docid == "":
        docid = generate_uuid()

    return docid