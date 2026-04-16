from prophet import Prophet
from statsmodels.tsa.arima.model import ARIMA

# Prophet
def train_prophet(df):
    data = df[['date', 'temp']].rename(columns={
        'date': 'ds',
        'temp': 'y'
    })

    model = Prophet()
    model.fit(data)

    return model

def forecast_prophet(model, periods=365):
    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)
    return forecast


# ARIMA
def train_arima(df):
    df = df.set_index('date')
    model = ARIMA(df['temp'], order=(5,1,0))
    model_fit = model.fit()
    return model_fit

def forecast_arima(model, steps=365):
    forecast = model.forecast(steps=steps)
    return forecast