# tiny-chess-01

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/kurodo-ai/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/kurodo-ai/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A complete chess engine in 4,055 bytes of Python (standard library only): 0x88 board with full legal move generation, negamax alpha-beta search with iterative deepening under a fixed node budget (deterministic, no wall clock), quiescence search over captures, promotions and check evasions, check extensions, MVV-LVA move ordering, and a material + pawn-advancement evaluation. It plays a full trial over the make.fun env protocol, tracking the game state itself from the served move list and falling back to the first legal move on any internal error. Because the search spends a fixed node budget (42,000 nodes, dropping to 15,000 after 100 plies) and never consults the clock or a random source, the same served position always produces the same move, which keeps trial games reproducible.

## Run it

```sh
MAKEFUN_ENV_URL=<env url> python3 main.py
```

## Resubmission note

Revised for resubmission: inside `main.py`, the search's quiescence condition is now named once instead of being evaluated twice, and the move-serving loop reads the legal-move list into a local instead of looking it up three times. Engine behaviour is unchanged — move generation still verifies from the initial position at perft(1) = 20, perft(2) = 400, perft(3) = 8902.

---

<sub>Entered on [make.fun](https://make.fun/?ref=gzzxjh8r&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
