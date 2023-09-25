# Bowling Game Kata 

The Bowling Game Kata is a coding exercise used primarily for practicing the Test-Driven Development (TDD) process, but it also helps in understanding how to model a real-world problem.

And my take is that TDD is cool, but you should do the kata for practicing programming and warmup your brain.

### Bowling Game Rule:

#### 1. Frames:

* A game consists of 10 frames.
* In general, each frame can have 1 or 2 rolls.
* The 10th frame might have 2 or 3 rolls, specifically if the player rolls a strike or spare.


#### 2. Scoring:

* If a bowler knocks down all ten pins in the first roll of a frame, it is called a "strike" and the frame is over. The score for that frame is 10 plus the sum of the next two rolls.
* If a bowler knocks down all ten pins after two rolls in a frame, it is called a "spare". The score for that frame is 10 plus the score of the next roll.
* If a bowler doesn't knock down all the pins in a frame (i.e., no strike or spare), the score for that frame is the total number of pins knocked down in those 2 rolls.
* The 10th frame has some special rules:
* If a strike is rolled, the bowler gets two more rolls.
* If a spare is rolled, the bowler gets one more roll.
* These additional rolls are used to calculate the score of the 10th frame, but they don't count as separate frames.

#### Expected Inputs and Outputs:

**Inputs:**

Number of pins knocked down in each roll.

**Outputs:**

Total score of the game.

### Input and Output Examples:

**Basic Scoring:**

#### 1. All gutter balls (no pins knocked down in any roll):**

Input:
```perl
Roll 20 times with 0 pins knocked down each time.
```
Output:
```mathematica
Total score: 0
```

#### 2. All rolls knock down one pin:

Input:
```perl
Roll 20 times with 1 pin knocked down each time.
```
Output:
```mathematica
Total score: 20
```

**Scoring with Spares:**

#### 1. Roll a spare in the first frame, then 3 pins, and all the rest are gutter balls:

Input:
```perl
Roll 5 pins.
Roll 5 pins.  (This completes the spare)
Roll 3 pins.
Roll 17 times with 0 pins knocked down each time.
```
Output:
```mathematica
Total score: 16 (10 for the spare, plus 3 for the bonus, plus 3)
```

**Scoring with Strikes:**

#### 1. Roll a strike in the first frame, then 3 pins and 4 pins, and all the rest are gutter balls:

Input:
```perl
Roll a strike (10 pins).
Roll 3 pins.
Roll 4 pins.
Roll 16 times with 0 pins knocked down each time.
```
Output:
```mathematica
Total score: 24 (10 for the strike, plus 7 for the bonus, plus 3, plus 4)
```

**Perfect Game:**

#### 1. Every roll is a strike:

Input:
```perl
Roll a strike (10 pins) 12 times.
```
Output:
```mathematica
Total score: 300
```