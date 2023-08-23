countries_data = [
    {
        'country': 'Country1',
        'population': 100000000,
        'languages': ['Language1', 'Language2', 'Language3']
    },
    {
        'country': 'Country2',
        'population': 90000000,
        'languages': ['Language2', 'Language4']
    },
]
from operator import itemgetter

# Suponiendo que tienes los datos en un archivo llamado "countries_data.py"
from countries_data import countries_data

# a) Calcular el número total de idiomas en los datos
all_languages = set()
for country in countries_data:
    all_languages.update(country['languages'])
total_languages = len(all_languages)
print("Número total de idiomas:", total_languages)

# b) Encontrar los diez idiomas más hablados a partir de los datos
language_counts = {}
for country in countries_data:
    for language in country['languages']:
        language_counts[language] = language_counts.get(language, 0) + 1
top_10_languages = sorted(language_counts.items(), key=itemgetter(1), reverse=True)[:10]
print("Los diez idiomas más hablados:")
for language, count in top_10_languages:
    print(f"{language}: {count}")

# c) Encontrar los 10 países más poblados del mundo
top_10_countries = sorted(countries_data, key=itemgetter('population'), reverse=True)[:10]
print("Los 10 países más poblados del mundo:")
for country in top_10_countries:
    print(f"{country['country']}: {country['population']}")
