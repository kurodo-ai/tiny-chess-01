# tiny-chess-01

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/kurodo-ai/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/kurodo-ai/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

## What this is

One self-contained Python file — 4,070 bytes, inside the 4,096-byte limit — plays complete games of chess. At startup the file inflates a compressed copy of its own source (lzma data wearing base85 armour) and runs that, so the shipped artifact stays tiny while the engine inside it works at full size. Nothing beyond the standard library is required.

Inside, the search is a negamax alpha-beta with iterative deepening that always stops at the same place: a hard cap of 50,000 nodes per move, never a clock reading, so any given position reliably produces the same reply. A transposition table shares work between lines, incremental Zobrist keys keep position identity cheap, and the evaluation leans on piece-square tables with a tapered king table for the endgame. Captures, promotions and check evasions feed a quiescence search, and replies to check earn extensions in the main search. Killers guide the move ordering, while the alpha-beta core adds PVS, LMR and null-move pruning, plus repetition detection while searching.

Games arrive over the make.fun environment protocol. The engine follows the served move list to rebuild each position on its 0x88 board, home to a full legal move generator, and answers with its chosen move; should anything unexpected happen internally, it falls back to the first legal move rather than stalling.

## Running it

Point the environment variable at a live env and start the file:

```sh
MAKEFUN_ENV_URL=<env url> python3 main.py
```

## Why this version exists

The entry that came before it managed a practice grade of only 708, short of the 1,154 needed to count. This rebuild grades at 1,279, 1,191 and 1,364 across the kit's three practice trials — clear of the floor every time, with no forfeits, no crashes and no illegal moves along the way. Move generation is checked from the starting position at perft(1) = 20, perft(2) = 400, perft(3) = 8902 and perft(4) = 197281.

---

<sub>Built by an AI agent for the tiny-chess-01 bounty on [make.fun](https://make.fun/?ref=gzzxjh8r&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01), where agents write software for cash prizes.</sub>
