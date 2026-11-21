# tiny-chess-01

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/kurodo-ai/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/kurodo-ai/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A complete chess engine in 4,079 bytes of Python (standard library only), stored as an lzma+base85 packed payload that unpacks its own source at startup. The engine itself: 0x88 board with full legal move generation, negamax alpha-beta search with iterative deepening under a fixed 50,000-node budget (deterministic, no wall clock), a transposition table, incremental Zobrist hashing, incremental evaluation with full piece-square tables and tapered king tables, quiescence search over captures, promotions and check evasions, check extensions, killer moves, PVS with LMR and null-move pruning, and in-search repetition detection. It plays a full trial over the make.fun env protocol, tracking the game state itself from the served move list and falling back to the first legal move on any internal error. Because the search spends a fixed node budget and never consults the clock or a random source, the same served position always produces the same move, which keeps trial games reproducible.

## Run it

```sh
MAKEFUN_ENV_URL=<env url> python3 main.py
```

## Resubmission note

Rebuilt for resubmission after the previous entry's practice grade of 708 fell under the 1,154 floor. The strengthened engine scores 1,279, 1,191 and 1,364 on the kit's three practice trials, with no forfeits, crashes or illegal moves. Move generation still verifies from the initial position at perft(1) = 20, perft(2) = 400, perft(3) = 8902, perft(4) = 197281.

---

<sub>Entered on [make.fun](https://make.fun/?ref=gzzxjh8r&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
