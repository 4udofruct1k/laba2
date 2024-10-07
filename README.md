  Лабораторная работа №2
  Функции в Python
1. Цель работы
2. Теория
  Целью работы является ознакомление с функциями и реализация программ с использованием функций.
  Для того, чтобы определить функцию потребуется написать ключевое слово def, задать имя функции, входные параметры, заключенные в скобки и в конце поставить двоеточие.
  Функция может возвращать значение с использованием ключевого
слова return.
  Функция может принимать любое количество аргументов любого типа. Она может возвращать любое количество результатов любого типа. Если функция не вызывает явно return, то вызывающая сторона получит в результате None.
  Python гибко обрабатывает аргументы функции и наиболее распространенный тип аргументов – это позиционные аргументы. Данный тип аргументов обуславливается копированием в соответствующие параметры по порядку. У данного типа аргументов есть недостаток в том, что требуется запоминать значение каждой позиции.
  Чтобы избежать путаницы с позиционными аргументами, можно указывать аргументы с помощью имен соответствующих параметров. Такие аргументы называются аргументы - ключевые слова.
  Функцию можно определить внутри другой функции и это называется внутренняя функция. Внутренние функции могут быть полезны при выполнении сложных задач более одного раза внутри другой функции. Это позволяет избежать использования циклов и дублирования кода.
  В Python лямбда-функция – это анонимная функция, выраженная в виде одного оператора. Ее можно использовать вместо обычной небольшой функции.
  В Python генератор – это объект, который предназначен для создания последовательностей. С помощью генераторов можно итерировать огромные последовательности, не создавая и не сохраняя всю последовательность в памяти сразу. Каждый раз когда происходит итерирование через генератор, он отслеживает, где находился во время последнего вызова, и возвращает следующее значение.
  Если требуется создать большую последовательность, то можно реализовать функцию-генератор. Это обычная функция, которая возвращает значение с помощью выражения yield, а не return.
3. Задание на лабораторную работу
Реализовать программы на Python с использованием функций.
