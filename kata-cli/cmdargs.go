package main

import (
	"errors"
	"flag"
)

func ParseArgs() error {
	language := flag.String("l", "", "Language to use for the kata [Required]")

	flag.Parse()

	if *language == "" {
		return errors.New("You must specify a language to use for the kata")
	}

}
