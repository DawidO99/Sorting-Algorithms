 #include <iostream>
#include <vector>
#include "algorytmy.h"

void insert_sort(std::vector<int>&w)
{
	int pom, j;
	for (int i = 1; i < w.size(); i++)
	{
		pom = w[i];
		j = i - 1;
		while (j >= 0 && w[j] > pom)
		{
			w[j + 1] = w[j];
			j--;
		}
		w[j + 1] = pom;
	}
}

void selection_sort(std::vector<int>& w)
{
	int pom;
	for (int i = 0; i < w.size() - 1; i++)
	{
		pom = i;
		for (int j = i + 1; j < w.size(); j++)
			if (w[j] < w[pom])
				pom = j;
		std::swap(w[i], w[pom]);
	}
}

void bubble_sort(std::vector<int>& w)
{
	for (int i = 0; i < w.size(); i++)
		for (int j = 1; j < w.size() - i; j++)
			if (w[j - 1] > w[j])
				std::swap(w[j - 1], w[j]);
}

void quick_sort(std::vector<int>& w, int left, int right)
{
	if (right <= left)
		return;
	int i = left, j = right;
	int pivot = w[(left + right) / 2];
	while (i <= j)
	{
		while (w[i] < pivot)
			i++;
		while (w[j] > pivot)
			j--;
		if (i <= j)
		{
			std::swap(w[i], w[j]);
			i++;
			j--;
		}
	}
	if (left < j)
		quick_sort(w, left, j);
	if (i < right)
		quick_sort(w, i, right);
}


void shell_sort(std::vector<int>& w)
{
	int pom;
	for (int i = w.size() / 2; i > 0; i /= 2)
	{
		for (int j = i; j < w.size(); j++)
		{
			int k;
			pom = w[j];
			for (k = j; k >= i && w[k - i] > pom; k -= i)
				w[k] = w[k - i];
			w[k] = pom;
		}
	}
}

void heap_sort(std::vector<int>& w)
{
	for (int i = w.size() / 2 - 1; i >= 0; i--)
		call_heap(w, w.size(), i);
	for (int i = w.size() - 1; i > 0; i--)
	{ 
		std::swap(w[0], w[i]);
		call_heap(w, i, 0);
	}
}

void call_heap(std::vector<int>& w, int n, int i)
{
	int max = i, left = 2 * i + 1, right = 2 * i + 2;
	if (left < n && w[left] > w[max])
		max = left;
	if (right < n && w[right] > w[max])
		max = right;
	if (max != i) 
	{
		std::swap(w[i], w[max]);
		call_heap(w, n, max);
	}
}