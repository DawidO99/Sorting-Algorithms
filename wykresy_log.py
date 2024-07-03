import matplotlib.pyplot as plt

# Ilość danych
ilosc_danych = [1000, 5000, 10000, 25000, 50000, 75000, 100000, 250000, 500000, 750000, 1000000]

### Metoda sortowania: Insertion Sort

#### Dla danych losowych:

# Czasy wykonania dla danych losowych
czas_insertion_random = [3801, 98682, 290986, 1858830, 7412865, 16620587, 29548876, 184938412, 741290369, 1666851713, 2976380484]
czas_insertion_random = [czas/1000000 for czas in czas_insertion_random]  # konwersja mikrosekund na sekundy

#### Dla danych posortowanych:

# Czasy wykonania dla danych posortowanych
czas_insertion_sorted = [16, 91, 152, 383, 832, 1171, 1656, 4090, 7836, 11733, 15456]
czas_insertion_sorted = [czas/1000000 for czas in czas_insertion_sorted]  # konwersja mikrosekund na sekundy

#### Dla danych posortowanych malejąco:

# Czasy wykonania dla danych posortowanych malejąco
czas_insertion_sorted_reversed = [6253, 218203, 594569, 3712185, 14939171, 33259822, 59136263, 370317886, 1480721624, 3332485390, 5947033617]
czas_insertion_sorted_reversed = [czas/1000000 for czas in czas_insertion_sorted_reversed]  # konwersja mikrosekund na sekundy


### Metoda sortowania: Selection Sort

#### Dla danych losowych:

# Czasy wykonania dla danych losowych
czas_selection_random = [6414, 191184, 552656, 3443387, 13778163, 30873357, 54905409, 343889877, 1374844823, 3119340846, 5525115348]
czas_selection_random = [czas/1000000 for czas in czas_selection_random]  # konwersja mikrosekund na sekundy

#### Dla danych posortowanych:

# Czasy wykonania dla danych posortowanych
czas_selection_sorted = [6291, 150509, 551008, 3452348, 13822811, 31228759, 54856864, 344589399, 1373057638, 3100946863, 5515914164]
czas_selection_sorted = [czas/1000000 for czas in czas_selection_sorted]  # konwersja mikrosekund na sekundy

#### Dla danych posortowanych malejąco:

# Czasy wykonania dla danych posortowanych malejąco
czas_selection_sorted_reversed = [6921, 163464, 555538, 3461726, 13725840, 30893192, 55044859, 344715796, 1373601651, 3121531049, 5518839752]
czas_selection_sorted_reversed = [czas/1000000 for czas in czas_selection_sorted_reversed]  # konwersja mikrosekund na sekundy


### Metoda sortowania: Bubble Sort

#### Dla danych losowych:

# Czasy wykonania dla danych losowych
czas_bubble_random = [10914, 275756, 956154, 6043220, 24200366, 54155427, 96531854, 601637676, 2405523295, 5468798817, 9657706379]
czas_bubble_random = [czas/1000000 for czas in czas_bubble_random]  # konwersja mikrosekund na sekundy

#### Dla danych posortowanych:

# Czasy wykonania dla danych posortowanych
czas_bubble_sorted = [6896, 140774, 562245, 3526903, 14103655, 31535434, 56061421, 350670887, 1401053959, 3171005080, 5661997902]
czas_bubble_sorted = [czas/1000000 for czas in czas_bubble_sorted]  # konwersja mikrosekund na sekundy

#### Dla danych posortowanych malejąco:

# Czasy wykonania dla danych posortowanych malejąco
czas_bubble_sorted_reversed = [11233, 273990, 1115367, 6982968, 27354189, 61523747, 109708134, 682300785, 2732855011, 6186422715, 10996370742]
czas_bubble_sorted_reversed = [czas/1000000 for czas in czas_bubble_sorted_reversed]  # konwersja mikrosekund na sekundy


### Metoda sortowania: Quick Sort

#### Dla danych losowych:

