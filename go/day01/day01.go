package main

import (
	"fmt"
	"math"
	"os"
	"slices"
	"strconv"
	"strings"
)

const (
	Example = "example.txt"
	Input   = "input.txt"
)

func parse(input string) ([]int, []int) {
	text, _ := os.ReadFile(input)
	return getLocationIds(string(text))
}

func getLocationIds(text string) ([]int, []int) {
	var left []int
	var right []int
	for _, line := range strings.Split(text, "\r\n") {
		ids := removeStringFromSlice(strings.Split(line, " "), "")
		l, _ := strconv.Atoi(ids[0])
		r, _ := strconv.Atoi(ids[1])
		left = append(left, l)
		right = append(right, r)
	}
	slices.Sort(left)
	slices.Sort(right)
	return left, right
}

func removeStringFromSlice(list []string, subString string) []string {
	var result []string
	for _, s := range list {
		if s != subString {
			result = append(result, s)
		}
	}
	return result
}

func getDistance(left []int, right []int) int {
	distance := 0
	for i := 0; i < len(left); i++ {
		distance += int(math.Abs(float64(left[i] - right[i])))
	}
	return distance
}

func getSimilarityScore(left []int, right []int) int {
	score := 0
	for i := 0; i < len(left); i++ {
		score += left[i] * getOccurrences(right, left[i])
	}
	return score
}

func getOccurrences(arr []int, num int) int {
	count := 0
	for _, n := range arr {
		if n == num {
			count++
		}
	}
	return count
}

func solve1(left []int, right []int) int {
	return getDistance(left, right)
}

func solve2(left []int, right []int) int {
	return getSimilarityScore(left, right)
}

func main() {
	left, right := parse(Input)
	fmt.Print("Answer to part 1: ", solve1(left, right), ".\n") // Correct answer for Part 1: 2904518.
	fmt.Print("Answer to part 2: ", solve2(left, right), ".")   // Correct answer for Part 2: 18650129.
}
