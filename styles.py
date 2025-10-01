import plotly.graph_objects as go

def boxplot_style(fig, n_cols, height=400, width=1125, gridcolor='lightgrey', gridwidth=0.5, ticklabels=True):

    fig.update_layout(
        height=height,
        width=width,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=50, r=50, t=50, b=50)
    )
    
    for i in range(1, n_cols+1):
        fig.update_yaxes(
            showticklabels=ticklabels,
            showgrid=True,
            gridcolor=gridcolor,
            gridwidth=gridwidth,
            row=1, col=i
        )
        fig.update_xaxes(showticklabels=False, row=1, col=i)
    
    return fig


def heatmap_style(fig, height=500, width=700, gridcolor='lightgrey', gridwidth=0.5):
    fig.update_layout(
        height=height,
        width=width,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(l=50, r=50, t=50, b=50)
    )
    
    fig.update_xaxes(showgrid=True, gridcolor=gridcolor, gridwidth=gridwidth)
    fig.update_yaxes(showgrid=True, gridcolor=gridcolor, gridwidth=gridwidth)
    
    return fig