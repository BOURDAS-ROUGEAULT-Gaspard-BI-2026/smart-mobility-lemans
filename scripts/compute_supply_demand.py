import pandas as pd

# 1. Charger les fréquences d'arrêts et les communes
df_stops = pd.read_csv("data/gtfs_static/stops_frequency.csv")
df_communes = pd.read_csv("data/reference/communes.csv")

# 2. Sommer les passages quotidiens par commune
supply_per_commune = (
    df_stops.groupby("nearest_commune")["daily_trip_count"]
    .sum()
    .reset_index()
)

# 3. Fusionner avec la population
df_merged = pd.merge(
    df_communes,
    supply_per_commune,
    left_on="commune",
    right_on="nearest_commune",
    how="left",
).fillna(0)

# 4. Calculer la métrique : nombre de passages pour 1 000 habitants
df_merged["trips_per_1000_pop"] = (
    df_merged["daily_trip_count"] / (df_merged["population"] / 1000)
).round(1)

# 5. Trier par métrique décroissante
df_merged = df_merged.sort_values("trips_per_1000_pop", ascending=False)

# Exporter le résultat
df_merged[
    [
        "commune",
        "population",
        "daily_trip_count",
        "trips_per_1000_pop",
    ]
].to_csv("data/gtfs_static/commune_supply_demand.csv", index=False)

print("Classement Offre / Demande par commune :")
print(
    df_merged[
        [
            "commune",
            "population",
            "daily_trip_count",
            "trips_per_1000_pop",
        ]
    ].to_string(index=False)
)
