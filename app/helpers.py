import pyproj
import pandas as pd
import numpy as np
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def lamber93_to_gps(x: int, y: int):
    lambert = pyproj.Proj(
        "+proj=lcc +lat_1=49 +lat_2=44 +lat_0=46.5 +lon_0=3 +x_0=700000 +y_0=6600000 +ellps=GRS80 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs"
    )
    wgs84 = pyproj.Proj("+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs")
    long, lat = pyproj.transform(lambert, wgs84, x, y)
    return long, lat


def get_coverage(city: str)-> dict | None:
    df = pd.read_csv("app/data_source/out_v3.csv")
    df["result_city"] = df["result_city"].astype(str)
    df["result_postcode"] = df["result_postcode"].astype(int)
    df = df[(df["result_city"] == city)]

    df_grouped = df.groupby(["operator_name"]).agg(
        {"2G": "mean", "3G": "mean", "4G": "mean"}
    )
    df_grouped["2G"] = df_grouped["2G"].apply(lambda x: 1 if x > 0 else 0)
    df_grouped["3G"] = df_grouped["3G"].apply(lambda x: 1 if x > 0 else 0)
    df_grouped["4G"] = df_grouped["4G"].apply(lambda x: 1 if x > 0 else 0)

    if len(df_grouped) == 0:
        return None
    dict_result = df_grouped.to_dict(orient="index")
    result = [{key: dict_result[key]} for key in dict_result]
    return result