# Czasy wykonania dla danych losowych
czas_quick_random = [158, 766, 1596, 4778, 9314, 13876, 18802, 51138, 104418, 160993, 218131]
czas_quick_random = [czas/1000000 for czas in czas_quick_random]  # konwersja mikrosekund na sekundy

#### Dla danych posortowanych:

# Czasy wykonania dla danych posortowanych
czas_quick_sorted = [86, 460, 988, 2752, 6157, 9236, 12700, 35600, 75521, 114212, 160841]
czas_quick_sorted = [czas/1000000 for czas in czas_quick_sorted]  # konwersja mikrosekund na sekundy

#### Dla danych posortowanych malejąco:

# Czasy wykonania dla danych posortowanych malejąco
czas_quick_sorted_reversed = [90, 480, 1036, 2871, 6405, 9626, 13188, 36851, 78311, 118166, 166107]
czas_quick_sorted_reversed = [czas/1000000 for czas in czas_quick_sorted_reversed]  # konwersja mikrosekund na sekundy


### Metoda sortowania: Shell Sort

#### Dla danych losowych:

# Czasy wykonania dla danych losowych
czas_shell_random = [315, 1720, 3833, 10369, 22062, 34000, 47725, 136910, 293945, 412288,604990]
czas_shell_random = [czas/1000000 for czas in czas_shell_random]  # konwersja mikrosekund na sekundy

#### Dla danych posortowanych:

# Czasy wykonania dla danych posortowanych
czas_shell_sorted = [147, 851, 1866, 5118, 11014, 17702, 23525, 63270, 136131, 211132, 282190]
czas_shell_sorted = [czas/1000000 for czas in czas_shell_sorted]  # konwersja mikrosekund na sekundy

#### Dla danych posortowanych malejąco:

# Czasy wykonania dla danych posortowanych malejąco
czas_shell_sorted_reversed = [219, 1113, 2385, 6327, 13540, 21388, 28634, 75181, 158112, 248279, 342700]
czas_shell_sorted_reversed = [czas/1000000 for czas in czas_shell_sorted_reversed]  # konwersja mikrosekund na sekundy


### Metoda sortowania: Heap Sort

#### Dla danych losowych:

# Czasy wykonania dla danych losowych
czas_heap_random = [347, 2031, 4391, 12017, 25673, 40003, 54803, 149067, 316007, 491538, 672683]
czas_heap_random = [czas/1000000 for czas in czas_heap_random]  # konwersja mikrosekund na sekundy

#### Dla danych posortowanych:

# Czasy wykonania dla danych posortowanych
czas_heap_sorted = [361, 1908, 4021, 10891, 23073, 35925, 49545, 133330, 281221, 437384, 585870]
czas_heap_sorted = [czas/1000000 for czas in czas_heap_sorted]  # konwersja mikrosekund na sekundy

#### Dla danych posortowanych malejąco:

# Czasy wykonania dla danych posortowanych malejąco
czas_heap_sorted_reversed = [392, 4032, 4032, 11145, 24193, 37498, 51403, 140055, 297207, 461989, 631147]
czas_heap_sorted_reversed = [czas/1000000 for czas in czas_heap_sorted_reversed]  # konwersja mikrosekund na sekundy

### 1. Wykres dla 3 podstawowych algorytmów razem - dane losowe
plt.figure(figsize=(10, 6))
plt.plot(ilosc_danych, czas_insertion_random, marker='o', label='Insertion Sort')
plt.plot(ilosc_danych, czas_selection_random, marker='o', label='Selection Sort')
plt.plot(ilosc_danych, czas_bubble_random, marker='o', label='Bubble Sort')
plt.yscale('log')  # zmiana skali osi y na logarytmiczną
plt.title('Basic Sorting Algorithms - Random Data')
plt.xlabel('Number of Elements')
plt.ylabel('Time (s)')
plt.grid(True)
plt.legend()
#plt.show()

