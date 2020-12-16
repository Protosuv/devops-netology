package main

import "fmt"

func main() {
	sum := 0
	for i := 0; i < 100; i++ {
		sum += i
		if (i >= 50) && (i <= 55) {
			fmt.Println(i)
		}
	}
	fmt.Println("Сумма равна ", sum)

	var a [2]string
	a[0] = "Привет"
	a[1] = "Tproger"
	fmt.Println(a[0], a[1])
	//fmt.Println(a)

	//primes := [6]int{2, 3, 5, 7, 11, 13}
	//fmt.Println(primes[2])

	primes2 := [6]int{2, 3, 5, 7, 11, 13}
	fmt.Println(primes2)

	var s []int = primes2[1:4]
	fmt.Println(s)
}
