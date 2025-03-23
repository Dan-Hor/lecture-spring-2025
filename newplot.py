import plotly.graph_objects as go


def plot(a, b, c, d, e, f):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=a, y=b, name=c))
    fig.update_layout(title=d, xaxis_title=e, yaxis_title=f)
    fig.show()
