# %%
import geopandas as gpd
from pathlib import Path
import pyogrio
import matplotlib as plt

#%%

OUTPUT = Path("../data/processed/cobertura.gpkg")

OUTPUT.parent.mkdir(
    parents=True,
    exist_ok=True
)

#%%

def processar_cobertura(arquivo, operadora, tecnologia, dbm):
    '''

    Geo data frame carrega o arquivo shb
    Cria um pacote com os dados de cada tecnologia e operadora
    Cria a camada dentro do geopackage
    
    "'''
    gdf = gpd.read_file(arquivo)

    # Adiciona os dados do pacote
    gdf["operadora"] = operadora
    gdf["tecnologia"] = tecnologia
    gdf["dbm"] = dbm

    # Cria automaticamente o nome da camada
    camada = f"{operadora.lower()}_{tecnologia.lower()}_{abs(dbm)}"

    # Salva dentro do GeoPackage
    gdf.to_file(
        OUTPUT,
        layer=camada,
        driver="GPKG"
    )
#%%

processar_cobertura(
    "../data/raw/claro/2g/pred_2G_CLARO_dbm-82.zip",
    "CLARO",
    "2G",
    -82
)

processar_cobertura(
    "../data/raw/claro/2g/pred_2G_CLARO_dbm-95.zip",
    "CLARO",
    "2G",
    -95
)

#%%

processar_cobertura(
    "../data/raw/tim/2g/pred_2G_TIM_dbm-82.zip",
    "TIM",
    "2G",
    -82
)

processar_cobertura(
    "../data/raw/tim/2g/pred_2G_TIM_dbm-95.zip",
    "TIM",
    "2G",
    -95
)

processar_cobertura(
    "../data/raw/vivo/2g/pred_2G_VIVO_dbm-82.zip",
    "VIVO",
    "2G",
    -82
)

processar_cobertura(
    "../data/raw/vivo/2g/pred_2G_VIVO_dbm-95.zip",
    "VIVO",
    "2G",
    -95
)

#%%

processar_cobertura(
    "../data/raw/claro/4g/pred_4G_CLARO_dbm-90.zip",
    "CLARO",
    "4G",
    -90
)

processar_cobertura(
    "../data/raw/claro/4g/pred_4G_CLARO_dbm-110.zip",
    "CLARO",
    "4G",
    -110
)

processar_cobertura(
    "../data/raw/tim/4g/pred_4G_TIM_dbm-90.zip",
    "TIM",
    "4G",
    -90
)

processar_cobertura(
    "../data/raw/tim/4g/pred_4G_TIM_dbm-110.zip",
    "TIM",
    "4G",
    -110
)

processar_cobertura(
    "../data/raw/vivo/4g/pred_4G_VIVO_dbm-90.zip",
    "VIVO",
    "4G",
    -90
)

processar_cobertura(
    "../data/raw/vivo/4g/pred_4G_VIVO_dbm-110.zip",
    "VIVO",
    "4G",
    -110
)

#%%

claro_82 = gpd.read_file(
    "../data/processed/cobertura.gpkg",
    layer="claro_2g_82"
)

print(claro_82)

claro_82.plot()
plt.show()