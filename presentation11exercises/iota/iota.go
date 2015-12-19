package main

import (
	"fmt"
	)

const (
  A = iota
  B = iota * 10
  RandomNumber = iota * 2
)

func main() {
  fmt.Println(A)
  fmt.Println(B)
  fmt.Println(RandomNumber)
}
