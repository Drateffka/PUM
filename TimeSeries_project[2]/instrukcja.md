# Instrukcje

Termin: 18 maja 12.18

Zadanie polega na przeprowadzeniu analizy i predykcji szeregów czasowych dotyczących poziomu pyłu zawieszonego przy użyciu modelu XGBoost. Pył PM10 i PM2.5 to drobne cząstki stałe lub ciekłe zawieszone w powietrzu, których średnica wynosi odpowiednio 10 lub mniej i 2,5 mikrometra lub mniej.

Zanieczyszczenie powietrza tymi cząsteczkami stanowi istotny problem dla zdrowia publicznego, ponieważ może przenikać głęboko do płuc i układu krwionośnego, co ma negatywny wpływ na zdrowie. Predykcja zawartości PMx w powietrzu pozwoli na lepsze planowanie i informowanie ludności o potencjalnych zagrożeniu.

## Część 1: Przygotowanie danych i inżynieria cech (20 punktów)

1. **Tworzenie cech**: Utwórz cechy (features) w oknach czasowych oraz cechy oparte na opóźnieniach wartości pyłu PM2.5 w celu uwzględnienia historii w predykcji. Dodatkowo, wykorzystaj informacje z datatime do tworzenia dodatkowych cech, takich jak dzień tygodnia, miesiąc, rok itp. Uzasadnij swój wybór. Czy jest możliwe uwzględnienienie czynnika przestrzennego w tworzeniu cech? (15 punktów)
2. **Podział zbioru danych**
Podziel zbiór danych szeregów czasowych na zestawy treningowy i testowe, zachowując chronologię danych. Pamiętaj, że posiadasz dane o charakterystyce czasowo-przestrzennej. Wykorzystaj ten podział do wstępnej oceny działania modelu. (5 punktów)

Notatki Ania:
PM2.5 na terenie całej Polski w 2019, źródło to GIOŚ. Jest dużo NULLi, bo GIOŚ nie uzupełnia.
Do tej pory był 1 szereg czasowy (Bydgoszcz), a tutaj będzie jeszcze rozmieszczenie czujników w przestrzeni. GIOŚ nie daje informacji gdzie one są zlokalizowane - jest info gdzie stacja, ale nie ma dokładnej lokalizacji. Trzeba ręcznie wyszukać współrzędne.

1. Jak uzupełnić wartości brakujące? Trend? Wartości w innych bliskich czujnikach? Jak to optymalnie robić na swoim komputerze?
2. Jak predykować? Można dla jednego czujnika i potem w pętli dla wszystkich i wyciągnąć średnią.

Trzeba uzasadnić wybór feature'ów.

## Część 2: Tworzenie modelu do predykcji (20 punktów)

1. **Inicjalizacja i trenowanie modelu.**
W tym ćwiczeniu do predykcji będziemy używaż algorytmu XGB (Extreme Gradient Boosting).
 Zainicjuj i wytrenuj model na danych uczących. Napisz plusy i minusy wykorzystania tego algorytmu w kontekście predykcji szeregów czasowych w formie zwięzłej tabeli (10 punktów)
2. **Tuning hiperparametrów**
Wykonaj tuning hiperparametrów poprzez trening i walidację krzyżową w celu znalezienia optymalnych wartości hiperparametrów. Napisz  czym są hiperparametry i dlaczego wymagają tuningu. (10 punktów)

Notatki Ania:
Kolejna część do predykcja przy użyciu algorytmu xgboost.

## Część 3: Backtesting (20 punktów)

1. **Podział na okna czasowe**
Podziel dane na wiele okien czasowych, na przykład poprzez użycie walk-forward lub roll-forward validation lub gap-roll-forward validation, aby uzyskać rzeczywistą ocenę wydajności modelu na przyszłych danych. Napisz na czym polega ten sposób walidacji i po co się go wykonuje. (10 punktów)
2. **Ocena wydajności**
Przeprowadź backtesting modelu, czyli ocenę wydajności modelu na danych historycznych, które nie zostały użyte do trenowania. Czym rózni się backtesting od testowania wydajności modelu dla danych niebędących szeregami czasowymi? (10 punktów)

Notatki Ania:
Backtesting.
Cross-walidacja szeregów czasowych.

Jak to zrobić i uzasadnić wybór.

## Część 4: Analiza istotności cech (20 punktów)

1. **Wyliczenie istotności cech**
Wykorzystaj wbudowane narzędzia do wyliczenia istotności cech w modelu (Feature Importance). (5 punktów)
2. **Interpretacja wyników**
Zinterpretuj istotność cech w kontekście dostępnych informacji - artykułów naukowych,  dokumentacji biblioteki itp.
(15 punktów)

Notatki Ania:
Analiza istotności cech wchodzących do algorytmu. Dlaczego ten algorytm bierze konkretną cechę jako najbardziej użyteczną do predykcji? Dokumentacja algorytmu.

## Część ogólna (10 punktów)

- Zgodność kodu z PEP-8 oraz elegancja kodu
- Ogólna interpretacja wyników
- Skuteczność i precyzja
- Oceniając wyniki backtestingu, skup się na skuteczności i precyzji predykcji modelu
- Kreatywność i innowacyjność
- Oceniając analizę istotności cech oraz tworząć cechy poszukaj kreatywnych i innowacyjnych sposobów działania.
- Strona edytorska
- Do oceny przekaż tylko finalny kod oraz interpretację. Pamiętaj o staranności edytorskiej

Ma być pep8, przejrzystość. Sprawozdanie ma być oczywiście bezosobowe. (10pkt)
Terminowe oddane. (10 pkt)

## Oddanie projektu w terminie określonym w systemie (10 punktów)

Za cały projekt możesz otrzymać maksymalnie 100 punktów co stanowi 100%. Ocena za projekt wyliczana jest zgodnie z regulaminem studiów AGH:
od 90%  bardzo dobry (5.0);
od 80%  plus dobry (4.5);
od 70%  dobry (4.0);
od 60%  plus dostateczny (3.5);
od 50%  dostateczny (3.0);
poniżej 50%  niedostateczny (2.0).

Forma oddania projektu - wydruk jupyter notebook w formacie .pdf
