with open('metroShortInfo.csv', encoding='utf-8') as file1:
    text = file1.read()


import psycopg2

connecT = psycopg2.connect(
    database='r_s_i_database',
    user='tomash_alexander',
    password='Mallard2012',
    host='localhost',
    port='5555',
)
connecT.autocommit = True

text = [
    tuple([text.split(',')]),
    ]

info = ", ".join(["%s"] * len(text))
postgres = (
    f"""INSERT INTO baseInfo_metroshortinfo (
        ofiName,
        n_ofiName,
        city,
        server,
        openDate,
        workTime,
        emblem,
        info,
        shortI
    ) 
    VALUES{info}"""
)

curs = connecT.cursor()
curs.execute(postgres, text)
