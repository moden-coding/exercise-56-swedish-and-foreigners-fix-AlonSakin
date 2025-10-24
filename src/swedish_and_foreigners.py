#!/usr/bin/env python3

import pandas as pd

def swedish_and_foreigners():
    municipalities = pd.read_csv("src/municipal.tsv", sep="\t", index_col=0)["Akaa":"Äänekoski"]

    municipalities = municipalities[municipalities["Share of Swedish-speakers of the population, %"] > 5]
    municipalities = municipalities[municipalities["Share of foreign citizens of the population, %"] > 5]

    return municipalities[["Population","Share of Swedish-speakers of the population, %","Share of foreign citizens of the population, %"]]


def main():
    print(swedish_and_foreigners())

if __name__ == "__main__":
    main()
