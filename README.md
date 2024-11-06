# Dokumentacja cz1 projektu
## Temat: Przewidywanie zachorowań na Covid19

Dane zostały zaczerpnięte 2 dataset na stronie Kaggle.com:
- [covid19_symptoms_dataset](https://www.kaggle.com/datasets/takbiralam/covid19-symptoms-dataset) 
- [covid19_symptoms_classification](https://www.kaggle.com/datasets/zhiruo19/covid19-symptoms-classification)
\
Datasety zawierają po kolei 2576 oraz 2000 rekordów

## Zdefiniowanie struktury i głównych komponentów projektu.
#### Ze względu na to, iż projekt jest wykonywany w parze oba dataset zostały scalone

### Po scaleniu:
- Dane zawierają kolumny tj. fever, bodypain, age, runnynose, diffbreath, infected
- Wszystkie kolumny są nominalne, brak pustych wartości.
- Jest 6 wierszy oraz 4574 rekordów

## Przygotowanie repozytorium GitHub, stworzenie backlogu projektu.

- Na potrzeby tego projektu została utworzona nowa organizacja a w niej ten projekt
- Repozytorium jest publiczne
- Został stworzony backlog projektu 
 
## Skrytpy w projekcie
### Skrypt split_data.py, który:
- Pobieraja dwa dataset z Kaggle.com
- Łączy oba dataset ze sobą zamieniając przy tym odpowiednio nagłówki kolumn
- Dzieli nowopowstały dataset combined.csv na train.csv oraz test.csv
- Zapisuje wszystkie 3 pliki

### Skrypt upload.py, który:
- Odczytuje zawartość wygenerowanych plików csv
- Wstawia dane z combined.csv, train.csv oraz test.csv do przygotowaneg google sheet do odpowiednich arkuszy data, train, set
#### Uwierzytelnianie następuje za pomocą crediancials oraz google_sheet_id