### 2. Wykres dla 3 podstawowych algorytmów razem - dane posortowane
plt.figure(figsize=(10, 6))
plt.plot(ilosc_danych, czas_insertion_sorted, marker='o', label='Insertion Sort')
plt.plot(ilosc_danych, czas_selection_sorted, marker='o', label='Selection Sort')
plt.plot(ilosc_danych, czas_bubble_sorted, marker='o', label='Bubble Sort')
plt.yscale('log')  # zmiana skali osi y na logarytmiczną
plt.title('Basic Sorting Algorithms - Sorted Data')
plt.xlabel('Number of Elements')
plt.ylabel('Time (s)')
plt.grid(True)
plt.legend()
#plt.show()

### 3. Wykres dla 3 podstawowych algorytmów razem - dane posortowane i odwrócone
plt.figure(figsize=(10, 6))
plt.plot(ilosc_danych, czas_insertion_sorted_reversed, marker='o', label='Insertion Sort')
plt.plot(ilosc_danych, czas_selection_sorted_reversed, marker='o', label='Selection Sort')
plt.plot(ilosc_danych, czas_bubble_sorted_reversed, marker='o', label='Bubble Sort')
plt.yscale('log')  # zmiana skali osi y na logarytmiczną
plt.title('Basic Sorting Algorithms - Sorted & Reversed Data')
plt.xlabel('Number of Elements')
plt.ylabel('Time (s)')
plt.grid(True)
plt.legend()
#plt.show()

### 4. Wykres dla 3 zaawansowanych algorytmów razem - dane losowe
plt.figure(figsize=(10, 6))
plt.plot(ilosc_danych, czas_quick_random, marker='o', label='Quick Sort')
plt.plot(ilosc_danych, czas_shell_random, marker='o', label='Shell Sort')
plt.plot(ilosc_danych, czas_heap_random, marker='o', label='Heap Sort')
plt.yscale('log')  # zmiana skali osi y na logarytmiczną
plt.title('Advanced Sorting Algorithms - Random Data')
plt.xlabel('Number of Elements')
plt.ylabel('Time (s)')
plt.grid(True)
plt.legend()
#plt.show()

### 5. Wykres dla 3 zaawansowanych algorytmów razem - dane posortowane
plt.figure(figsize=(10, 6))
plt.plot(ilosc_danych, czas_quick_sorted, marker='o', label='Quick Sort')
plt.plot(ilosc_danych, czas_shell_sorted, marker='o', label='Shell Sort')
plt.plot(ilosc_danych, czas_heap_sorted, marker='o', label='Heap Sort')
plt.yscale('log')  # zmiana skali osi y na logarytmiczną
plt.title('Advanced Sorting Algorithms - Sorted Data')
plt.xlabel('Number of Elements')
plt.ylabel('Time (s)')
plt.grid(True)
plt.legend()
#plt.show()

### 6. Wykres dla 3 zaawansowanych algorytmów razem - dane posortowane i odwrócone
plt.figure(figsize=(10, 6))
plt.plot(ilosc_danych, czas_quick_sorted_reversed, marker='o', label='Quick Sort')
plt.plot(ilosc_danych, czas_shell_sorted_reversed, marker='o', label='Shell Sort')
plt.plot(ilosc_danych, czas_heap_sorted_reversed, marker='o', label='Heap Sort')
plt.yscale('log')  # zmiana skali osi y na logarytmiczną
plt.title('Advanced Sorting Algorithms - Sorted & Reversed Data')
plt.xlabel('Number of Elements')
plt.ylabel('Time (s)')
plt.grid(True)
plt.legend()
#plt.show()

### 7. Wykres dla wszystkich 6 metod razem - dane losowe
plt.figure(figsize=(10, 6))
plt.plot(ilosc_danych, czas_insertion_random, marker='o', label='Insertion Sort')
plt.plot(ilosc_danych, czas_selection_random, marker='o', label='Selection Sort')
plt.plot(ilosc_danych, czas_bubble_random, marker='o', label='Bubble Sort')
plt.plot(ilosc_danych, czas_quick_random, marker='o', label='Quick Sort')
plt.plot(ilosc_danych, czas_shell_random, marker='o', label='Shell Sort')
plt.plot(ilosc_danych, czas_heap_random, marker='o', label='Heap Sort')
plt.yscale('log')  # zmiana skali osi y na logarytmiczną
plt.title('All Sorting Algorithms - Random Data')
plt.xlabel('Number of Elements')
plt.ylabel('Time (s)')
plt.grid(True)
plt.legend()
#plt.show()

