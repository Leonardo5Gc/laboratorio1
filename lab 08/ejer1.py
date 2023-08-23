import countries_data

# otro_archivo.py
from countries_data import los_idiomas_mas_hablados, los_paises_mas_poblados

# Supongamos que tienes la lista de países (countries) aquí
# countries = [...]

top_languages = los_idiomas_mas_hablados()
print("Top 10 most spoken languages:")
for lang, count in top_languages:
    print(f"{lang}: {count} countries")

top_populated_countries = los_paises_mas_poblados()
print("\nTop 10 most populated countries:")
for country in top_populated_countries:
    print(f"{country['name']}: {country['population']} people")
