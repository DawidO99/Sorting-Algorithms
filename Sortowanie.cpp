#include <iostream>
#include <fstream>
#include <vector>
#include <chrono>
#include "algorytmy.h"
void menu();
void print(std::vector<int>w);
void read(std::vector<int>& w, int n);

int main()
{
	std::vector<int> w;
	int num, n;
	std::cout << "Podaj liczbe danych wejsciowych : " << std::endl;
	std::cin >> n;
	while (true)
	{
		menu();
		std::cout << "Wybierz algorytm : " << std::endl;
		std::cin >> num;
		switch (num)
		{
		case 1:
		{
			read(w, n);
			insert_sort(w);
			std::cout << "Posortowano : " << std::endl;
			print(w);
			w.clear();
			break;
		}
		case 2:
		{
			read(w, n);
			selection_sort(w);
			std::cout << "Posortowano : " << std::endl;
			print(w);
			w.clear();
			break;
		}
		case 3:
		{
			read(w, n);
			bubble_sort(w);
			std::cout << "Posortowano : " << std::endl;
			print(w);
			w.clear();
			break;
		}
		case 4:
		{
			read(w, n);
			quick_sort(w, 0, w.size() - 1);
			std::cout << "Posortowano : " << std::endl;
			print(w);
			w.clear();
			break;
		}
		case 5:
		{
			read(w, n);
			shell_sort(w);
			std::cout << "Posortowano : " << std::endl;
			print(w);
			w.clear();
			break;
		}
		case 6:
		{
			read(w, n);
			heap_sort(w);
			std::cout << "Posortowano : " << std::endl;
			print(w);
			w.clear();
			break;
		}
		default:
			std::cout << "Zakonczenie dzialania programu" << std::endl;
			return 0;
		}
	}
}

void menu()
{
	std::cout << "1. Sortowanie przez wstawianie" << std::endl;
	std::cout << "2. Sortowanie przez selekcje" << std::endl;
	std::cout << "3. Sortowanie babelkowe" << std::endl;
	std::cout << "4. Quicksort" << std::endl;
	std::cout << "5. Sortowanie Shella" << std::endl;
	std::cout << "6. Heapsort" << std::endl;
	std::cout << "Dowolny inny klawisz - zakonczenie pracy programu." << std::endl;
}

void read(std::vector<int>& w, int n)
{
	std::fstream file("dane", std::ios::in);
	int num;
	int ile = 0;
	while (n > 0)
	{
		file >> num;
		ile++;
		w.push_back(num);
		n--;
	}
	std::cout << "Dane wejsciowe  : " << std::endl;
	std::cout << "Wczytano : " << ile << " liczb" << std::endl;
	print(w);
	file.close();
}

void print(std::vector<int>w)
{
	for (auto el : w)
		std::cout << el << " ";
	std::cout << std::endl;
}