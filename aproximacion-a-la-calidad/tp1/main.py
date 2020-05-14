#!/usr/bin/env python3
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy
from scipy.stats import chi2_contingency


def main():
    categorical = [
        "Car", "Car_desc", "Jur", "Jur_desc", "Sjur", "Sjur_desc", "Ent", "Ent_desc", "Og", "Og_desc", "UE", "UE_desc", "Prog", "Prog_desc", "Sprog", "Sprog_desc", "Proy", "Proy_desc", "Actividad", "Act_desc", "Ob", "ob_desc", "Fin", "Fin_desc", "Fun", "Fun_desc", "Inc", "Inc_desc", "Ppal", "Ppal_desc", "Par", "Par_desc", "Spar", "Spar_desc", "Eco", "Eco_desc", "Fte", "Fte_desc", "Geo", "Geo_desc",
    ]

    categoricalIds = list(
        filter(lambda text: not text.endswith("_desc"), categorical))
    categoricalDesc = list(
        filter(lambda text: text.endswith("_desc"), categorical))

    nonCategorical = [
        "Sanción", "Vigente", "Definitivo", "Devengado"
    ]

    types = {var: "category" for var in categorical}

    data = pd.read_csv("dataset.csv", dtype=types)

    print(data[nonCategorical].describe())

    # plt.show(data[nonCategorical].boxplot())

    # print(data[categoricalIds].describe())
    # print(pd.value_counts(data[categoricalIds]))
    # print(data[categoricalDesc].describe())
    # print(data[categoricalDesc].describe().loc[["unique", "count"]])

    # j jfor var in ["Car_desc"]:
    #   print(pd.value_counts(data[var]))

    # print(data.loc[data['Definitivo'] == 0, 'Definitivo'].count())

    # todas
    # jfor var in categoricalDesc:
    #    print(pd.value_counts(data[var]))

    # plt.show(data[nonCategorical].plot())

    crosstable = pd.crosstab(data["Car_desc"], data["Jur_desc"])
    print(crosstable)
    print(chi2_contingency(crosstable)[0])
    print(chi2_contingency(crosstable)[1])


if __name__ == "__main__":
    main()
