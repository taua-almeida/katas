package main

import (
	"errors"
	"flag"
)

func ParseArgs() error {
	language := flag.String("l", "", "Language to use for the kata [Required]")
	withChallenge := flag.Bool("with-challenge", false, "Include a challenge in the kata [False by default]")
	amount := flag.Int("a", 0, "Number of challenges to the kata [0 by default]")
	specificChallenge := flag.S("s", 0, "Specific challenge to include in the kata [0 by default]")

	flag.Parse()

	if *language == "" {
		return errors.New("You must specify a language to use for the kata")
	}

}
