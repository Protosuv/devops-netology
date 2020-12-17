//
package main

import "fmt"

func main() {
	var divider int = 3 // делитель
	var vol int = 100
	var x []int // объявляем срез, т.к неизвестна длина

	for i := 0; i < vol; i++ {
		var y int = i % divider
		//fmt.Println(y, i) // Для отладки
		if y == 0 {
			x = append(x, i) //Добавление элемента в срез
			fmt.Println(i)
		}
	}
	fmt.Println("Итоговый массив чисел делящихся на 3: ", x)
	fmt.Println("Длина массива: ", len(x), "числа.")
}
