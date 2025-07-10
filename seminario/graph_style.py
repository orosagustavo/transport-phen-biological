import seaborn as sns
def apply_authentic_seaborn_style(dark_mode=True):
    """
    Aplica uma estilização autêntica aos gráficos Seaborn/Matplotlib de Gustavo,
    integrando ciência, tecnologia, biologia e música em um tema coeso.
    Args:
        dark_mode (bool): Se True, aplica um tema escuro. Se False, aplica um tema claro.
                          (Padrão: True, para refletir o ambiente de VSCode/Linux).
    """

    if dark_mode:
        # Paleta de Cores para Modo Escuro
        colors = [
            "#5DADE2",  # Azul Celeste 
            "#2ECC71",  # Verde Esmeralda 
            "#BB86FC",  # Roxo Digital 
            "#F1C40F",  # Amarelo Ouro 
            "#EC7063",  # Vermelho Coral 
            "#3498DB",  # Azul Secundário 
            "#9B59B6"   # Roxo Secundário 
        ]
        text_color = "#E0E0E0"  # Branco Suave
        bg_color = "#012340"    # Fundo Escuro (similar ao VSCode)
        grid_color = "#363636"  # Linhas de grade mais escuras
        spine_color = "#555555" # Borda dos eixos
    else:
        # Paleta de Cores para Modo Claro (adaptação da escura para contraste)
        colors = [
            "#3498DB",  # Azul Principal
            "#27AE60",  # Verde Principal
            "#8E44AD",  # Roxo
            "#E67E22",  # Laranja (alternativa ao amarelo ouro)
            "#C0392B",  # Vermelho
            "#5DADE2",  # Azul Secundário
            "#2ECC71"   # Verde Secundário
        ]
        text_color = "#2C3E50"  # Azul escuro quase preto
        bg_color = "#F8F8F8"    # Fundo muito claro
        grid_color = "#E0E0E0"  # Linhas de grade claras
        spine_color = "#BBBBBB" # Borda dos eixos

    sns.set_palette(colors)

    # Configurações do tema principal com sns.set_theme
    sns.set_theme(
        style="darkgrid" if dark_mode else "whitegrid", # darkgrid para o tema escuro, whitegrid para o claro
        rc={
            # Cores de Fundo e Texto
            "figure.facecolor": bg_color,
            "axes.facecolor": bg_color,
            "text.color": text_color,
            "axes.labelcolor": text_color,
            "xtick.color": text_color,
            "ytick.color": text_color,

            # Linhas de Grade e Eixos
            "grid.color": grid_color,
            "grid.linestyle": ":",  # Pontilhada para ser sutil e tecnológica
            "axes.edgecolor": spine_color, # Cor das bordas dos eixos
            "axes.linewidth": 0.8,         # Espessura sutil da borda
            

            # Fontes para Clareza e Profissionalismo (inspirado em ambientes de código)
            "font.family": "monospace" if dark_mode else "sans-serif", # Fonte monospace para toque tech no dark mode
            "font.sans-serif": ['DejaVu Sans', 'Arial', 'Helvetica'],
            "font.size": 12,
            "axes.titlesize": 18,
            "axes.labelsize": 14,
            "xtick.labelsize": 11,
            "ytick.labelsize": 11,
            "legend.fontsize": 10,
            "figure.titlesize": 20, # Título da figura mais proeminente

            # Estilo de Linhas e Marcadores (dados científicos e fluidos)
            "lines.linewidth": 2.5,
            "lines.markersize": 7,
            "scatter.edgecolors": text_color, # Borda nos pontos de dispersão
            "scatter.marker": 'o',            # Marcador padrão redondo

            # Ajustes para legendas
            "legend.frameon": False, # Sem moldura na legenda
            "legend.numpoints": 1,   # Um ponto por item na legenda

            # Melhorar a visibilidade de ticks menores
            "xtick.minor.visible": True,
            "ytick.minor.visible": True,
            "xtick.major.width": 1.0,
            "ytick.major.width": 1.0,
            "xtick.minor.width": 0.6,
            "ytick.minor.width": 0.6,
            "xtick.direction": "out",
            "ytick.direction": "out",
        }
    )

    print(f"Estilo pessoal Seaborn aplicado com sucesso (Modo {'Escuro' if dark_mode else 'Claro'})!")