package main

import "fmt"

//var lenght int = 3

func main() {
	fmt.Println("Введите число: ")
	var input int
	fmt.Scanf("%d", &input)
	//fmt.Println(input)

	var output int = input % 2
	fmt.Println(output)
	if output > 0 {
		fmt.Println(output)
	}
}
