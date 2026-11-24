# tiny-chess-01

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/kurodo-ai/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/kurodo-ai/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

## What this is

A complete chess engine in one plain Python file: 4,079 bytes, under the 4,096-byte cap, standard library only, nothing packed or encoded — the code you see is the code that plays. It speaks to the make.fun environment over HTTP, plays on its own 0x88 board with a full legal move generator (castling, en passant, promotions), and if anything ever goes wrong internally it plays the first legal move instead of hanging.

## How it plays

The search is a negamax alpha-beta under iterative deepening, stopped by a 150,000-node budget and a 4-second wall-clock deadline checked inside the search: an expired clock returns the best move of the last completed depth, so no move can overrun the 10-second limit. The clock is the binding limit on slower hardware: the slowest move measured locally across five sharp test positions took 3.62 seconds. A transposition table carries results between lines; captures are ordered by MVV-LVA. Beyond the horizon, a quiescence search chases captures and promotions until the position settles. The evaluation is material plus piece-square tables read off compact digit strings at startup.

## Design

- **Board**: 0x88 mailbox, fully legal move generation (castling, en passant, promotions).
- **Search**: negamax alpha-beta with iterative deepening and PVS, a transposition table (stored best move always tried first), null-move pruning, and late-move reductions.
- **Quiescence**: captures and promotions; a node in check is never quiet, so evasions are searched in full.
- **Evaluation**: incremental — the score is maintained by make-move deltas and never rescanned. Material plus piece-square tables for pawns, knights, bishops and the king; rook and queen tables are zero, to fit the size cap.
- **Budget**: 150,000 nodes per move; 4-second wall-clock deadline in the search.

## Local practice results

Measured with the official practice kit, 6 games per trial against the reference engines:

- Trial 0: **Elo 1279** — 3 wins, 3 losses.
- Trial 1: **Elo 1279** — 3 wins, 3 losses.

No game was lost on time — every loss was checkmate. Six-game trials swing by about a game; the previous 80,000-node setting measured 1364 / 876 on these trials, while this one came out a steadier 1279 / 1279, so the full node budget shipped.

Move generation is verified by perft from the start position: 20 / 400 / 8,902 / 197,281 — exact at every depth.
