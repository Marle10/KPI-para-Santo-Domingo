import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

# Datos simulados para Café Santo Domingo
data = {
    "Mes": ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"],
    "Tasa_Conversion": [4.5, 5.0, 5.3, 5.1, 4.9, 5.2],
    "AOV": [18, 19, 20, 21, 20, 22],
    "CAC": [12, 11, 10, 10, 9, 10],
    "Abandono_Carrito": [45, 44, 42, 40, 38, 36],
    "Ingresos": [45000, 47000, 48000, 50000, 52000, 55000]
}
df = pd.DataFrame(data)

# Inicializar la aplicación Dash
app = Dash(__name__)

# Layout del Dashboard
app.layout = html.Div([
    html.H1("Dashboard Interactivo - Café Santo Domingo", style={"textAlign": "center"}),

    # Gráfico 1: Tasa de Conversión
    dcc.Graph(
        id="tasa-conversion",
        figure=px.line(df, x="Mes", y="Tasa_Conversion", title="Tasa de Conversión por Mes", markers=True)
    ),

    # Gráfico 2: AOV por Mes
    dcc.Graph(
        id="aov",
        figure=px.bar(df, x="Mes", y="AOV", title="Valor Promedio de Pedido (AOV)")
    ),

    # Gráfico 3: Tasa de Abandono de Carrito
    dcc.Graph(
        id="abandono-carrito",
        figure=px.line(df, x="Mes", y="Abandono_Carrito", title="Tasa de Abandono de Carrito", markers=True)
    ),

    # Gráfico 4: CAC vs Ingresos
    dcc.Graph(
        id="cac-vs-ingresos",
        figure=px.bar(df, x="Mes", y=["CAC", "Ingresos"], title="CAC vs Ingresos", barmode="group")
    )
])

# Ejecutar el servidor
if __name__ == '__main__':
    app.run_server(debug=True)