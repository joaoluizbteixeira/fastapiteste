from fastapi import FastAPI
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

app = FastAPI()
meses_judaicos = ['Nissan', 'Yar', 'Sivan', 'Tammuz', 'AB', 'Elul', 'Tishri', 'Khesvan', 'Kisleu', 'Thebet', 'Schebat', 'Adar']

@app.get("/teste/{data_converter}")
async def return_message(data_converter: str):
    data_gregoriano = datetime.strptime(data_converter, "%d-%m-%Y")
    data_maconica = data_gregoriano - relativedelta(days=79) + relativedelta(years=4000)
    mes_maconico = meses_judaicos[data_maconica.month-1]
    mensagem_retornada = f'A data {datetime.strftime(data_gregoriano, "%d-%m-%Y")} da era vulgar equivale ao dia {data_maconica.day} do mês de {mes_maconico} (mês {data_maconica.month}) do ano de {data_maconica.year} da verdadeira luz'
    return {"mensagem": mensagem_retornada}