### 8. Wykres dla wszystkich 6 metod razem - dane posortowane
plt.figure(figsize=(10, 6))
plt.plot(ilosc_danych, czas_insertion_sorted, marker='o', label='Insertion Sort')
plt.plot(ilosc_danych, czas_selection_sorted, marker='o', label='Selection Sort')
plt.plot(ilosc_danych, czas_bubble_sorted, marker='o', label='Bubble Sort')
plt.plot(ilosc_danych, czas_quick_sorted, marker='o', label='Quick Sort')
plt.plot(ilosc_danych, czas_shell_sorted, marker='o', label='Shell Sort')
plt.plot(ilosc_danych, czas_heap_sorted, marker='o', label='Heap Sort')
plt.yscale('log')  # zmiana skali osi y na logarytmiczną
plt.title('All Sorting Algorithms - Sorted Data')
plt.xlabel('Number of Elements')
plt.ylabel('Time (s)')
plt.grid(True)
plt.legend()
#plt.show()

### 9. Wykres dla wszystkich 6 metod razem - dane posortowane i odwrocone
plt.figure(figsize=(10, 6))
plt.plot(ilosc_danych, czas_insertion_sorted_reversed, marker='o', label='Insertion Sort')
plt.plot(ilosc_danych, czas_selection_sorted_reversed, marker='o', label='Selection Sort')
plt.plot(ilosc_danych, czas_bubble_sorted_reversed, marker='o', label='Bubble Sort')
plt.plot(ilosc_danych, czas_quick_sorted_reversed, marker='o', label='Quick Sort')
plt.plot(ilosc_danych, czas_shell_sorted_reversed, marker='o', label='Shell Sort')
plt.plot(ilosc_danych, czas_heap_sorted_reversed, marker='o', label='Heap Sort')
plt.yscale('log')  # zmiana skali osi y na logarytmiczną
plt.title('All Sorting Algorithms - Sorted & Reversed Data')
plt.xlabel('Number of Elements')
plt.ylabel('Time (s)')
plt.grid(True)
plt.legend()
#plt.show()

import pandas as pd

# Tworzenie tabel dla czasów wykonania poszczególnych algorytmów sortowania dla każdego zestawu danych
for n in ilosc_danych:
    data = {
        'Insertion Sort': [czas_insertion_random[ilosc_danych.index(n)], czas_insertion_sorted[ilosc_danych.index(n)], czas_insertion_sorted_reversed[ilosc_danych.index(n)]],
        'Selection Sort': [czas_selection_random[ilosc_danych.index(n)], czas_selection_sorted[ilosc_danych.index(n)], czas_selection_sorted_reversed[ilosc_danych.index(n)]],
        'Bubble Sort': [czas_bubble_random[ilosc_danych.index(n)], czas_bubble_sorted[ilosc_danych.index(n)], czas_bubble_sorted_reversed[ilosc_danych.index(n)]],
        'Quick Sort': [czas_quick_random[ilosc_danych.index(n)], czas_quick_sorted[ilosc_danych.index(n)], czas_quick_sorted_reversed[ilosc_danych.index(n)]],
        'Shell Sort': [czas_shell_random[ilosc_danych.index(n)], czas_shell_sorted[ilosc_danych.index(n)], czas_shell_sorted_reversed[ilosc_danych.index(n)]],
        'Heap Sort': [czas_heap_random[ilosc_danych.index(n)], czas_heap_sorted[ilosc_danych.index(n)], czas_heap_sorted_reversed[ilosc_danych.index(n)]]
    }
    
    df = pd.DataFrame(data, index=['Random', 'Sorted', 'Sorted & Reversed'])
    
    # Wyświetlenie tabeli dla danego zestawu danych
    print(f"Table for {n} elements:")
    print(df)
    print('\n')
    
    # Eksport tabeli do pliku CSV
    df.to_csv(f'sorting_algorithms_times_{n}_elements.csv')

