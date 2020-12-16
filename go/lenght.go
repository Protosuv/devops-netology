package main

import "fmt"

var lenght float32 = 0.3048 // длина одного метра в футах

func main() {
	fmt.Println("Введите длину в метрах: ")
	var input float32
	fmt.Scanf("%f", &input)

	output := input / lenght

	fmt.Println("Длина в футах: ", output)
}
