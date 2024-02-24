#include <iostream>
using namespace std;
template <typename Type>
void Production(Type* array, size_t n)
{
	Type main_prod;
	size_t counter = 0;
	size_t IndexMin = 0;
	size_t IndexMax = 0;
	for (size_t i = 0; i < n; i++) {
		if (array[i] < array[IndexMin]) IndexMin = i;
		else if (array[i] > array[IndexMax]) IndexMax = i;
	}
	if (IndexMax < IndexMin) {
		auto temp = IndexMin;
		IndexMin = IndexMax;
		IndexMax = temp;
	}
	for (size_t i = IndexMin + 1; i < IndexMax; i++) {
		if (counter == 0) main_prod = 1;
		main_prod *= array[i];
		counter += 1;
	}
	if (counter == 0)
		cout << endl << "Не получилось вычислить ответ, нет элементов между максимальным и минимальным элементами" << endl;
	else
		cout << endl << "Конечное произведение = " << main_prod << endl;
}
template <typename Type>
void Решение()
{
	Type* array = nullptr;
	size_t n;
	cout << endl << "Введите размер массива: " << endl;

	cin >> n;
	if (n <= 0)
	{
		if (n == 0)
		{
			cout << "Массив пуст." << endl;
			return;
		}
		throw "ОШИБКА: Длина массива не может быть меньше 0.";
	}
	array = new Type[n];
	cout << endl << "Введите через пробел все элементы массива" << endl;
	for (size_t i = 0; i < n; i++)
	{
		cout << "Введите " << i + 1 << " элемент массива: ";
		cin >> array[i];
	}
	Production<Type>(array, n);
}
int main()
{
	setlocale(LC_ALL, "ru");
	int flag;
	cout << "=== Выберите тип массива: ===\n1) int \n2) float \n3) double" << endl;
	cin >> flag;
	switch (flag)
	{
		case 1: Решение<int>(); break;
		case 2: Решение<float>(); break;
		case 3: Решение<double>(); break;
		default: { cout << "Ошибка: Неизвестная команда." << endl; return 1; }
	}
	return 0;
}